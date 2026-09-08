#!/usr/bin/env python3
"""Regenerate the roster table in OPS-MANUAL.md from live Sleeper data.

Rewrites only the block between <!-- ROSTER:START --> and <!-- ROSTER:END -->
for the team named TEAM_NAME. Everything else in the manual is left alone.
Meant to run right after pull_sleeper.py (locally or in GitHub Actions).
"""

import json
import re
import sys
from pathlib import Path

from pull_sleeper import BASE, DATA_DIR, USERNAME, get, resolve_league, slim_players

TEAM_NAME = "Gradient Ascent"
MANUAL = Path(__file__).resolve().parent.parent / "OPS-MANUAL.md"
START, END = "<!-- ROSTER:START -->", "<!-- ROSTER:END -->"

# Order the manual presents starters in (differs from Sleeper's TE/FLEX order)
SLOT_ORDER = ["QB", "RB", "RB", "WR", "WR", "FLEX", "TE", "K", "DEF"]


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
        return json.loads(cache.read_text())
    return slim_players(get(f"{BASE}/players/nfl"))


def display_name(pid, players: dict) -> str:
    p = players.get(str(pid))
    if not p:
        return str(pid)
    name = p.get("name") or str(pid)
    if p.get("pos") == "DEF":  # "Buffalo Bills" -> "Buffalo", matching manual style
        name = name.rsplit(" ", 1)[0]
    return name


def build_table(roster: dict, roster_positions: list, players: dict) -> str:
    starters = roster.get("starters") or []
    # Sleeper aligns starters[i] with roster_positions[i]; bucket by slot label
    by_slot: dict[str, list] = {}
    for slot, pid in zip(roster_positions, starters):
        if slot != "BN":
            by_slot.setdefault(slot, []).append(pid)

    rows = []
    for slot in SLOT_ORDER:
        pid = by_slot.get(slot, []).pop(0) if by_slot.get(slot) else None
        name = "—" if pid in (None, "0", 0) else display_name(pid, players)
        rows.append(f"| {slot} | {name} |")

    starter_ids = {str(s) for s in starters}
    bench_ids = [p for p in (roster.get("players") or []) if str(p) not in starter_ids]
    # Sleeper lists players in ID order; sort bench by position, then name
    pos_rank = {"QB": 0, "RB": 1, "WR": 2, "TE": 3, "K": 4, "DEF": 5}
    bench_ids.sort(key=lambda p: (pos_rank.get((players.get(str(p)) or {}).get("pos"), 9), display_name(p, players)))
    bench = [display_name(p, players) for p in bench_ids]
    rows.append(f"| BN | {', '.join(bench) if bench else '—'} |")

    return "\n".join(["| Slot | Player |", "|------|--------|", *rows])


def main():
    text = MANUAL.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(text):
        sys.exit(f"{MANUAL.name}: missing {START} / {END} markers")

    _, league = resolve_league()
    roster = find_roster(league["league_id"])
    table = build_table(roster, league.get("roster_positions") or [], load_players())

    new_text = pattern.sub(lambda _m: f"{START}\n{table}\n{END}", text, count=1)
    if new_text == text:
        print("OK: roster table unchanged")
        return
    MANUAL.write_text(new_text, encoding="utf-8")
    print(f"OK: updated roster table in {MANUAL.name}")


if __name__ == "__main__":
    main()
