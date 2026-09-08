# Task: Thursday Night Football call (Thu 5:00 PM ET)

Read `tasks/COMMON.md` first and follow it. This task produces the **Thursday start/bench call**. Thursday players lock at kickoff, usually 8:15 PM ET, so the output must be final and unambiguous.

## Data
Always refresh the digest per COMMON.md so injury designations are current. Then use web search for the Thursday game's inactives and injury news for any of my players in it, and cite what you found.

## The call
Determine which NFL teams play tonight. If the digest does not say and web search cannot confirm, say so plainly and give a conditional call ("if X plays tonight, START").

For every player on my roster whose NFL team plays tonight, starters and bench alike, output exactly one line, `START [player, position-team]` or `BENCH [player, position-team]`, followed by a one-line reason. When starting a Thursday player commits a FLEX or positional slot before the Sunday slate is known, name the Sunday alternative and say why the Thursday player wins or loses that comparison under this scoring. A Questionable Thursday player with no Sunday fallback is a real risk: no IR slot, no second chance after lock.

If no rostered player plays tonight, write `NO THURSDAY PLAYERS` and note in one paragraph any Thursday-game player on this week's opponent's roster.

Also list any of my players with a new injury designation since the last decision file, as a heads-up for Sunday, without making Sunday's call yet.

## File
`docs/_decisions/2026-wkNN-thu-tnf.md`, kind `thursday`, title `Week NN Thursday call`. Sections:
- metadata line: decision time (ET), digest pulled timestamp, Thursday game and kickoff if known
- `## Call` (START/BENCH lines or `NO THURSDAY PLAYERS`)
- `## Reasoning`
- `## Injury watch for Sunday`
- `## For the clipboard` (only START/BENCH lines, or `NO ACTION`)

Commit message: `Week NN Thursday call: <summary>`.
