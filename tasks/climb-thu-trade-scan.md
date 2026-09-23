# Task: Thursday trade scan (Thu 8:00 AM ET)

Read `tasks/COMMON.md` first and follow it. This task produces the weekly **trade scan**.

## Run once a week — check this first
**If `docs/_decisions/2026-wkNN-thu-trades.md` already exists for this week, stop.** Do not write a second one and never edit the first. Give the standard three-line report from the existing file (its `**Do by:**` line, its `## For the clipboard` section in a code fence, its page link), send no push notification, and stop. Refreshing and committing the digest per COMMON is fine; writing a second scan is not. Two routines may fire this task until the old UI-created one is disabled (see `SCHEDULED-TASKS.md`); both firing must be harmless.

## Data
COMMON.md already refreshed the digest at the start of this run. Use `all_rosters` and `standings` in `data/digest.json` for every team's roster, record, and points.

## The scan
Look for trades that make Gradient Ascent better under the manual's scoring edges. Look for partners with a positional surplus where I have a gap, or a need I can fill from my depth. Read each partner's record and roster shape: a losing team values now, a winning team values depth. Check prior trade scans in `docs/_decisions/` so you do not re-pitch a rejected deal without a changed rationale.

Produce at most two proposals, zero if nothing clears the bar. A lopsided proposal gets declined and wastes Sean's time, so weigh acceptance odds. For each proposal:
- Counterpart team name and manager display name from the digest
- `GIVE: [players]` and `GET: [players]`, exact
- `PITCH:` the exact message Sean pastes into league chat or a DM, in my voice, under 80 words, no exclamation points
- Under `## Why`, one line on why it helps me and one on why they should accept, both data-backed and honest

For each player on a `GET:` line, write his note in `docs/_data/notes.yml` in this commit (COMMON.md, Roster notes); if the trade is declined the line is harmless, and if it is accepted the roster page is already right.

If nothing clears the bar, the clipboard is `NO ACTION` and `## Why` says in one line what would change that.

## File
`docs/_decisions/2026-wkNN-thu-trades.md`, kind `trades`, title `Week NN trade scan`, in the structure COMMON.md fixes:
- `**Do by:**` when the pitch should be sent (usually today, so the counterpart can answer before Sunday) · `**Digest:**` pulled timestamp
- `## For the clipboard`: per proposal, the counterpart, the GIVE/GET lines and the PITCH text, in the order to send them and with any "only if proposal 1 is declined" condition stated; or `NO ACTION`
- `## Why`: two lines per proposal (helps me; why they accept), then at most 3 passed-on ideas, one line each
- `## Detail` (optional, 250 words max): positional shape of the league if it drove the pick, sources as one line of links

Update `## State` and `## Open threads` in `data/ledger.md` in the same commit: one thread per proposal sent, with the fallback and the condition that retires it.

Commit message: `Week NN trade scan: <summary>`.
