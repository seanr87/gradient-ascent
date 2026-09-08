# Task: Thursday trade scan (Thu 8:00 AM ET)

Read `tasks/COMMON.md` first and follow it. This task produces the weekly **trade scan**.

## Data
Freshness limit: 12 hours. Refresh per COMMON.md if older. Use `all_rosters` and `standings` in `data/digest.json` for every team's roster, record, and points.

## The scan
Look for trades that make Gradient Ascent better under the manual's scoring edges. Look for partners with a positional surplus where I have a gap, or a need I can fill from my depth. Read each partner's record and roster shape: a losing team values now, a winning team values depth. Check prior trade scans in `docs/_decisions/` so you do not re-pitch a rejected deal without a changed rationale.

Produce at most two proposals, zero if nothing clears the bar. A lopsided proposal gets declined and wastes Sean's time, so weigh acceptance odds. For each proposal:
- Counterpart team name and manager display name from the digest
- `GIVE: [players]` and `GET: [players]`, exact
- Why it helps me (two or three sentences, data-backed)
- Why they should accept (one or two sentences, honest)
- `PITCH:` the exact message Sean pastes into league chat or a DM, in my voice, under 80 words, no exclamation points

If nothing clears the bar, write `NO PROPOSALS` with one paragraph on why and what would change that.

## File
`docs/_decisions/2026-wkNN-thu-trades.md`, kind `trades`, title `Week NN trade scan`. Sections:
- metadata line: decision time (ET) and digest pulled timestamp
- `## Proposals` (numbered, or `NO PROPOSALS`)
- `## Passed on` (two or three rejected ideas, one line each)
- `## For the clipboard` (per proposal: counterpart, GIVE/GET lines, PITCH text; or `NO ACTION`)

Commit message: `Week NN trade scan: <summary>`.
