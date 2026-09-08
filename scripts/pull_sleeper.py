#!/usr/bin/env python3
"""Pull Sleeper league data into data/ as a Claude-ready digest.

Read-only, no auth. Resolves league by username + season so you never
need to hunt for the league ID. Run locally or via GitHub Actions.

Outputs (all in data/):
  digest.json       full structured dump: league, rosters, standings, this
                    week's and last week's matchups with points, transactions,
                    trending adds/drops
  digest.md         human/Claude-readable summary of the same
  players_slim.json name / pos / team / injury lookup for fantasy positions
"""

import json
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

USERNAME = "seanroreilly87"
SEASON = "2026"
LEAGUE_NAME = "The Climb"  # used to pick the right league if you're in several
SPORT = "nfl"
BASE = "https://api.sleeper.app/v1"
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

# Positions worth keeping when we slim the giant players database
KEEP_POS = {"QB", "RB", "WR", "TE", "K", "DEF"}


def get(url: str):
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)


def resolve_league():
    user = get(f"{BASE}/user/{USERNAME}")
    leagues = get(f"{BASE}/user/{user['user_id']}/leagues/{SPORT}/{SEASON}")
    for lg in leagues:
        if lg["name"] == LEAGUE_NAME:
            return user, lg
    if len(leagues) == 1:
        return user, leagues[0]
    names = [lg["name"] for lg in leagues]
    sys.exit(f"League '{LEAGUE_NAME}' not found. Available: {names}")


def slim_players(players: dict) -> dict:
    """The full player DB is ~5 MB; keep only fantasy-relevant fields."""
    slim = {}
    for pid, p in players.items():
        if not isinstance(p, dict) or p.get("position") not in KEEP_POS:
            continue
        slim[pid] = {
            "name": p.get("full_name") or f"{p.get('first_name','')} {p.get('last_name','')}".strip(),
            "pos": p.get("position"),
            "team": p.get("team"),
            "status": p.get("status"),
            "injury_status": p.get("injury_status"),
            "injury_note": p.get("injury_body_part"),
        }
    return slim


def team_label(user: dict) -> str:
    """Sleeper team name if set, else the manager's display name."""
    return (user.get("metadata") or {}).get("team_name") or user.get("display_name") or "?"


def pair_matchups(matchups: list, label_by_roster: dict) -> list:
    """Group Sleeper's flat matchup rows into [{matchup_id, teams:[{team, roster_id, points}]}]."""
    groups: dict = {}
    for m in matchups or []:
        groups.setdefault(m.get("matchup_id"), []).append({
            "roster_id": m.get("roster_id"),
            "team": label_by_roster.get(m.get("roster_id"), "?"),
            "points": round(float(m.get("points") or 0), 2),
        })
    out = []
    for mid, teams in groups.items():
        teams.sort(key=lambda t: -t["points"])
        out.append({"matchup_id": mid, "teams": teams})
    out.sort(key=lambda g: (g["matchup_id"] is None, g["matchup_id"] or 0))
    return out


def standings(rosters: list, label_by_roster: dict) -> list:
    rows = []
    for r in rosters:
        s = r.get("settings") or {}
        pf = float(s.get("fpts") or 0) + float(s.get("fpts_decimal") or 0) / 100
        pa = float(s.get("fpts_against") or 0) + float(s.get("fpts_against_decimal") or 0) / 100
        rows.append({
            "roster_id": r["roster_id"],
            "team": label_by_roster.get(r["roster_id"], "?"),
            "wins": s.get("wins") or 0, "losses": s.get("losses") or 0, "ties": s.get("ties") or 0,
            "points_for": round(pf, 2), "points_against": round(pa, 2),
            "waiver_position": s.get("waiver_position"),
        })
    rows.sort(key=lambda x: (-x["wins"], x["losses"], -x["points_for"]))
    return rows


def main():
    DATA_DIR.mkdir(exist_ok=True)
    now = datetime.now(timezone.utc)

    user, league = resolve_league()
    lid = league["league_id"]

    state = get(f"{BASE}/state/{SPORT}")           # current NFL week
    week = state.get("week") or 1
    season_type = state.get("season_type")        # pre / regular / post
    prev_week = week - 1 if week > 1 else None

    rosters = get(f"{BASE}/league/{lid}/rosters")
    users = get(f"{BASE}/league/{lid}/users")
    matchups = get(f"{BASE}/league/{lid}/matchups/{week}")
    matchups_prev = get(f"{BASE}/league/{lid}/matchups/{prev_week}") if prev_week else []
    transactions = get(f"{BASE}/league/{lid}/transactions/{week}")
    trending_add = get(f"{BASE}/players/{SPORT}/trending/add?lookback_hours=24&limit=50")
    trending_drop = get(f"{BASE}/players/{SPORT}/trending/drop?lookback_hours=24&limit=50")
    players = slim_players(get(f"{BASE}/players/{SPORT}"))

    # Map roster_id -> manager display name and team label, and find Sean's roster
    user_by_id = {u["user_id"]: u for u in users}
    owner_by_roster, label_by_roster = {}, {}
    my_roster = None
    for r in rosters:
        u = user_by_id.get(r.get("owner_id")) or {}
        owner_by_roster[r["roster_id"]] = u.get("display_name", "?")
        label_by_roster[r["roster_id"]] = team_label(u) if u else "?"
        if r.get("owner_id") == user["user_id"]:
            my_roster = r

    this_week = pair_matchups(matchups, label_by_roster)
    last_week = pair_matchups(matchups_prev, label_by_roster)
    table = standings(rosters, label_by_roster)

    my_rid = my_roster["roster_id"] if my_roster else None
    my_matchup = next((g for g in this_week if any(t["roster_id"] == my_rid for t in g["teams"])), None)
    my_opponent = None
    if my_matchup:
        my_opponent = next((t["team"] for t in my_matchup["teams"] if t["roster_id"] != my_rid), None)

    digest = {
        "pulled_at_utc": now.isoformat(timespec="seconds"),
        "nfl_week": week,
        "season_type": season_type,
        "league": {"id": lid, "name": league["name"], "scoring": league.get("scoring_settings"),
                   "roster_positions": league.get("roster_positions")},
        "my_roster": my_roster,
        "my_opponent_this_week": my_opponent,
        "owner_by_roster_id": owner_by_roster,
        "team_by_roster_id": label_by_roster,
        "standings": table,
        "matchups_this_week": matchups,
        "scores_this_week": this_week,
        "scores_last_week": last_week,
        "transactions_this_week": transactions,
        "trending_adds_24h": trending_add,
        "trending_drops_24h": trending_drop,
        "all_rosters": rosters,
    }

    (DATA_DIR / "digest.json").write_text(json.dumps(digest, indent=1), encoding="utf-8")
    (DATA_DIR / "players_slim.json").write_text(json.dumps(players, indent=1), encoding="utf-8")

    # Human/Claude-readable summary
    def pname(pid):
        p = players.get(str(pid), {})
        tag = f" [{p.get('injury_status')}]" if p.get("injury_status") else ""
        return f"{p.get('name', pid)} ({p.get('pos','?')}-{p.get('team','FA')}){tag}"

    def score_lines(groups):
        out = []
        for g in groups:
            t = g["teams"]
            if len(t) == 2:
                out.append(f"- {t[0]['team']} {t[0]['points']:.2f} — {t[1]['team']} {t[1]['points']:.2f}")
            else:
                out.append("- " + ", ".join(f"{x['team']} {x['points']:.2f}" for x in t))
        return out or ["- (no matchups)"]

    lines = [
        f"# Sleeper digest — {league['name']}",
        f"Pulled: {now.strftime('%Y-%m-%d %H:%M UTC')} · NFL week {week} ({season_type})",
        "",
        "## My roster",
    ]
    if my_roster:
        for pid in my_roster.get("players") or []:
            starter = " (STARTER)" if pid in (my_roster.get("starters") or []) else ""
            lines.append(f"- {pname(pid)}{starter}")
    if my_opponent:
        lines += ["", f"## My matchup this week", f"- Opponent: {my_opponent}"]

    lines += ["", "## Standings (W-L, points for)"]
    for i, row in enumerate(table, 1):
        wp = f", waiver #{row['waiver_position']}" if row.get("waiver_position") else ""
        lines.append(f"{i}. {row['team']} — {row['wins']}-{row['losses']}"
                     f"{'-' + str(row['ties']) if row['ties'] else ''}, {row['points_for']:.2f} PF{wp}")

    lines += ["", f"## This week's matchups (week {week})"] + score_lines(this_week)
    if prev_week:
        lines += ["", f"## Last week's results (week {prev_week})"] + score_lines(last_week)

    lines += ["", "## Trending adds (24h, all Sleeper)"]
    for t in trending_add[:25]:
        lines.append(f"- {pname(t['player_id'])} — {t['count']:,} adds")
    lines += ["", "## League transactions this week"]
    for tx in transactions[:30]:
        adds = ", ".join(pname(p) for p in (tx.get("adds") or {}))
        drops = ", ".join(pname(p) for p in (tx.get("drops") or {}))
        who = ", ".join(label_by_roster.get(rid, "?") for rid in (tx.get("roster_ids") or []))
        lines.append(f"- {tx['type']} ({tx['status']}) {who}: +[{adds}] -[{drops}]")

    (DATA_DIR / "digest.md").write_text("\n".join(lines) + "\n")
    print(f"OK: week {week}, {len(players)} players, wrote data/digest.json, players_slim.json, digest.md")


if __name__ == "__main__":
    main()
