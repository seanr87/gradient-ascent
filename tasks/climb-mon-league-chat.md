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
`docs/_decisions/2026-wkNN-mon-chat.md`, kind `chat`, title `Week NN league chat`. Sections:
- metadata line: decision time (ET) and digest pulled timestamp
- `## The fact` (the data point the message rests on, with the numbers)
- `## The message` (the message, as prose)
- `## For the clipboard` (the message text only, nothing else)

Commit message: `Week NN league chat: <target team>`.

## Notification
This task always sends the push notification described in COMMON.md, with the message text itself as the body (truncate to fit under 200 characters). The point of this task is proving the notification arrives.
