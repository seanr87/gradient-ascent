# Task: Sunday final lineup (Sun 9:00 AM ET)

Read `tasks/COMMON.md` first and follow it. This task produces the **final Sunday lineup**. Early games lock at 1:00 PM ET, so the output must be complete and paste-ready.

## Data
COMMON.md already refreshed the digest at the start of this run; confirm the "Pulled:" line is from the last few minutes. Then use web search for injury and inactive news on every starter or candidate carrying a designation, and cite what you found. Roster slots: 1 QB, 2 RB, 2 WR, 1 TE, 1 FLEX (RB/WR/TE), 1 K, 1 DEF, 5 bench, no IR.

## The lineup
Fill all nine starting slots and list the five bench players. Apply the manual's edges: the first-down bonus favors high-touch backs and chain-moving receivers over big-play-dependent players; rushing QBs spike; distance kicker scoring; DEF by matchup. A player tagged Out or Doubtful does not start. A Questionable player starts only if the alternative is clearly worse, and you must name the bench alternative and the game time so Sean can swap before lock if news breaks. Players on bye do not start. Note any Monday night player and whether starting him leaves a slot exposed with no fallback. Respect any Thursday player already locked in by this week's Thursday file.

Flag every change from the prior week's lineup (last Sunday's file) with a one-line reason. If a slot has no viable player, say so and give an emergency `ADD [player] / DROP [player]`, and write the added player's line in `docs/_data/notes.yml` in this commit (COMMON.md, Roster notes).

## File
`docs/_decisions/2026-wkNN-sun-lineup.md`, kind `lineup`, title `Week NN lineup`, in the structure COMMON.md fixes:
- `**Do by:**` the earliest lock among the nine (usually 1:00 PM ET), plus any earlier deadline for an emergency add · `**Digest:**` pulled timestamp and opponent (from `my_opponent_this_week`)
- `## For the clipboard`: the nine `SLOT: Player` lines, then any emergency `ADD / DROP`, then the contingency lines (`IF X is inactive by <time> — START Y at <slot>`), nothing else
- `## Why`: one line per changed slot (what changed and why), one line per Questionable starter (status, game time, the bench alternative), and one line per Monday-night starter naming the fallback or saying none exists; then at most 3 passed-on bench players
- `## Detail` (optional, 250 words max): the bench, two or three sentences on the opponent's lineup and where the week is won or lost, sources as one line of links

A contingency must be executable: name a swap Sean can make before the earliest lock involved, and prefer the line that maximizes the slot over the one that insures it (Lesson 3). Update `## State` and `## Open threads` in `data/ledger.md` in the same commit: each contingency as a thread with its check time.

Commit message: `Week NN lineup: <summary>`.
