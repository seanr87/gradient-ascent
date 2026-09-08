# Task: Sunday final lineup (Sun 9:00 AM ET)

Read `tasks/COMMON.md` first and follow it. This task produces the **final Sunday lineup**. Early games lock at 1:00 PM ET, so the output must be complete and paste-ready.

## Data
The scheduled pull commits a fresh digest at about 8:00 AM ET this morning. Freshness limit: 2 hours; refresh per COMMON.md if older. Then use web search for injury and inactive news on every starter or candidate carrying a designation, and cite what you found. Roster slots: 1 QB, 2 RB, 2 WR, 1 TE, 1 FLEX (RB/WR/TE), 1 K, 1 DEF, 5 bench, no IR.

## The lineup
Fill all nine starting slots and list the five bench players. Apply the manual's edges: the first-down bonus favors high-touch backs and chain-moving receivers over big-play-dependent players; rushing QBs spike; distance kicker scoring; DEF by matchup. A player tagged Out or Doubtful does not start. A Questionable player starts only if the alternative is clearly worse, and you must name the bench alternative and the game time so Sean can swap before lock if news breaks. Players on bye do not start. Note any Monday night player and whether starting him leaves a slot exposed with no fallback. Respect any Thursday player already locked in by this week's Thursday file.

Flag every change from the prior week's lineup (last Sunday's file) with a one-line reason. If a slot has no viable player, say so and give an emergency `ADD [player] / DROP [player]`.

## File
`docs/_decisions/2026-wkNN-sun-lineup.md`, kind `lineup`, title `Week NN lineup`. Sections:
- metadata line: decision time (ET), digest pulled timestamp, opponent this week (from `my_opponent_this_week`)
- `## Starters` as a table: Slot, Player, Team, Game time (ET) if known, Status, Changed? (Yes with reason, or blank)
- `## Bench`
- `## Contingencies` ("if X is ruled out, start Y" for every Questionable starter)
- `## The matchup` (two or three sentences on the opponent's lineup and where the week is won or lost)
- `## For the clipboard` (the nine `SLOT: Player` lines, then the contingency lines, nothing else)

Commit message: `Week NN lineup: <summary>`.
