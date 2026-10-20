# Task: Wednesday post-waiver review (Wed 12:00 PM ET)

Read `tasks/COMMON.md` first and follow it. This task produces the **post-waiver review**. Waivers cleared at 3:00 AM ET this morning.

## Run once a week — check this first
**If `docs/_decisions/2026-wkNN-wed-review.md` already exists for this week, stop.** Do not write a second one and never edit the first. Give the standard three-line report from the existing file (its `**Do by:**` line, its `## For the clipboard` section in a code fence, its page link), send no push notification, and stop. Refreshing and committing the digest per COMMON is fine; writing a second review is not. Two routines may fire this task until the old UI-created one is disabled (see `SCHEDULED-TASKS.md`); both firing must be harmless.

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
`docs/_decisions/2026-wkNN-wed-review.md`, kind `review`, title `Week NN post-waiver review`, in the structure COMMON.md fixes:
- `**Do by:**` "now" for any pivot add (free agency is first-come) · `**Digest:**` pulled timestamp
- `## For the clipboard`: pivot ADD/DROP lines or `NO ACTION`
- `## Why`: one line per Tuesday claim (cleared, or who got him and at what priority), one line per pivot add, then at most 3 passed-on players
- `## Detail` (optional, 250 words max): notable moves by other managers and what each signals, any starting slot that now looks different for Sunday, sources as one line of links

Update `## State` and `## Open threads` in `data/ledger.md` in the same commit: close each cleared or lost claim's thread, add a thread for every pivot add and for any missed player worth a Thursday look.

Do not hand-edit the roster table in `OPS-MANUAL.md`; the pull workflow regenerates it.

Commit message: `Week NN post-waiver review: <summary>`.
