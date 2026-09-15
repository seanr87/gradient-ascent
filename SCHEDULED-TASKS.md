# GRADIENT ASCENT — SCHEDULED TASK REGISTRY
*Source of truth for every scheduled task. Last revised 2026-09-14.*

## How it works
- All seven tasks are **Claude Code cloud routines**, managed at https://claude.ai/code/routines. They run in Anthropic's cloud on a cron, each with its own fresh checkout of this repo. Nothing depends on Sean's machine being awake or the desktop app being open.
- Each routine's prompt is a short bootstrap: check out `master`, read `tasks/COMMON.md` and its own `tasks/<task-id>.md`, and follow them. **The instructions in `tasks/` are the versioned source.** Editing a task's behavior is a commit to this repo; the live routine picks it up on its next run. The bootstrap prompt itself never needs to change.
- Every routine pulls fresh Sleeper data itself (`scripts/pull_sleeper.py`, no credentials), commits the digest, writes its output to `docs/_decisions/` (or `docs/_posts/` for the column), pushes to `master`, and sends Sean a push notification with the clipboard lines. GitHub Pages publishes each decision at https://seanr87.github.io/gradient-ascent/decisions/ within about a minute.
- Routines run as `claude-opus-5` with tools Bash, Read, Write, Edit, Glob, Grep, WebSearch, WebFetch, PushNotification, in the `gradient-ascent` cloud environment (`env_0125ZmYW1E8cAbQ65veHhrZM`), whose network access is Custom with `api.sleeper.app` allowed on top of the default package-manager list. They can push because the Claude GitHub App is installed on the repo (https://github.com/apps/claude/installations/select_target); the claude.ai GitHub connector alone gives read only.

## Cadence
| # | Task ID | Routine ID | When (ET) | Output |
|---|---------|------------|-----------|--------|
| 1 | `climb-tue-weekly-column` | `trig_01SHaEx1ATL9aDyE6XhFifTt` | Tue 7:30 AM | `docs/_posts/YYYY-MM-DD-week-NN.md`. Skips itself until a week has been played |
| 2 | `climb-tue-waiver-claims` | `trig_01CRESt3SMxaCi7UDBrQH7Uh` | Tue 9:30 PM | `docs/_decisions/2026-wkNN-tue-waivers.md`. Waivers clear Wed 3:00 AM |
| 3 | `climb-wed-post-waiver-review` | `trig_0189zh2wC5LqTmQp38hrmVrn` | Wed 12:00 PM | `docs/_decisions/2026-wkNN-wed-review.md` |
| 4 | `climb-thu-trade-scan` | `trig_01TAsV5kXxdEprxHrxBiunGt` | Thu 8:00 AM | `docs/_decisions/2026-wkNN-thu-trades.md` |
| 5 | `climb-thu-tnf-check` | `trig_01XyQV9es4MXDvas42VTEFGj` | Thu 5:00 PM | `docs/_decisions/2026-wkNN-thu-tnf.md` |
| 6 | `climb-sun-final-lineup` | `trig_01CarVocM38YYE8nT6NtiTDa` | Sun 9:00 AM | `docs/_decisions/2026-wkNN-sun-lineup.md` |
| 7 | `climb-mon-league-chat` | `trig_01MQTa67SoWFDnjWPhyG2jFP` | Mon 8:00 PM | `docs/_decisions/2026-wkNN-mon-chat.md`. Low stakes; proves the whole pipeline weekly |
| 8 | `climb-note` | `trig_01Ed6DEgsJdd1c6mZYaDwZt1` | Daily 12:00 PM | `docs/_notes/YYYY-MM-DD-HHMM.md`. One line for the site's Notes page; also a daily digest refresh |

Crons are stored with `CRON_TZ=America/New_York`, so they hold their ET times across the November DST change. The scheduler adds a few minutes of jitter.

## Data the tasks depend on
- `scripts/pull_sleeper.py` writes `data/digest.md` and `data/digest.json`: rosters, standings with waiver position, this and last week's scores, transactions, trending adds and drops. Every routine runs it at the start of its run.
- `scripts/update_roster.py` regenerates the roster table in `OPS-MANUAL.md` and `docs/_data/roster.yml` for the site.
- `.github/workflows/sleeper-pull.yml` runs about 45 minutes before every routine slot (UTC crons on odd minutes; they drift an hour earlier ET after the November DST change). It is the fallback when the cloud egress proxy blocks `api.sleeper.app`, which it did on the first test run: a routine can also dispatch it on demand through the GitHub MCP tools.

## Bootstrap prompt (what the live routines contain)
> You are a scheduled Claude Code cloud routine with a checkout of the GitHub repo seanr87/gradient-ascent (default branch master). Run `git checkout master` and `git pull --rebase origin master`. Then read `tasks/COMMON.md` and `tasks/<task-id>.md` in that repo and carry them out exactly. They are the full, versioned instruction set for this run. If either file is missing, stop, report that, and send a push notification saying the run failed. The user is not present: do not ask questions, make reasonable choices and note them in the decision file.

## Checking on a run
From a Claude Code session: `/schedule list` shows the routines; the `RemoteTrigger` tool's `list_runs` and `get_run_log` show what a run did. On the web, each routine page at https://claude.ai/code/routines lists its runs. A decision that is not on `origin/master` did not happen, whatever the run log says.

## Retired: desktop scheduled tasks
Six Claude Code desktop scheduled tasks (`climb-*`, in the Claude desktop app on Sean's machine) ran this cadence from 2026-09-08 to 2026-09-14. They are **disabled, not deleted**, so they can be re-enabled as a fallback. Do not run both systems at once; decisions would be committed twice.

## Change log
- 2026-09-07 — Initial registry: five decision tasks as claude.ai routines with one-paragraph prompts fetching raw digest URLs; weekly column planned.
- 2026-09-08 — Six desktop scheduled tasks added that commit directly. Instructions moved into `tasks/`. The five claude.ai routines were never disabled and kept running blind in parallel; their week 1 waiver output is what Sean executed on Sep 9, while the desktop review committed NO ACTION.
- 2026-09-14 — Consolidated on cloud routines. The five routines rewritten to the bootstrap prompt above with a repo checkout; column and league-chat routines created; `tasks/COMMON.md` adapted for the cloud (pulls Sleeper data directly, push notifications). Desktop tasks disabled.
