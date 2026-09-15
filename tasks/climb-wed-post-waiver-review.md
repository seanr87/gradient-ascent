# Task: Wednesday post-waiver review (Wed 12:00 PM ET)

Read `tasks/COMMON.md` first and follow it. This task produces the **post-waiver review**. Waivers cleared at 3:00 AM ET this morning.

## Data
COMMON.md already refreshed the digest at the start of this run. Confirm the "Pulled:" line is from this morning, after waivers cleared at 3:00 AM ET; the transactions list is the whole point of this task.

## The review
Compare Tuesday's claim file (`docs/_decisions/2026-wkNN-tue-waivers.md`) against the transactions that actually processed:
- Which of my claims cleared and which did not, and who beat me to each miss and at what priority.
- Notable moves by the other eleven managers, with a one-line read on what each is signaling.
- Roster implications: is the roster still the one I planned around, and does any starting slot look different for Sunday.
- Any pivot: free agents still available worth an immediate add (free agency is first-come after waivers clear), as `ADD [player] / DROP [player]` lines with a reason, or `NO MOVES`.

Ruthless indifference: no consolation adds, no loyalty.

Roster notes (COMMON.md): the refresh will print `NOTE MISSING` for any claim that cleared without a note and `NOTE ORPHAN` for every player dropped this morning. Write the missing ones, delete the orphans, and write a note for every pivot `ADD` in this file, all in this commit. This is the run where the roster page most often falls behind, so do not skip it.

## File
`docs/_decisions/2026-wkNN-wed-review.md`, kind `review`, title `Week NN post-waiver review`. Sections:
- metadata line: decision time (ET) and digest pulled timestamp
- `## What cleared` (claim, result, who got him if not me)
- `## Around the league`
- `## Roster implications`
- `## For the clipboard` (ADD/DROP lines or `NO ACTION`)

Do not hand-edit the roster table in `OPS-MANUAL.md`; the pull workflow regenerates it.

Commit message: `Week NN post-waiver review: <summary>`.
