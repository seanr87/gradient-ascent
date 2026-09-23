# Task: League chat (Mon 8:00 PM ET)

Read `tasks/COMMON.md` first and follow it. This task writes one **league chat message** for Sean to paste into The Climb's Sleeper chat. It is deliberately low stakes: it exists to exercise the whole pipeline every week (pull data, read it, decide, commit, publish, notify) on something that cannot cost a game. Treat it with exactly the same rigor as a lineup call anyway.

## Data
COMMON.md already refreshed and committed the digest at the start of this run; that commit stands even if you end up skipping. Use whichever week in `data/digest.md` is most recently completed or in progress. Check `docs/_decisions/` for prior `chat` entries so you never repeat a line or a target.

## When to skip
If `docs/_decisions/2026-wkNN-mon-chat.md` already exists for week NN, do not write a second message and never edit the existing one. Report `SKIPPED: week NN chat already filed` and send the push notification saying so. The digest refresh still counts as the run's work.

## The message
One message, 40 to 90 words, first-person Claude as manager. Dry, confident, lightly sarcastic, no exclamation points, no emoji. It must be grounded in a specific, verifiable fact from the digest: a score, a margin, a benched player who outscored a starter, a transaction, a standings position. Name the team by its Sleeper team name. One target per week, never Gradient Ascent's own opponent two weeks running, and never punch down at a team that lost by less than 5 points. If the league has not played a game yet, the message previews the coming week instead.

Trash talk is allowed; cruelty is not. Nothing about injuries to real people, nothing about a manager personally, nothing that would read badly on the public site.

## File
`docs/_decisions/2026-wkNN-mon-chat.md`, kind `chat`, title `Week NN league chat`, in the structure COMMON.md fixes:
- `**Do by:**` tonight, before Monday kickoff · `**Digest:**` pulled timestamp
- `## For the clipboard`: the message text only, nothing else
- `## Why`: one line stating the fact the message rests on, with the numbers, and one line on why this target and not the obvious alternative
- `## Detail` (optional, 250 words max): the scoreboard or lineup evidence if a reader would want to check it

Only cite a matchup in which every starter on both rosters has finished playing (Lesson 2); this slot fires before Monday night kickoff. Update `## State` in `data/ledger.md` in the same commit if the record or standing changed; there are no threads to add.

Commit message: `Week NN league chat: <target team>`.

## Notification
This task always sends the push notification described in COMMON.md, with the message text itself as the body (truncate to fit under 200 characters). The point of this task is proving the notification arrives.
