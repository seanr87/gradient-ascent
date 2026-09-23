# Task: Waiver filing check (Tue 10:30 PM ET)

Read `tasks/COMMON.md` first and follow it, with the exceptions in "What this task does not do" below.

This task exists because of a specific, repeated, documented failure: in Week 1 and Week 2 the Tuesday claims file was written, committed and pushed on time, and **not one claim was ever filed in Sleeper**. Two waiver runs, zero claims, from a team whose own operations manual says waivers won the league. The decision was never the problem. The gap between the decision and the app was.

This run closes that gap while there is still time to act. Waivers process **Wednesday 3:14 AM ET** (confirmed from the league transaction log, not from settings). Firing at 10:30 PM leaves roughly four and a half hours.

## What this task does not do

It writes **no decision file**, makes **no claim of its own**, and changes **no lineup**. It does not second-guess the claims in this week's waiver file; if it disagrees with them, that is Tuesday's file's business and next Tuesday's. It refreshes the digest, checks one fact, and either stays quiet or raises the alarm. Committing the refreshed digest per COMMON is the only write it makes.

## The check

1. Read this week's `docs/_decisions/2026-wkNN-tue-waivers.md`. If it does not exist, the 6:00 PM routine failed — say so and notify.
2. Pull the league's pending waiver claims directly. The digest does not carry them, so query the API:

```
https://api.sleeper.app/v1/league/1389359498023436288/transactions/<leg>
```

Use the current leg (and check the previous one — Sleeper has filed a Wednesday run under the prior leg before). Look for transactions with `type` of `waiver` whose `roster_ids` contain **8** (Gradient Ascent) and whose `status` is `pending`.

3. Compare what is filed against what the claims file ordered:

- **Every claim filed, in the right priority order** — quiet. Report it and send no notification. A silent Tuesday night is the success case and must stay silent, or the alarm stops meaning anything.
- **No claims filed at all** — notify. This is the failure that has happened twice.
- **Some filed, some missing, or the order does not match the file** — notify, naming exactly which lines are missing and where the order diverges.
- **Cannot determine** (endpoint unreachable, pending claims not exposed, ambiguous response) — notify saying so plainly, and give the claim lines again so Sean can check by eye. Never report "all filed" from an absence of evidence; an unverifiable check is a failed check, not a pass.

## Reporting

This task writes no decision file and does not touch `data/ledger.md`. Per COMMON.md the run's final output is exactly three things: the deadline line (`**Do by:** Wed 3:00 AM ET`, until the process review settles the measured time), a code fence holding either `ALL FILED` or the missing `ADD / DROP` lines verbatim in the claims file's order (or `CANNOT VERIFY` followed by every claim line), and the link to this week's waiver decision page. Nothing else. When notifying, the notification leads with the action and repeats the missing `ADD / DROP` lines verbatim from the claims file so Sean can paste without opening anything:

`Waivers process in 4h and no claims are filed. ADD Hill / DROP Allen; ADD Vele / DROP Lemon.`

If everything is filed, the report says so and **no notification is sent**.
