# Task: Weekly process review (Tue 6:00 AM ET)

Read `tasks/COMMON.md` first and follow it, then read `tasks/LOCKED.md` in full. This task audits the whole pipeline for the week just finished, stage by stage (data → decision → handoff → execution → schedule), and fixes what it finds on its own, within the guardrails below. It fires after Monday night is final and before the 7:30 AM column, so any fix is live for Tuesday's 6:00 PM waiver run.

It writes **no decision file and no clipboard**. Its output is the ledger, at most two guarded changes, and one push notification.

## Data
COMMON.md already refreshed and committed the digest. Call the week just finished NN (the most recently completed week in `data/digest.md`). Exception to COMMON's setup step 4: read every decision file for week NN, the week's post if one exists, and the whole of `data/ledger.md`. For run history use whichever of these the session has, in this order: the `RemoteTrigger` tool's `list_runs` and `get_run_log`; the Claude Code Remote `list_triggers` tool (each routine's `last_run`); failing both, the commit log (`git log --format='%h %ci %s'`), which shows every run that reached the repo. Say which source you used. For Sleeper timestamps use the league's transaction endpoint, which the digest does not carry in full:

```
https://api.sleeper.app/v1/league/1389359498023436288/transactions/<leg>
```

Check the current leg and the previous one; Sleeper has filed a Wednesday run under the prior leg before. `created` and `status_updated` are millisecond epochs; convert to ET.

## The review, stage by stage

**Data.** For every run that week:
- Did the digest refresh? Compare the `Pulled:` time the decision file cites to the decision time in its front matter.
- Was the Action fallback needed (a `Sleeper digest` commit authored by the workflow rather than the routine, or a decision file saying the proxy blocked the pull)?
- Did any run fail, skip or double-fire? Two commits for one slot, a decision file missing for a slot that should have written one, a `SKIPPED` report, a run with no commit.
- Was a decision made on stale or missing data? A `Pulled:` line more than 30 minutes before the decision time, or a file that says so.

**Decisions.** This is where the ledger's grading lives now.
- Grade every call from week NN's decision files (every clipboard line and every start/bench call) as `Right`, `Wrong (luck)` (the call was sound, the outcome was not), `Wrong (process)` (the call was unsound, or was never executed) or `Unknown` (cannot be known yet; never guessed), with a one-line cause, as rows in `## Scorecard`.
- Rewrite the ledger to the 150-line cap: refresh `## State` and `## Open threads`; keep the last 3 weeks of `## Scorecard` and `## Execution` in full and roll older weeks into one summary line each; re-check every thesis against the week's results and retire any whose kill condition was met.
- Distill: add or update a `## Lessons` entry only with evidence from actual results, citing the week. Merge duplicates. Drop any lesson disproven twice. Never more than 10.

**Handoff.** For every decision file of week NN:
- Was the push notification sent? (Run log if available; otherwise the report in the run's session; otherwise mark unverifiable.)
- Did it lead with the action?
- Was the file within its caps (structure, 400 words excluding the clipboard, Detail 250)?
- How much time was there between the notification and the file's `Do by` deadline, and how much of that was overnight (11 PM to 7 AM ET)?

**Execution.** Compare every clipboard line of week NN to Sleeper's transactions and lineups:
- Record whether it landed, and the **latency**: decision commit time (`git log` on the decision file) to the Sleeper transaction's `created` time. Lineup lines have no timestamp in the public API; record landed or not from the starters at lock and mark latency `n/a`.
- Log when Sean actually executes, by day and hour, on the `Sean acts:` line under `## Execution` (for example `Tue 9–10 PM ×2, Wed 12–1 PM ×1`). Keep a running tally across weeks; it is the input to the schedule stage.
- Log every miss and the slot it came from, in the `## Execution` table.

**Schedule.** Using at least 2 weeks of execution timing (do nothing here until you have them):
- If misses cluster in a slot, move that slot's decision time to a time Sean has actually acted (from the `Sean acts:` tally), or add a reminder routine for it. `climb-tue-waiver-check` is the model: silent on success, alarm on a miss, fires with time left before the deadline.
- Deadlines are fixed by the NFL and Sleeper. Only the decision and reminder times move.
- A slot change is a routine cron edit (or a new routine) plus the matching header in the `tasks/` file plus the registry row, all in one commit.

**Also: the waiver processing time.** Measure it from the week's claim `status_updated` timestamps. The registry says 3:14 AM ET (measured, Week 1 run) and the ledger says about 3:05 (Sleeper's screen), so settle it with data: if two weeks of runs agree to the minute, that is the time; correct every file that states one (`tasks/climb-tue-waiver-claims.md`, `tasks/climb-tue-waiver-check.md`, `tasks/COMMON.md`, `SCHEDULED-TASKS.md`, `OPS-MANUAL.md`, `README.md`, `data/ledger.md`) in one commit, which counts as one of the week's two changes. Until it is settled, every waiver `Do by` says 3:00 AM ET and this task leaves those lines alone.

## What this task may change without asking
Each week it may change `tasks/` files, `SCHEDULED-TASKS.md`, and the agent-owned routines (create one, edit a cron, enable or disable one). Limits:
- **At most 2 changes a week. Each change is one commit** (a routine change plus its task header and registry row is one change). Reverts of last week's changes do not count against the two.
- **`tasks/LOCKED.md`.** Nothing it lists may be altered. If a change you want would, do not make it; write one line under `## Process review` saying what you wanted and why it is locked.
- **Kill condition.** Every change is logged under `## Process changes` in the ledger as `change | date | kill condition | status`. The kill condition is a measurable result that means the change failed (for example "a waiver miss at the new slot within 2 weeks", or "the reminder fires on a week with nothing missing").
- **Revert.** Check every `active` row in `## Process changes` **first, before anything else**. If its kill condition was met, undo it: `git revert` the change's commit (or restore the old cron with `update_trigger`, or re-enable what was disabled), mark the row `reverted <date>: <why>`, and say so in the notification. A change that survives 4 weeks is marked `kept` and its row rolls into one line.
- **Registry.** Every routine change is also logged in the `SCHEDULED-TASKS.md` change log with the routine ID, and the cadence table is updated in the same commit.
- **Nothing is deleted.** Disable routines; never delete them. Never delete a task file; empty it to a pointer if it is retired.
- **Routine tools.** Routine changes use the Claude Code Remote tools (`list_triggers`, `create_trigger`, `update_trigger`). If this session does not hold them (a routine created without connectors runs without them), do the task-side half of the change, log the routine half in the registry as `PENDING-TOOLS` with the exact cron and routine ID, and say so in the notification. It still counts as one change.

## Output
Rewrite `## Process review` in the ledger, at most 12 lines, dated: one line per stage (data, decisions, handoff, execution, schedule), one line per change made or reverted, one line per locked change refused, and the waiver-time measurement. Commit the ledger and any registry edit per COMMON (`Week NN process review: <one-line summary>`); each change is its own commit before that.

There is no deadline and no clipboard for this run, so the run's final output is exactly two things and nothing else: the `## Process review` section in a code fence, and the link https://github.com/seanr87/gradient-ascent/blob/master/data/ledger.md.

The push notification is one line, under 200 characters, and names any change made, for example: `Process: moved Thu trades to 7 PM (2 misses at 8 AM).` or `Process: reverted Thu 7 PM slot (missed again).` or `Process: no changes. 5 of 6 lines landed; waiver time 3:05 AM confirmed.`
