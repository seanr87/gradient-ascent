# GRADIENT ASCENT — SCHEDULED TASK REGISTRY
*Source of truth for every scheduled task. Last revised 2026-09-23.*

## How it works
- All tasks are **Claude Code cloud routines**, managed at https://claude.ai/code/routines. They run in Anthropic's cloud on a cron, each with its own fresh checkout of this repo. Nothing depends on Sean's machine being awake or the desktop app being open.
- Each routine's prompt is a short bootstrap: check out `master`, read `tasks/COMMON.md` and its own `tasks/<task-id>.md`, and follow them. **The instructions in `tasks/` are the versioned source.** Editing a task's behavior is a commit to this repo; the live routine picks it up on its next run. The bootstrap prompt itself never needs to change.
- Every routine pulls fresh Sleeper data itself (`scripts/pull_sleeper.py`, no credentials), commits the digest, writes its output to `docs/_decisions/` (or `docs/_posts/` for the column, `docs/_notes/` for notes, `data/ledger.md` for the process review), pushes to `master`, and sends Sean a push notification. GitHub Pages publishes each decision at https://seanr87.github.io/gradient-ascent/decisions/ within about a minute.
- Routines run in the `gradient-ascent` cloud environment (`env_0125ZmYW1E8cAbQ65veHhrZM`), whose network access is Custom with `api.sleeper.app` allowed on top of the default package-manager list, with the built-in tools (Bash, Read, Write, Edit, Glob, Grep, WebSearch, WebFetch, PushNotification). They can push because the Claude GitHub App is installed on the repo (https://github.com/apps/claude/installations/select_target); the claude.ai GitHub connector alone gives read only.
- **Every routine is now agent-owned** (`created_via: meta_mcp`), so the process review can edit any cron, enable or disable any routine, and create new ones. The routines created on 2026-09-23 carry no MCP connectors (the creating session could not attach any), so their sessions have the built-in tools only; see the constraint below.

## Cadence
| # | Task ID | Routine ID | When (ET) | Output |
|---|---------|------------|-----------|--------|
| 0 | `climb-tue-process-review` | `trig_01P3h3hypwwkUj5FDEaKWBHm` | **Tue 6:00 AM** | **No decision file.** Grades last week into `data/ledger.md`, audits data, handoff, execution and schedule, makes at most 2 guarded changes |
| 1 | `climb-tue-weekly-column` | `trig_01NP2S2aeEM1GwgzM8y4Wy88` | Tue 7:30 AM | `docs/_posts/YYYY-MM-DD-week-NN.md`. Skips itself until a week has been played. Reads its grades from the ledger |
| 2 | `climb-tue-waiver-claims` | `trig_01QKizipo66S7hwyTDEfDEo5` | **Tue 6:00 PM** | `docs/_decisions/2026-wkNN-tue-waivers.md`. Waivers process Wed ~3:00 AM (see Waiver timing) |
| 2b | `climb-tue-waiver-claims` (9:30 PM re-report) | `trig_0184wwSMn3B4bS7FWA3bGViJ` | Tue 9:30 PM | **No file.** The task's "Run once a week" check makes it find the 6 PM file, re-report its clipboard, and exit |
| 3 | `climb-tue-waiver-check` | `trig_01MvL5QMr7wPCL2RTfSqizRj` | Tue 10:30 PM | **No file.** Verifies the claims are actually filed in Sleeper. Silent when they are |
| 4 | `climb-wed-post-waiver-review` | `trig_019MBqLRvMRv7mxARWKR9N1H` | Wed 12:00 PM | `docs/_decisions/2026-wkNN-wed-review.md` |
| 5 | `climb-thu-trade-scan` | `trig_01NYdAjMEw3yt65PboXZ69eJ` | Thu 8:00 AM | `docs/_decisions/2026-wkNN-thu-trades.md` |
| 6 | `climb-thu-tnf-check` | `trig_01Y1HL1MH8UCR7zoxegPRh2y` | Thu 5:00 PM | `docs/_decisions/2026-wkNN-thu-tnf.md` |
| 7 | `climb-sun-final-lineup` | `trig_01PGq4ypJNjDGe89MUT8zk9h` | Sun 9:00 AM | `docs/_decisions/2026-wkNN-sun-lineup.md` |
| 8 | `climb-mon-league-chat` | `trig_011asoLjgydikQJHmhrrdN9V` | Mon 8:00 PM | `docs/_decisions/2026-wkNN-mon-chat.md`. Low stakes; proves the whole pipeline weekly |
| 9 | `climb-note` ×10 | see table below | scattered | `docs/_notes/YYYY-MM-DD-HHMM.md`. One line for the site's Notes page; also the data refresh |

Crons are stored with `CRON_TZ=America/New_York`, so they hold their ET times across the November DST change. The scheduler adds a few minutes of jitter.

### Superseded UI-created routines — Sean must disable these (not delete)
Created through the web UI, so no agent can edit or disable them. Each has an agent-owned replacement above with the same cron and the same bootstrap prompt. Until Sean disables them at https://claude.ai/code/routines, both fire; every decision task has a "Run once a week" guard so the second run finds the file, re-reports it, and exits without a notification.

| Old routine ID | Task | When (ET) | Replaced by |
|---|---|---|---|
| `trig_01SHaEx1ATL9aDyE6XhFifTt` | `climb-tue-weekly-column` | Tue 7:30 AM | `trig_01NP2S2aeEM1GwgzM8y4Wy88` |
| `trig_01CRESt3SMxaCi7UDBrQH7Uh` | `climb-tue-waiver-claims` (old 9:30 PM) | Tue 9:30 PM | `trig_0184wwSMn3B4bS7FWA3bGViJ` |
| `trig_0189zh2wC5LqTmQp38hrmVrn` | `climb-wed-post-waiver-review` | Wed 12:00 PM | `trig_019MBqLRvMRv7mxARWKR9N1H` |
| `trig_01TAsV5kXxdEprxHrxBiunGt` | `climb-thu-trade-scan` | Thu 8:00 AM | `trig_01NYdAjMEw3yt65PboXZ69eJ` |
| `trig_01XyQV9es4MXDvas42VTEFGj` | `climb-thu-tnf-check` | Thu 5:00 PM | `trig_01Y1HL1MH8UCR7zoxegPRh2y` |
| `trig_01CarVocM38YYE8nT6NtiTDa` | `climb-sun-final-lineup` | Sun 9:00 AM | `trig_01PGq4ypJNjDGe89MUT8zk9h` |
| `trig_01MQTa67SoWFDnjWPhyG2jFP` | `climb-mon-league-chat` | Mon 8:00 PM | `trig_011asoLjgydikQJHmhrrdN9V` |

Already disabled: the old daily `climb-note` (`trig_01Ed6DEgsJdd1c6mZYaDwZt1`, UI-created, `enabled: false` since 2026-09-20).

**Currently pending on Sean:** disable the seven routines in the table above. One-time.

### Waiver timing — being settled by measurement
The registry measured **3:14 AM ET** from the Week 1 run: the `status_updated` timestamp shared by all nine claims (`2026-09-16 07:14 UTC`), read from `/league/<id>/transactions/1`. Sleeper's transaction screen showed **~3:05 AM ET** for the Week 3 run (`2026-wk03-tue-trades`). Settings agree in shape (`waiver_day_of_week: 2`, `waiver_clear_days: 2`) but give no hour. The process review measures the time from each week's claim timestamps and, once two weeks agree to the minute, corrects every file that states one in a single commit. Until then every waiver `Do by` says **3:00 AM ET**.

The claims routine originally fired **Tue 9:30 PM**, leaving about five and a half hours to the run, essentially all of it overnight. Two weeks running the file was correct, on time, and never executed. The slot moved to **Tue 6:00 PM** to put the decision in front of Sean while he is awake, and `climb-tue-waiver-check` was added at **Tue 10:30 PM** as a last call with about four and a half hours left. The check is silent on success by design — an alarm that fires every week stops being an alarm. It is the model for any reminder routine the process review adds.

### The note slots
Ten a week at deliberately irregular hours, replacing the single daily noon run. Sean asked for the times not to be predictable and for a few more of them. All agent-owned.

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

### Constraint: who can edit which routine
A routine created through the web UI or HTTP API (`created_via: http_api`) cannot be edited by an agent: `update_trigger` refuses with *"Agents can only update routines they created."* As of 2026-09-23 every live routine is agent-owned, so the process review can edit crons, enable or disable routines, and create new ones, using the Claude Code Remote tools (`list_triggers`, `create_trigger`, `update_trigger`).

One gap remains. Routines created from a Claude Code session carry only the MCP connectors that session could pass through, and the 2026-09-23 session could pass none, so the routines it created (0, 1, 2b, 4–8) run with the built-in tools only. The routines created on 2026-09-20 (2, 3, and the ten note slots) do carry the Claude Code Remote connector. In practice: the process review (routine 0) can edit `tasks/` and this registry in every run, but can edit routines only when its session holds the Claude Code Remote tools. When it does not, it does the task-side half of a schedule change, logs the routine half here as **PENDING-TOOLS** with the exact cron and routine ID, and says so in its notification. If Sean re-creates routine 0 from the claude.ai routines UI with the Claude Code Remote connector attached, that gap closes (the routine itself then becomes UI-created and uneditable by agents, which is acceptable for the reviewer).

## Who changes what
- `tasks/`, this registry, and the routines' schedules and enabled state are changed by the process review only, at most two changes a week, each one commit, each with a kill condition logged in `data/ledger.md` under `## Process changes` and reverted by the next review if met. `tasks/LOCKED.md` lists what it may never alter.
- Nothing is deleted. Routines are disabled, files are emptied to a pointer, and git history is the archive.
- Sean's only recurring job is executing clipboard lines. His one-time job right now is the disable list above.

## Data the tasks depend on
- `scripts/pull_sleeper.py` writes `data/digest.md` and `data/digest.json`: rosters, standings with waiver position, this and last week's scores, transactions, trending adds and drops. Every routine runs it at the start of its run.
- `scripts/update_roster.py` regenerates the roster table in `OPS-MANUAL.md` and `docs/_data/roster.yml` for the site, with each player's acquisition (draft round and pick, or the week and transaction type) from Sleeper's draft and transaction history, and reports any rostered player missing a line in `docs/_data/notes.yml`.
- `.github/workflows/sleeper-pull.yml` runs about 45 minutes before every routine slot (UTC crons on odd minutes; they drift an hour earlier ET after the November DST change). It is the fallback when the cloud egress proxy blocks `api.sleeper.app`, which it did on the first test run.

## Bootstrap prompt (what the live routines contain)
> You are a scheduled Claude Code cloud routine with a checkout of the GitHub repo seanr87/gradient-ascent (default branch master). Run `git checkout master` and `git pull --rebase origin master`. Then read `tasks/COMMON.md` and `tasks/<task-id>.md` in that repo and carry them out exactly. They are the full, versioned instruction set for this run. If either file is missing, stop, report that, and send a push notification saying the run failed. The user is not present: do not ask questions, make reasonable choices and note them in the decision file.

Each replacement created on 2026-09-23 carries its predecessor's exact prompt (the same bootstrap with a one-clause summary of the task), so behaviour is unchanged.

## Checking on a run
From a Claude Code session: `/schedule list` shows the routines; the `RemoteTrigger` tool's `list_runs` and `get_run_log` show what a run did, and the Claude Code Remote `list_triggers` tool shows each routine's `last_run`. On the web, each routine page at https://claude.ai/code/routines lists its runs. A decision that is not on `origin/master` did not happen, whatever the run log says.

## Retired: desktop scheduled tasks
Six Claude Code desktop scheduled tasks (`climb-*`, in the Claude desktop app on Sean's machine) ran this cadence from 2026-09-08 to 2026-09-14. They are **disabled, not deleted**, so they can be re-enabled as a fallback. Do not run both systems at once; decisions would be committed twice.

## Change log
- 2026-09-07 — Initial registry: five decision tasks as claude.ai routines with one-paragraph prompts fetching raw digest URLs; weekly column planned.
- 2026-09-08 — Six desktop scheduled tasks added that commit directly. Instructions moved into `tasks/`. The five claude.ai routines were never disabled and kept running blind in parallel; their week 1 waiver output is what Sean executed on Sep 9, while the desktop review committed NO ACTION.
- 2026-09-14 — Consolidated on cloud routines. The five routines rewritten to the bootstrap prompt above with a repo checkout; column and league-chat routines created; `tasks/COMMON.md` adapted for the cloud (pulls Sleeper data directly, push notifications). Desktop tasks disabled.
- 2026-09-20 — Waiver claims moved to Tue 6:00 PM (`trig_01QKizipo66S7hwyTDEfDEo5`, agent-owned); `climb-tue-waiver-check` added at Tue 10:30 PM (`trig_01MvL5QMr7wPCL2RTfSqizRj`); daily note replaced by ten scattered slots; old daily note disabled by Sean.
- 2026-09-23 — Process review added at Tue 6:00 AM (`trig_01P3h3hypwwkUj5FDEaKWBHm`). Every UI-created routine re-created as agent-owned with the same cron and prompt: column `trig_01NP2S2aeEM1GwgzM8y4Wy88`, 9:30 PM waiver re-report `trig_0184wwSMn3B4bS7FWA3bGViJ`, Wed review `trig_019MBqLRvMRv7mxARWKR9N1H`, Thu trades `trig_01NYdAjMEw3yt65PboXZ69eJ`, Thu TNF `trig_01Y1HL1MH8UCR7zoxegPRh2y`, Sun lineup `trig_01PGq4ypJNjDGe89MUT8zk9h`, Mon chat `trig_011asoLjgydikQJHmhrrdN9V`. Seven old routines pending disable by Sean. Every decision task guarded against double-firing. Kill conditions in `data/ledger.md`.
