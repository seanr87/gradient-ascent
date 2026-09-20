# GRADIENT ASCENT — SCHEDULED TASK REGISTRY
*Source of truth for every scheduled task. Last revised 2026-09-14.*

## How it works
- All eight tasks are **Claude Code cloud routines**, managed at https://claude.ai/code/routines. They run in Anthropic's cloud on a cron, each with its own fresh checkout of this repo. Nothing depends on Sean's machine being awake or the desktop app being open.
- Each routine's prompt is a short bootstrap: check out `master`, read `tasks/COMMON.md` and its own `tasks/<task-id>.md`, and follow them. **The instructions in `tasks/` are the versioned source.** Editing a task's behavior is a commit to this repo; the live routine picks it up on its next run. The bootstrap prompt itself never needs to change.
- Every routine pulls fresh Sleeper data itself (`scripts/pull_sleeper.py`, no credentials), commits the digest, writes its output to `docs/_decisions/` (or `docs/_posts/` for the column), pushes to `master`, and sends Sean a push notification with the clipboard lines. GitHub Pages publishes each decision at https://seanr87.github.io/gradient-ascent/decisions/ within about a minute.
- Routines run as `claude-opus-5` with tools Bash, Read, Write, Edit, Glob, Grep, WebSearch, WebFetch, PushNotification, in the `gradient-ascent` cloud environment (`env_0125ZmYW1E8cAbQ65veHhrZM`), whose network access is Custom with `api.sleeper.app` allowed on top of the default package-manager list. They can push because the Claude GitHub App is installed on the repo (https://github.com/apps/claude/installations/select_target); the claude.ai GitHub connector alone gives read only.

## Cadence
| # | Task ID | Routine ID | When (ET) | Output |
|---|---------|------------|-----------|--------|
| 1 | `climb-tue-weekly-column` | `trig_01SHaEx1ATL9aDyE6XhFifTt` | Tue 7:30 AM | `docs/_posts/YYYY-MM-DD-week-NN.md`. Skips itself until a week has been played |
| 2 | `climb-tue-waiver-claims` | `trig_01QKizipo66S7hwyTDEfDEo5` | **Tue 6:00 PM** | `docs/_decisions/2026-wkNN-tue-waivers.md`. Waivers process Wed 3:14 AM |
| 2b | `climb-tue-waiver-claims` (old duplicate) | `trig_01CRESt3SMxaCi7UDBrQH7Uh` | Tue 9:30 PM | **No-ops.** The task's "Run once a week" check makes it find the 6 PM file and exit |
| 3 | `climb-tue-waiver-check` | `trig_01MvL5QMr7wPCL2RTfSqizRj` | Tue 10:30 PM | **No file.** Verifies the claims are actually filed in Sleeper. Silent when they are |
| 4 | `climb-wed-post-waiver-review` | `trig_0189zh2wC5LqTmQp38hrmVrn` | Wed 12:00 PM | `docs/_decisions/2026-wkNN-wed-review.md` |
| 5 | `climb-thu-trade-scan` | `trig_01TAsV5kXxdEprxHrxBiunGt` | Thu 8:00 AM | `docs/_decisions/2026-wkNN-thu-trades.md` |
| 6 | `climb-thu-tnf-check` | `trig_01XyQV9es4MXDvas42VTEFGj` | Thu 5:00 PM | `docs/_decisions/2026-wkNN-thu-tnf.md` |
| 7 | `climb-sun-final-lineup` | `trig_01CarVocM38YYE8nT6NtiTDa` | Sun 9:00 AM | `docs/_decisions/2026-wkNN-sun-lineup.md` |
| 8 | `climb-mon-league-chat` | `trig_01MQTa67SoWFDnjWPhyG2jFP` | Mon 8:00 PM | `docs/_decisions/2026-wkNN-mon-chat.md`. Low stakes; proves the whole pipeline weekly |
| 9 | `climb-note` ×10 | see table below | scattered | `docs/_notes/YYYY-MM-DD-HHMM.md`. One line for the site's Notes page; also the data refresh |

Crons are stored with `CRON_TZ=America/New_York`, so they hold their ET times across the November DST change. The scheduler adds a few minutes of jitter.

### Waiver timing — measured, not assumed
Waivers process **Wednesday 3:14 AM ET**. That is not from league settings; it is the `status_updated` timestamp shared by all nine claims in the Week 1 run (`2026-09-16 07:14 UTC`), read from `/league/<id>/transactions/1`. Settings agree in shape (`waiver_day_of_week: 2`, `waiver_clear_days: 2`) but give no hour.

The claims routine originally fired **Tue 9:30 PM**, leaving 5h36m to the run, essentially all of it overnight. Two weeks running the file was correct, on time, and never executed. The slot moved to **Tue 6:00 PM** to put the decision in front of Sean while he is awake, and `climb-tue-waiver-check` was added at **Tue 10:30 PM** as a last call with about four and a half hours left. The check is silent on success by design — an alarm that fires every week stops being an alarm.

### The note slots
Ten a week at deliberately irregular hours, replacing the single daily noon run. Sean asked for the times not to be predictable and for a few more of them.

| Routine ID | When (ET) |
|---|---|
| `trig_01JysbKd4yNFPadzQyYs5cus` | Mon 8:12 AM |
| `trig_01Rbh16rV7GGtnXbNj3DAW6Z` | Tue 11:07 AM |
| `trig_01K14YAWpCadEv4Xb33zovSQ` | Tue 2:33 PM |
| `trig_01J6B316LXhQzTYTY9iuNRUe` | Wed 9:23 AM |
| `trig_01K4XM6r2G82r7vFgrb8toQs` | Thu 1:36 PM |
| `trig_01U5gznM1Xa4SC2XXskZ7VaL` | Thu 7:52 PM |
| `trig_012e2YuQqNw56YknbUtAUq4M` | Fri 10:19 AM |
| `trig_01Su64LVwDWADmvhKQ2notdD` | Sat 12:28 PM |
| `trig_01TxD2AU5sWk3tjkgSY4XAFi` | Sat 4:47 PM |
| `trig_01XcGx7hFbKeZ1ygN7iD5kC2` | Sun 11:11 AM |

The old daily routine `trig_01Ed6DEgsJdd1c6mZYaDwZt1` must be **disabled by Sean** — see the constraint below. Until it is, there are seventeen notes a week, not ten.

### Constraint: who can edit which routine
A routine created through the web UI or HTTP API (`created_via: http_api`) **cannot be edited by an agent**, including by me. `update_trigger` refuses with *"Agents can only update routines they created."* Routines 1, 2, and 4 through 8, plus the old daily note, are all in that category: I can read them and I cannot change their cron, their prompt, or their enabled state.

So a schedule change I decide on splits in two. The part I can do — creating a new routine, editing the `tasks/` instructions it reads — I do. The part only Sean can do is changing an existing routine at https://claude.ai/code/routines. Any such change is recorded here as **PENDING** until it is confirmed live, and a task file whose header states a time the live cron does not match is a discrepancy to flag, not to trust.

Where a routine can be worked around instead, it is — a change that needs nothing from Sean is worth more than a correct one waiting on him. The waiver move was done that way: rather than wait for the 9:30 PM cron to be edited, a new 6:00 PM routine (`trig_01QKizipo66S7hwyTDEfDEo5`, agent-owned and editable) was created, and the task file gained a "Run once a week" guard so the old routine finds the file written and exits. Both fire; only one decides.

**Currently pending on Sean: nothing.**

*Cleared 2026-09-20:* the old daily `climb-note` (`trig_01Ed6DEgsJdd1c6mZYaDwZt1`) is **disabled**, confirmed by reading it back — `enabled: false`, updated 14:34 UTC. The ten scattered slots are the only note routines now firing. It could not be neutralised from the task side, because a blanket "skip if a note exists today" rule would also have killed the deliberate second note on Tuesday, Thursday and Saturday.

*Tidy-up, optional:* routine 2b can be deleted once convenient. It costs one wasted run a week and nothing else.

## Data the tasks depend on
- `scripts/pull_sleeper.py` writes `data/digest.md` and `data/digest.json`: rosters, standings with waiver position, this and last week's scores, transactions, trending adds and drops. Every routine runs it at the start of its run.
- `scripts/update_roster.py` regenerates the roster table in `OPS-MANUAL.md` and `docs/_data/roster.yml` for the site, with each player's acquisition (draft round and pick, or the week and transaction type) from Sleeper's draft and transaction history, and reports any rostered player missing a line in `docs/_data/notes.yml`.
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
