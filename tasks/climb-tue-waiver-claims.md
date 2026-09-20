# Task: Tuesday waiver claims (Tue 6:00 PM ET)

Read `tasks/COMMON.md` first and follow it. This task produces this week's **waiver claims**. Waivers process Wednesday 3:14 AM ET (confirmed from the league transaction log, not from settings).

## Run once a week — check this first

**If `docs/_decisions/2026-wkNN-tue-waivers.md` already exists for this week, stop. Do not write a second one and do not edit the first.**

Two routines currently fire this task: the intended one at **6:00 PM ET**, and an older duplicate at **9:30 PM ET** that only Sean can remove (see the editing constraint in `SCHEDULED-TASKS.md`). The 6:00 PM run writes the file. The 9:30 PM run must find it and exit, because a decision file is written once and never revised — that is COMMON's rule and it outranks this task.

On finding the file already written, do this and nothing else: confirm it is this week's, report its path, its commit, and its `## For the clipboard` section verbatim so the lines are in front of Sean one more time before the run, and send no push notification — the 6:00 PM run already sent one and `climb-tue-waiver-check` covers the alarm at 10:30 PM. Then stop. Refreshing and committing the digest per COMMON is fine and worth doing; writing a decision is not.

If the file does **not** exist, you are the run that writes it. Continue.

## Data
COMMON.md already refreshed the digest at the start of this run; confirm the "Pulled:" line is from the last few minutes before deciding. Tonight's data matters more than any other run's: it is the last look before waivers process.

## The decision
Evaluate the free-agent and waiver pool against every roster spot using the manual's scoring edges: +0.5 per rushing/receiving first down (volume and possession players spike), rushing QBs spike, -2 INT and 4-pt pass TD sink pocket passers, distance kicker scoring, streamable DEF by matchup, and no IR slot so injured players occupy real roster space. Weigh the trending-adds list as a signal of who other managers will chase, and my waiver position from the standings.

Produce a ranked claim list, at most five claims. Each claim is one line in exactly this form, followed by a one-line reason:

```
ADD [player, position-team] / DROP [player, position-team]
```

For every player you claim, add his line to `docs/_data/notes.yml` in this commit (COMMON.md, Roster notes): the reason in the claim, compressed to a sentence or two in my voice. Rank claims in the order Sean should enter them; Sleeper processes in priority order and cancels later claims that reuse a drop that already succeeded. Say explicitly when a claim is a conditional backup for an earlier one. If the correct call is no claims, write `NO CLAIMS` and explain in one paragraph.

## File
`docs/_decisions/2026-wkNN-tue-waivers.md`, kind `waivers`, title `Week NN waiver claims`. Sections:
- metadata line: decision time (ET) and digest pulled timestamp
- `## Claims (enter in this order)`
- `## Reasoning` (a short paragraph per claim, plus notable players passed on and why)
- `## For the clipboard` (only the ADD/DROP lines, or `NO ACTION`)

Commit message: `Week NN waiver claims: <summary>`.
