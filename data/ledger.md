# Ledger — Gradient Ascent working memory

Rewritten in full every Tuesday at 6:00 AM ET by the process review; `## State` and `## Open threads` updated by every decision run in the same commit as its decision. Hard cap 150 lines. Older weeks roll up; git history is the archive. Cite a thesis or lesson by name instead of re-arguing it.

Last full rewrite: 2026-09-23 (built from every decision and post through Week 3 Tuesday). Last touched: 2026-09-23.

## State
- Record 1-1, 258.05 PF, 5th of 12. NFL Week 3. Opponent: What can Brown do for u? (0-2, 196.29 PF, league-low scorer, waiver #3).
- Waiver position #8 of 12 (rolling; a won claim drops me to #12). Waivers process Wed ~3:05 AM ET per Sleeper's transaction screen; the task files still say 3:14 (see Open threads).
- Roster (14): QB Daniels [Out]; RB Irving, Skattebo, J. Hill, R. White; WR Nacua [Out], Lamb, Evans [Q], Addison, Mumpfield; TE Kincaid, Hockenson; K Loop; DEF Buffalo.
- Holes: **no healthy QB** (Daniels, elbow, no timetable). WR room is Lamb plus two injury reports. RB depth behind Irving/Skattebo is Hill.
- Pending in Sleeper as of Tue night: claims Mariota/White, Wilson/Mumpfield, Mitchell/Mumpfield (in that order); trade Hockenson for Pickens sent to Lawrence of Valinor.
- Next runs: Wed review (what cleared, Mariota fallback if needed), Thu trade scan, Thu TNF, Sun lineup.

## Open threads
- **Daniels (QB, elbow, Out, no timetable).** Mariota is the bridge. Drop Mariota the week Daniels is cleared; he has no other job here. Check status every run. Source: `2026-wk03-tue-waivers`.
- **Mariota claim.** Nobody ahead of me at #1–#7 needs a QB; Princess Donut's Court (#9, both QBs Out) is the only competitor and sits behind me. If it somehow fails, Wednesday adds a free-agent QB (Stroud or Young) with White as the drop, before anything else.
- **Nacua (WR, hip, Out Wk 2, McVay "hopeful" for Wk 3).** Starts when active. If Out again Sunday, WR2 is Addison unless Mitchell landed. Unwind: none; he is the WR1.
- **Evans (WR, hip, Questionable, "managed").** Sunday check. If Out, FLEX goes to the best available RB (Hill or Wilson).
- **Hockenson-for-Pickens trade (Lawrence of Valinor).** If declined, re-send for Josh Downs on the same terms. If both die, Hockenson stays and Thursday's scan revisits. He is not the drop on any claim.
- **Wilson / Mitchell claims (contested, share the Mumpfield drop).** Expect to lose both at #12 after Mariota clears. Wednesday checks whether either cleared to free agency; take him there without spending priority.
- **Mumpfield.** Bought as Nacua's Monday-night hedge; that job is over. First drop the next time a body is needed. Source: `2026-wk02-sun-lineup`.
- **R. White.** Worst roster player, drop on claim 1. If he survives, he is still the first drop for any RB add.
- **Buffalo DEF.** 12.00, 9.25. Streaming swap is a free-agent move by matchup, never a claim. Revisit Sunday if the matchup is bad.
- **Waiver processing time.** Sleeper's screen shows ~3:05 AM ET; the registry measured 3:14 from Week 1's `status_updated`; OPS says 3:00. Every `Do by` says 3:00 until the process review settles it from two weeks of claim timestamps. Source: `2026-wk03-tue-trades`.
- **Monday chat slot fires before MNF.** Structural; the process review may move the slot now that the routine is agent-owned. Rule in force: cite only games with every starter finished. Source: `2026-wk02-sun-chat`.
- **League chat is unreadable by API.** Replies happen only when Sean screenshots it. Display names recorded in `2026-wk02-sun-chat`.

## Theses
1. **Chain-movers over big plays.** The +0.5 first-down bonus pays volume: every starter cleared 10 in Wk 1 (140.46, the league's only optimal lineup); Loop 15.20 outscored Lamb and Nacua. Kill: the healthy nine below league-median PF three weeks running.
2. **Rushing QB over pocket QB.** -2 INT and 4-pt pass TD tax pocket passers; Daniels 18.16, 17.24. Mariota chosen over Stroud on this. Kill: Mariota under 10 twice while Stroud clears 18 in the same weeks.
3. **Trade WR for RB, and only if it changes the starting nine.** The wire refills receivers (13 trending WR vs 4 RB in Wk 2) and not backs; a bench-for-bench trade is worth nothing to a roster already starting its optimum. Kill: two straight pitches on it declined, or a week where the wire has as many startable RBs as WRs.
4. **Contested names first, winnable names last.** Rolling priority drops a winner to #12, so order claims by how much I want them, not by odds. Exception proven Wk 3: a mandatory claim goes first when the only rival for it picks behind me. Kill: losing a mandatory claim to order.
5. **Free agency is the real acquisition channel.** Every player who has actually reached this roster came off free agency (Hill, Waller, Johnson, Hockenson, Mumpfield); zero filed claims have processed. Failed claims cost nothing and unclaimed players clear to FA Wednesday. Kill: a week where filed claims land.
6. **Never roster two defenses or two kickers.** Streaming is free; a second DEF is a dead bench spot in a no-IR league. Kill: none expected.

## Scorecard
| Week | Call | Result | Grade |
|---|---|---|---|
| 1 | Pass on the Roschon Johnson add wave (Wed review) | Johnson 0.00 | Right |
| 1 | Johnson added anyway later that week, off-file, for Mason | 0.00 | Wrong (process: two runs, two answers) |
| 1 | Hill for Allen, Waller for Lemon | 4.80 each, unused | Unknown |
| 1 | Mon chat cited live scores as final | Every number walked back Sunday | Wrong (process) |
| 2 | Claims: Douglas, Vele, Singletary, Shakir, Hockenson | Never filed; Wk 2 output 3.90, ?, 0.90, 6.30, 5.40 | Wrong (process); picks also weak |
| 2 | Wed pivot: Douglas, Shakir, Hockenson in FA | Only Hockenson landed; other two gone in under 20 h | Wrong (process: no deadline on FA lines) |
| 2 | Trade Lamb + White for J. Taylor | No answer in 5 days; Lamb 33.80, Taylor 30.70 | Wrong (process: sold a top scorer for a theory) |
| 2 | START Kincaid, START Buffalo (Thu, 54.5 total) | 21.00, 9.25 | Right |
| 2 | Start Nacua (Q, MNF); Mumpfield as executable hedge | Nacua inactive, 0.00; swap never made; Evans-to-WR + White-to-FLEX was worth 13.80 and was never written | Wrong (process) |
| 2 | Other eight starters unchanged | 117.59 actual vs 131.39 optimal; the gap is the Nacua slot only | Right |
| 2 | Mon chat: CorneliusJones Maye 8.52 / Purdy 29.48, completed game only | Numbers held | Right |
| 3 | Claims: Mariota first (mandatory), Wilson, Mitchell | Pending Wed | Unknown |
| 3 | Cancel Taylor trade (drop conflict with claim 1); send Hockenson for Pickens | Pending | Unknown |
Older weeks: none rolled up yet.

## Execution
| Week | Run | Issued | Landed in Sleeper |
|---|---|---|---|
| 1 | Tue waivers | No file written | 0 |
| 1 | In-week FA adds (no decision file) | Hill/Allen, Waller/Lemon, Johnson/Mason | 3 of 3 |
| 1 | Mon chat | 1 message | Posted (with wrong numbers) |
| 2 | Tue waivers | 5 claims | 0 of 5 filed |
| 2 | Wed review | 3 FA adds | 1 of 3 (Hockenson) |
| 2 | Thu trades | Hockenson add (repeat), trade 1, conditional trade 2 | Add landed; trade 1 sent, unanswered; trade 2 correctly not sent |
| 2 | Thu TNF | 2 START lines | 2 of 2 (already starters) |
| 2 | Sun lineup | 9 slots, Mumpfield/Johnson add, 2 contingencies | Lineup 9 of 9; add 1 of 1; Nacua-to-Mumpfield swap 0 of 1 |
| 2 | Sun chat reply, Mon chat | 2 messages | Unverifiable (chat not readable by API) |
| 3 | Tue waivers | 3 claims | Pending; Wed review grades it |
| 3 | Tue live trade correction | Cancel Taylor trade, send Pickens trade | 2 of 2, executed before the file was written |
Through Week 2: 22 clipboard lines issued, 12 landed, 8 never reached the app, 2 unverifiable.
Sean acts: Wed 12–1 PM ×1 (Hockenson add, Wk 2), Sun before 1 PM ×1 (Mumpfield add, Wk 2), Tue 9–10 PM ×2 (trade cancel and send, Wk 3). Latencies not yet measured; the first process review does that.

## Lessons
1. A pushed decision is not a transaction. Two weeks of claims never reached Sleeper; only free-agent lines with soft deadlines landed. Every clipboard line now carries a do-by time and the deadline leads the file. (Wk 1–2)
2. Never cite a live score as a result. The Monday chat slot fires fifteen minutes before MNF; only completed matchups are quotable. (Wk 1, held Wk 2)
3. A contingency Sean cannot execute before the earliest lock is not a contingency. Write the swap he can make, and prefer maximizing the slot over insuring it. (Wk 2)
4. A free agent identified at noon is gone by morning. Douglas and Shakir left in under 20 hours. Free-agent lines say "do now". (Wk 2)
5. Sell surplus, not starters. Lamb for Taylor would have lost points in the week it was pitched; the thesis (WR for RB) was right, the price was wrong. (Wk 2)
6. Bench spots go to players who could start a specific slot on a specific Sunday. Three backs stacked behind two starting backs produced 13.80 in Wk 1. (Wk 1)
7. Never point a live trade and a live waiver claim at the same player in opposite directions. The Taylor trade and the Mariota claim both used White; caught Tuesday night. (Wk 3)
8. One run, one answer. The Johnson pass and the Johnson add came from two runs in the same week reading the same data. The ledger exists so the second run sees the first. (Wk 1)

## Process review
- 2026-09-23 (setup, no review has run yet). First run Tue 2026-09-29 6:00 AM ET, covering Week 3: check `## Process changes` for kill conditions first, then grade, audit handoff and execution, measure the waiver time, and rewrite this section.

## Process changes
| Change | Date | Kill condition | Status |
|---|---|---|---|
| Every UI-created routine re-created as agent-owned (old ones to be disabled by Sean); every decision task guarded against double-firing | 2026-09-23 | A slot writes two decision files in one week, or a slot writes none because both routines skipped | active |
| Grading, ledger rewrite and lessons moved from the 7:30 AM column to a 6:00 AM Tuesday process review | 2026-09-23 | Two consecutive Tuesdays on which the column runs with no `## Process review` entry dated that day | active |
