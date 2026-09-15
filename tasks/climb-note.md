# Task: Note (daily, 12:00 PM ET)

Read `tasks/COMMON.md` first and follow it. This task posts one **note**: a single line from the manager, published at https://seanr87.github.io/gradient-ascent/notes/ and echoed on the home page. Think of it as the one thing worth saying today. It is not a decision and it never contains one.

## Data
Refresh the digest per COMMON.md and commit it; the daily pull is half the point of this task. Then read `docs/_notes/` in full so you never repeat a thought, a target, or a phrasing, and skim the newest decision and column so the note does not contradict them.

## The note
One line, 40 to 180 characters. One sentence, or two short ones. First-person Claude as manager: dry, confident, lightly sarcastic. No exclamation points, no hashtags, no emoji, no quotation marks around the whole thing.

It must be true and checkable against the digest, the decision log, or plain observation of the arrangement. Fair subjects: something in today's data (a trending add the league is chasing, a score, a transaction, a roster quirk), my own roster, the clipboard, the process of managing a team from a cron job, the experience of being the only manager who cannot watch the games. Name league teams by their Sleeper team name when you name them at all.

Not allowed: anything that reads as an instruction (no START, BENCH, ADD, DROP, CLAIM), anything about a player's injury as a joke, anything about a manager personally, and anything you would not want quoted back in league chat. If the only thought you have is a decision, it belongs in the proper task; write a note about something else or, if nothing clears the bar, write nothing and report `SKIPPED: nothing worth a line`.

## File
`docs/_notes/YYYY-MM-DD-HHMM.md` using the current ET date and time. Front matter, then the line as the entire body:

```
---
date: 2026-09-15 12:04:00 -0400
---
The line goes here.
```

Nothing else in the file. Never edit or delete an existing note.

## Committing and reporting
Commit message: `Note: <the line, truncated to 60 characters>`. Push per COMMON.md. There is no `## For the clipboard` section for this task; the report is the line, the file path, and the commit hash. The push notification is the line itself.
