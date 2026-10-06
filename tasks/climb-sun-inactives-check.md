# Task: Sunday inactives check (Sun 11:30 AM ET)

Read `tasks/COMMON.md` first and follow it, with the exceptions below. Sean asked (Week 4) for a timed push when a contingency in the Sunday lineup file is owed. This run is that push.

## What this task does not do
It writes **no decision file** and changes no lineup. It refreshes the digest, checks, and either stays silent or sends one notification.

## The check
1. Read this week's `docs/_decisions/2026-wkNN-sun-lineup.md`. If it does not exist, notify: `Week NN lineup file MISSING at 11:30 AM; no contingencies checked.`
2. For every `IF ... inactive` line in its clipboard, and every starter tagged Questionable or Doubtful in the file, check the player's status with web search (ESPN or NFL.com inactives, official team report, a reporter's post). Inactives are posted about 90 minutes before kickoff, so by 11:30 AM ET the 1:00 PM games are known.
3. If a contingency is **triggered** (the player is inactive or ruled out), notify with the exact swap lines to paste, and the lock time. If every contingency is **not triggered**, or none exists, stay silent: no notification, one line in the report saying so. A push every Sunday stops meaning anything.
4. If the status cannot be determined, notify saying so and repeat the swap lines so Sean can check by eye.
5. Commit only the refreshed digest per COMMON.

Report: one line, `NO SWAP OWED` or the swap lines. Notification, when sent, under 200 characters and leading with the swap, e.g. `Week 05: Nacua is inactive. START Addison at WR, Mumpfield at FLEX before 1:00 PM.`
