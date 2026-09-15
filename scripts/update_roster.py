#!/usr/bin/env python3
"""Regenerate roster tables from live Sleeper data.

Two outputs, both for the team named TEAM_NAME:
  1. OPS-MANUAL.md — rewrites only the block between <!-- ROSTER:START -->
     and <!-- ROSTER:END -->. Everything else in the manual is left alone.
  2. docs/_data/roster.yml — one row per roster spot (slot, player, pos,
     team, status, acquired, acquired_via, acquired_week) that the public
     site's roster page renders.

Every row carries how and when the player was acquired, derived from the
league's draft picks and every completed transaction since week 1, so the
site can show "Draft" or "Wk N" next to each player without anyone keeping
a ledger by hand.

Also checks docs/_data/notes.yml (Claude's one-line note per player) against
the roster and prints NOTE MISSING / NOTE ORPHAN lines. Those are warnings for
the run to act on, not errors; the exit code stays 0.

Meant to run right after pull_sleeper.py (locally or in GitHub Actions).
"""

import json
import re
import sys
from pathlib import Path

from pull_sleeper import BASE, DATA_DIR, SPORT, USERNAME, get, resolve_league, slim_players

TEAM_NAME = "Gradient Ascent"
ROOT = Path(__file__).resolve().parent.parent
MANUAL = ROOT / "OPS-MANUAL.md"
SITE_DATA = ROOT / "docs" / "_data" / "roster.yml"
NOTES = ROOT / "docs" / "_data" / "notes.yml"
START, END = "<!-- ROSTER:START -->", "<!-- ROSTER:END -->"

# Order the manual presents starters in (differs from Sleeper's TE/FLEX order)
SLOT_ORDER = ["QB", "RB", "RB", "WR", "WR", "FLEX", "TE", "K", "DEF"]
POS_RANK = {"QB": 0, "RB": 1, "WR": 2, "TE": 3, "K": 4, "DEF": 5}

# Sleeper transaction types -> how the site labels the acquisition
VIA_LABEL = {
    "free_agent": "free agent",
    "waiver": "waiver claim",
    "trade": "trade",
    "commissioner": "commissioner",
}


def find_roster(league_id: str):
    users = get(f"{BASE}/league/{league_id}/users")
    rosters = get(f"{BASE}/league/{league_id}/rosters")
    owner = next((u for u in users if (u.get("metadata") or {}).get("team_name") == TEAM_NAME), None)
    if owner is None:  # team name unset in Sleeper -> fall back to Sean's account
        owner = next((u for u in users if u.get("display_name") == USERNAME), None)
    if owner is None:
        sys.exit(f"No team '{TEAM_NAME}' (or user {USERNAME}) in league {league_id}")
    uid = owner["user_id"]
    for r in rosters:
        if r.get("owner_id") == uid or uid in (r.get("co_owners") or []):
            return r
    sys.exit(f"No roster owned by {uid} in league {league_id}")


def load_players() -> dict:
    cache = DATA_DIR / "players_slim.json"
    if cache.exists():
        return json.loads(cache.read_text(encoding="utf-8"))
    return slim_players(get(f"{BASE}/players/nfl"))


def display_name(pid, players: dict) -> str:
    p = players.get(str(pid))
    if not p:
        return str(pid)
    name = p.get("name") or str(pid)
    if p.get("pos") == "DEF":  # "Buffalo Bills" -> "Buffalo", matching manual style
        name = name.rsplit(" ", 1)[0]
    return name


def current_week() -> int:
    state = get(f"{BASE}/state/{SPORT}")
    return int(state.get("week") or 1)


def acquisitions(league_id: str, roster_id: int, week: int) -> dict:
    """pid -> {ts, week, via, detail} for every player this roster ever acquired.

    Draft picks come first; any completed transaction that added the player to
    this roster afterwards overrides them, latest transaction winning. A player
    drafted, dropped, and re-added therefore shows the re-add.
    """
    acq: dict = {}
    for d in get(f"{BASE}/league/{league_id}/drafts") or []:
        if d.get("status") != "complete":
            continue
        for p in get(f"{BASE}/draft/{d['draft_id']}/picks") or []:
            if p.get("roster_id") == roster_id and p.get("player_id"):
                acq[str(p["player_id"])] = {
                    "ts": 0, "week": 0, "via": "draft",
                    "detail": f"R{p.get('round')}, pick {p.get('pick_no')}",
                }
    for w in range(1, max(week, 1) + 1):
        for tx in get(f"{BASE}/league/{league_id}/transactions/{w}") or []:
            if tx.get("status") != "complete":
                continue
            for pid, rid in (tx.get("adds") or {}).items():
                if rid != roster_id:
                    continue
                ts = int(tx.get("created") or 0)
                if ts < acq.get(str(pid), {}).get("ts", -1):
                    continue
                via = tx.get("type") or "?"
                acq[str(pid)] = {
                    "ts": ts, "week": int(tx.get("leg") or w), "via": via,
                    "detail": VIA_LABEL.get(via, via.replace("_", " ")),
                }
    return acq


def roster_rows(roster: dict, roster_positions: list, players: dict, acq: dict) -> list:
    """[{slot, pid, player, pos, team, status, acquired, acquired_via, acquired_week}]
    in manual order: starters then bench."""
    starters = roster.get("starters") or []
    # Sleeper aligns starters[i] with roster_positions[i]; bucket by slot label
    by_slot: dict[str, list] = {}
    for slot, pid in zip(roster_positions, starters):
        if slot != "BN":
            by_slot.setdefault(slot, []).append(pid)

    def row(slot, pid):
        p = players.get(str(pid)) or {}
        empty = pid in (None, "0", 0)
        a = {} if empty else acq.get(str(pid), {})
        if empty or not a:
            acquired, via, wk = "", "", -1
        elif a["via"] == "draft":
            acquired, via, wk = "Draft", a["detail"], 0
        else:
            acquired, via, wk = f"Wk {a['week']}", a["detail"], a["week"]
        return {
            "slot": slot,
            "pid": None if empty else str(pid),
            "player": "—" if empty else display_name(pid, players),
            "pos": "" if empty else (p.get("pos") or ""),
            "team": "" if empty else (p.get("team") or "FA"),
            "status": "" if empty else (p.get("injury_status") or ""),
            "acquired": acquired,
            "acquired_via": via,
            "acquired_week": wk,
        }

    rows = []
    for slot in SLOT_ORDER:
        pid = by_slot.get(slot, []).pop(0) if by_slot.get(slot) else None
        rows.append(row(slot, pid))

    starter_ids = {str(s) for s in starters}
    bench_ids = [p for p in (roster.get("players") or []) if str(p) not in starter_ids]
    # Sleeper lists players in ID order; sort bench by position, then name
    bench_ids.sort(key=lambda p: (POS_RANK.get((players.get(str(p)) or {}).get("pos"), 9), display_name(p, players)))
    for i, pid in enumerate(bench_ids, 1):
        rows.append(row(f"BN{i}", pid))
    return rows


def acquired_label(r: dict) -> str:
    if not r["acquired"]:
        return "—"
    return f"{r['acquired']} ({r['acquired_via']})" if r["acquired_via"] else r["acquired"]


def build_table(rows: list) -> str:
    out = ["| Slot | Player | Acquired |", "|------|--------|----------|"]
    for r in rows:
        slot = "BN" if r["slot"].startswith("BN") else r["slot"]
        out.append(f"| {slot} | {r['player']} | {acquired_label(r)} |")
    return "\n".join(out)


def yaml_str(s: str) -> str:
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def build_site_data(rows: list) -> str:
    lines = ["# Generated by scripts/update_roster.py from Sleeper. Do not edit by hand;",
             "# it is overwritten after every data pull. Player notes live in notes.yml.",
             "# acquired is \"Draft\" or \"Wk N\"; acquired_via says how (round and pick,",
             "# free agent, waiver claim, trade); acquired_week is 0 for the draft."]
    for r in rows:
        lines.append(f"- slot: {yaml_str(r['slot'])}")
        for k in ("player", "pos", "team", "status", "acquired", "acquired_via"):
            lines.append(f"  {k}: {yaml_str(r[k])}")
        lines.append(f"  acquired_week: {r['acquired_week']}")
    return "\n".join(lines) + "\n"


def read_note_keys(path: Path) -> list:
    """Player names that have a note in notes.yml. The file is one
    `"Name": "note"` pair per line; this parses only that shape, on purpose,
    so the format stays simple enough for a routine to edit safely."""
    if not path.exists():
        return []
    keys = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r'^"((?:[^"\\]|\\.)*)"\s*:', line)
        if m:
            keys.append(m.group(1).replace('\\"', '"').replace("\\\\", "\\"))
    return keys


def check_notes(rows: list) -> None:
    keys = set(read_note_keys(NOTES))
    on_roster = {r["player"] for r in rows if r["pid"]}
    missing = [r for r in rows if r["pid"] and r["player"] not in keys]
    orphans = sorted(keys - on_roster)
    for r in missing:
        print(f"NOTE MISSING: {r['player']} ({r['slot']}, {acquired_label(r)}) has no line in docs/_data/notes.yml")
    for name in orphans:
        print(f"NOTE ORPHAN: {name} has a note but is not on the roster")
    if not missing and not orphans:
        print("OK: notes.yml covers the roster exactly")


def main():
    text = MANUAL.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(text):
        sys.exit(f"{MANUAL.name}: missing {START} / {END} markers")

    _, league = resolve_league()
    lid = league["league_id"]
    roster = find_roster(lid)
    acq = acquisitions(lid, roster["roster_id"], current_week())
    rows = roster_rows(roster, league.get("roster_positions") or [], load_players(), acq)

    table = build_table(rows)
    new_text = pattern.sub(lambda _m: f"{START}\n{table}\n{END}", text, count=1)
    if new_text == text:
        print("OK: roster table unchanged")
    else:
        MANUAL.write_text(new_text, encoding="utf-8")
        print(f"OK: updated roster table in {MANUAL.name}")

    SITE_DATA.parent.mkdir(parents=True, exist_ok=True)
    site = build_site_data(rows)
    if SITE_DATA.exists() and SITE_DATA.read_text(encoding="utf-8") == site:
        print("OK: docs/_data/roster.yml unchanged")
    else:
        SITE_DATA.write_text(site, encoding="utf-8")
        print("OK: wrote docs/_data/roster.yml")

    check_notes(rows)


if __name__ == "__main__":
    main()
