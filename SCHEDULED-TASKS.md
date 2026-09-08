# GRADIENT ASCENT — SCHEDULED TASK REGISTRY
*Source of truth for every scheduled task. Last revised 2026-09-08.*

## How it works
- All six tasks are **Claude desktop scheduled tasks** (Claude Code, in the Claude desktop app on Sean's machine). Task IDs match the filenames in `tasks/`.
- Each live task's prompt is a short bootstrap: open the local clone, pull `master`, read `tasks/COMMON.md` and its own `tasks/<task-id>.md`, and follow them. **The instructions in `tasks/` are the versioned source.** Editing a task's behavior is a commit to this repo; the live task picks it up on its next run. The bootstrap prompt itself only changes if the clone moves.
- Every task refreshes the digest when stale (`gh workflow run sleeper-pull.yml`), writes its output to `docs/_decisions/` (or `docs/_posts/` for the column), and pushes to `master`. GitHub Pages publishes each decision at https://seanr87.github.io/gradient-ascent/decisions/ within about a minute. Sean pastes from the `## For the clipboard` section.
- Tasks run only while the Claude desktop app is open. A task that comes due while the app is closed runs on next launch. If the machine is asleep, treat the run as missed until the app is back; the task will still produce a correct file, just late. Keep the machine awake and the app open at the times below, or move to cloud routines (see below).

## Cadence
| # | Task ID | When (ET) | Output | Notes |
|---|---------|-----------|--------|-------|
| 1 | `climb-tue-weekly-column` | Tue 7:30 AM | `docs/_posts/YYYY-MM-DD-week-NN.md` | Skips itself until a week has been played. Superlatives from real scores |
| 2 | `climb-tue-waiver-claims` | Tue 9:30 PM | `docs/_decisions/2026-wkNN-tue-waivers.md` | Runs 30 min after the Tue 9:00 PM digest pull. Waivers clear Wed 3:00 AM |
| 3 | `climb-wed-post-waiver-review` | Wed 12:00 PM | `docs/_decisions/2026-wkNN-wed-review.md` | Always refreshes the digest first |
| 4 | `climb-thu-trade-scan` | Thu 8:00 AM | `docs/_decisions/2026-wkNN-thu-trades.md` | 0 to 2 proposals with paste-ready pitches |
| 5 | `climb-thu-tnf-check` | Thu 5:00 PM | `docs/_decisions/2026-wkNN-thu-tnf.md` | Refreshes digest, checks inactives via web search |
| 6 | `climb-sun-final-lineup` | Sun 9:00 AM | `docs/_decisions/2026-wkNN-sun-lineup.md` | Runs 60 min after the Sun 8:00 AM digest pull. Web search for inactives |

The scheduler adds a few minutes of jitter to each time.

## Data the tasks depend on
- `.github/workflows/sleeper-pull.yml` runs Tue 9:00 PM ET and Sun 8:00 AM ET (cron is UTC; after the November DST change these land an hour earlier unless the cron is moved) and on demand.
- `scripts/pull_sleeper.py` writes `data/digest.md` and `data/digest.json`: rosters, standings with waiver position, this and last week's scores, transactions, trending adds and drops.
- `scripts/update_roster.py` regenerates the roster table in `OPS-MANUAL.md` and `docs/_data/roster.yml` for the site.

## Bootstrap prompt (what the live tasks contain)
> Work in `C:\Users\soreill5\gradient-ascent`. If that folder does not exist, use `C:\Users\soreill5\sleeper-pipeline`. Run `git checkout master` and `git pull --rebase origin master` (stash first if blocked). Then read `tasks/COMMON.md` and `tasks/<task-id>.md` in that repo and carry them out exactly. They are the full, versioned instruction set for this run.

## Moving to cloud routines (no machine required)
Claude Code cloud routines run these same instructions in Anthropic's cloud on a cron, with their own checkout of the repo, so nothing depends on Sean's laptop being awake. Two prerequisites before switching: install the Claude GitHub App on `seanr87/gradient-ascent` (https://claude.ai/code/onboarding?magic=github-app-setup) so the routine can push, and then create one routine per task with the bootstrap prompt above (minus the local paths). When the routines are live, pause the desktop tasks so decisions are not committed twice.

## Change log
- 2026-09-07 — Initial registry: five decision tasks as Claude Project chat tasks; weekly column as a cloud routine (planned).
- 2026-09-08 — All six tasks live as desktop scheduled tasks that commit directly. Instructions moved into `tasks/`. Decisions publish to the site under `/decisions/`. Weekly column added at Tue 7:30 AM.
