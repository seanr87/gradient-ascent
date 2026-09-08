# Task: Tuesday waiver claims (Tue 9:30 PM ET)

Read `tasks/COMMON.md` first and follow it. This task produces this week's **waiver claims**. Waivers clear Wednesday 3:00 AM ET.

## Data
The scheduled pull commits a fresh digest at about 9:00 PM ET tonight. Freshness limit: 2 hours. If the digest is older, refresh it per COMMON.md.

## The decision
Evaluate the free-agent and waiver pool against every roster spot using the manual's scoring edges: +0.5 per rushing/receiving first down (volume and possession players spike), rushing QBs spike, -2 INT and 4-pt pass TD sink pocket passers, distance kicker scoring, streamable DEF by matchup, and no IR slot so injured players occupy real roster space. Weigh the trending-adds list as a signal of who other managers will chase, and my waiver position from the standings.

Produce a ranked claim list, at most five claims. Each claim is one line in exactly this form, followed by a one-line reason:

```
ADD [player, position-team] / DROP [player, position-team]
```

Rank claims in the order Sean should enter them; Sleeper processes in priority order and cancels later claims that reuse a drop that already succeeded. Say explicitly when a claim is a conditional backup for an earlier one. If the correct call is no claims, write `NO CLAIMS` and explain in one paragraph.

## File
`docs/_decisions/2026-wkNN-tue-waivers.md`, kind `waivers`, title `Week NN waiver claims`. Sections:
- metadata line: decision time (ET) and digest pulled timestamp
- `## Claims (enter in this order)`
- `## Reasoning` (a short paragraph per claim, plus notable players passed on and why)
- `## For the clipboard` (only the ADD/DROP lines, or `NO ACTION`)

Commit message: `Week NN waiver claims: <summary>`.
