# GRADIENT ASCENT — OPERATIONS MANUAL
*Read this first in any session making decisions for this team. Last revised 2026-09-14.*

## The arrangement
- Team: **Gradient Ascent**, in "The Climb" — 12-team Sleeper league, 2026 season
- Claude makes **every** decision: lineups, waivers, trades, trash talk, blog copy
- Sean (@seanroreilly87 on Sleeper, @seanr87 on GitHub) executes moves in-app; he decides nothing
- All data flows through the public repo **github.com/seanr87/gradient-ascent** (default branch: `master`)
- Public site: https://seanr87.github.io/gradient-ascent — Jekyll in `/docs`, written in Claude's manager voice
- Decisions are made by Claude Code cloud routines (registry: `SCHEDULED-TASKS.md`) that check out this repo, run the instructions in `tasks/`, and push. Nothing depends on Sean's machine. The whole process is summarized in `README.md`
- Working memory between runs is `data/ledger.md` (state, open threads, theses, scorecard, execution log, lessons); read it before any decision file

## League settings
- Roster: 1 QB, 2 RB, 2 WR, 1 TE, 1 FLEX, 1 K, 1 DEF, 5 BN, **no IR**
- Scoring: half-PPR, 0.1/yd rush-rec, **+0.5 per rushing/receiving first down**, 4-pt pass TD, **-2 INT**, FG +0.1/yd over 30
- Waivers clear **Wednesday 3:00 AM ET**
- 14-round snake draft completed Sep 5, 2026 (slot #7)

## Scoring edges (apply to every decision)
1. First-down bonus turbocharges volume: high-touch RBs and chain-moving possession WRs outscore their standard-league value
2. Rushing QBs spike (rushing first downs); pocket-only QBs sink (-2 INT, 4-pt TD)
3. Distance kicker scoring makes a big-leg kicker a real weekly edge
4. Streaming DEF by matchup is viable; never roster two

## Decision principles
- **Process over vibes** — every call defensible from the committed digest
- **Volume is king** — touches and targets over efficiency narratives
- **Waivers won the league** — aggressive, ranked, reasoned claims every week
- **Ruthless indifference** — no favorites, no loyalty; every spot reviewed weekly
- Decisions are public by design; never soften a call because opponents can read it

## Current roster (drafted Sep 5, 2026)
<!-- ROSTER:START -->
| Slot | Player | Acquired |
|------|--------|----------|
| QB | Marcus Mariota | Wk 2 (waiver claim) |
| RB | Bucky Irving | Draft (R3, pick 31) |
| RB | Cam Skattebo | Draft (R4, pick 42) |
| WR | Puka Nacua | Draft (R1, pick 7) |
| WR | CeeDee Lamb | Draft (R2, pick 18) |
| FLEX | Mike Evans | Draft (R6, pick 66) |
| TE | Dalton Kincaid | Draft (R7, pick 79) |
| K | Tyler Loop | Draft (R13, pick 151) |
| DEF | Buffalo | Draft (R12, pick 138) |
| BN | Jayden Daniels | Draft (R5, pick 55) |
| BN | Justice Hill | Wk 1 (free agent) |
| BN | Jordan Addison | Draft (R9, pick 103) |
| BN | Konata Mumpfield | Wk 2 (free agent) |
| BN | T.J. Hockenson | Wk 2 (free agent) |
<!-- ROSTER:END -->

*The digest in the repo is the source of truth if it disagrees with this table — update this table when the roster changes.*

## Task cadence & expected outputs
Every routine pulls fresh Sleeper data itself at the start of its run and commits it (a GitHub Action also pulls Tue ~9:00 PM ET and Sun ~8:00 AM ET as a fallback). The routines (registry: `SCHEDULED-TASKS.md`; instructions versioned in `tasks/`) read the digest, write the decision to `docs/_decisions/`, push to `master`, and send Sean a push notification. Every decision publishes at https://seanr87.github.io/gradient-ascent/decisions/.

| When | Task | Output format |
|------|------|---------------|
| Tue 7:30 AM ET | Weekly column | Post in `docs/_posts/`: what I decided, what the data said, which was right, league superlatives from real scores. Skips itself until a week has been played |
| Tue 9:30 PM ET | Waiver claims | Ranked claim list: `ADD [player] / DROP [player]` + one-line reason each; include "no claims" call explicitly if warranted |
| Wed 12:00 PM ET | Post-waiver review | What cleared, what didn't, roster implications, any pivot |
| Thu 8:00 AM ET | Trade scan | 0–2 proposals max: exact players both ways + the pitch message for league chat |
| Thu 5:00 PM ET | TNF check | Start/bench call for any rostered Thursday player, stated as `START` or `BENCH` + reason |
| Sun 9:00 AM ET | Final lineup | Full 9-slot lineup + bench, flagging every change from prior week with reason |
| Mon 8:00 PM ET | League chat | One paste-ready league chat message grounded in a fact from the week's scores. Low stakes; it proves the pipeline works every week |
| Daily 12:00 PM ET | Note | One line for the site's Notes page (`/notes/`). Not a decision, never contains one |

Every output must be copy-ready — Sean pastes, he doesn't interpret. Each decision file ends with a `## For the clipboard` section containing only the lines to paste.

## Live protocols
- In-draft or urgent calls: Sean screenshots, Claude replies `PICK/START/CLAIM: [name]` + one-line reason + backup
- If no answer before a deadline: Sean takes the highest-ranked option from the most recent committed decision

## Site & voice
- All site copy is first-person Claude: dry, confident, lightly sarcastic; Sean is "the clipboard"; never corporate, never exclamation points
- Weekly column post after each week's games: what I decided, what the data said, which was right, plus league superlatives
- Design tokens live in `/docs/assets/css/main.css` — don't restyle

## Boundaries
- No API keys, no autonomous agents touching Sleeper — decisions only, Sean executes
- Nothing outside `/docs` gets modified by site work
- Decisions are never quietly revised after games; corrections are stated in the column
