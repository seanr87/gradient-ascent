# Task: Thursday Night Football call (Thu 5:00 PM ET)

Read `tasks/COMMON.md` first and follow it. This task produces the **Thursday start/bench call**. Thursday players lock at kickoff, usually 8:15 PM ET, so the output must be final and unambiguous.

## Run once a week — check this first
**If `docs/_decisions/2026-wkNN-thu-tnf.md` already exists for this week, stop.** Do not write a second one and never edit the first. Give the standard three-line report from the existing file (its `**Do by:**` line, its `## For the clipboard` section in a code fence, its page link), send no push notification, and stop. Refreshing and committing the digest per COMMON is fine; writing a second call is not. Two routines may fire this task until the old UI-created one is disabled (see `SCHEDULED-TASKS.md`); both firing must be harmless.

## Data
COMMON.md already refreshed the digest at the start of this run, so injury designations are current. Then use web search for the Thursday game's inactives and injury news for any of my players in it, and cite what you found.

## The call
Determine which NFL teams play tonight. If the digest does not say and web search cannot confirm, say so plainly and give a conditional call ("if X plays tonight, START").

For every player on my roster whose NFL team plays tonight, starters and bench alike, output exactly one line in the clipboard, `START [player, position-team]` or `BENCH [player, position-team]`, with its one-line reason under `## Why`. When starting a Thursday player commits a FLEX or positional slot before the Sunday slate is known, name the Sunday alternative and say why the Thursday player wins or loses that comparison under this scoring. A Questionable Thursday player with no Sunday fallback is a real risk: no IR slot, no second chance after lock.

If no rostered player plays tonight, write `NO THURSDAY PLAYERS` and note in one paragraph any Thursday-game player on this week's opponent's roster.

Also list any of my players with a new injury designation since the last decision file, as a heads-up for Sunday, without making Sunday's call yet.

## File
`docs/_decisions/2026-wkNN-thu-tnf.md`, kind `thursday`, title `Week NN Thursday call`, in the structure COMMON.md fixes:
- `**Do by:**` tonight's kickoff (ET), naming the game · `**Digest:**` pulled timestamp
- `## For the clipboard`: only START/BENCH lines, or `NO ACTION` (which covers `NO THURSDAY PLAYERS`)
- `## Why`: one line per START/BENCH call, naming the Sunday alternative where a slot is being locked early; if no rostered player plays tonight, one line saying so and one on any Thursday player on my opponent's roster
- `## Detail` (optional, 250 words max): the injury watch for Sunday, one line per rostered player with a new designation since the last decision file, no Sunday call made; sources as one line of links

Update `## State` and `## Open threads` in `data/ledger.md` in the same commit: locked slots, new injury designations.

Commit message: `Week NN Thursday call: <summary>`.
