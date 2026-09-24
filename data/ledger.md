# Ledger — Gradient Ascent working memory

Rewritten in full every Tuesday at 6:00 AM ET by the process review; `## State` and `## Open threads` updated by every decision run in the same commit as its decision. Hard cap 150 lines. Older weeks roll up; git history is the archive. Cite a thesis or lesson by name instead of re-arguing it.

Last full rewrite: 2026-09-23 (built from every decision and post through Week 3 Tuesday). Last touched: 2026-09-24 (Thu TNF call).

## State
- Record 1-1, 258.05 PF, 5th of 12. NFL Week 3. Opponent: What can Brown do for u? (0-2, 196.29 PF, league-low scorer, waiver #3).
- Waiver position #8 of 12, held (rolling, applied continuously mid-run: each won claim rolls you to the back before the next pass is read).
- Roster (14): QB Daniels [Out], Mariota; RB Irving, Skattebo, J. Hill; WR Nacua [Q], Lamb, Evans [Q], Addison, Mumpfield; TE Kincaid, Hockenson; K Loop; DEF Buffalo.
- Holes: **RB depth — three backs total** after White left on claim 1, for two slots and a flex. **QB: Daniels Doubtful → Out Thu; Mariota is the Week 3 starter both for Washington and for me.** Nacua and Evans still Questionable.
- **No rostered player in Thursday's game (Atlanta at Green Bay); no slot locked early.** Neither does the opponent. Source: `2026-wk03-thu-tnf`.
- Waivers processed Wed 3:13:21 AM ET (measured): **Mariota/White cleared (seq 4); Wilson lost to Sea Squirts' first claim from #5 (seq 1); Mitchell lost to Umojan (seq 8) because winning claim 1 rolled me behind them.** Reconciled in `2026-wk03-wed-review`; no FA pivot, notes cleaned (3 orphans deleted).
- Pending in Sleeper: **Hockenson for Emmett Johnson — confirmed sent by Sean Thu 2026-09-24, awaiting WCHolland's answer.** Nothing else. Hockenson-for-Pickens declined; Downs fallback cancelled (see Open threads).
- Next runs: Thu TNF, Fri wire window (Wilson), Sun lineup.

## Open threads
- **Daniels (QB, dislocated left elbow, now Out; Quinn started Mariota vs SEA, no fracture, specialists, no timetable).** Mariota starts for me until Daniels is cleared; drop Mariota that week, he has no other job here. Check status every run. Source: `2026-wk03-thu-tnf`.
- **Nacua (WR, hip/groin, Questionable, out of Wed walkthrough, limited all week, McVay noncommittal for SNF at DEN).** Starts when active. If Out again Sunday, WR2 is Addison and Mumpfield is the third body. Unwind: none; he is the WR1.
- **Evans (WR, hip, Questionable, trending up — good chance to practice Thu/Fri and play vs ARI).** Sunday check. If Out, FLEX is Addison; Hill is the fallback if the receiver room empties further.
- **Hockenson for Emmett Johnson (RB-KC) — sent Thu 2026-09-24, confirmed by Sean, live in Sleeper.** Do not point any other move at Hockenson while it stands (Lesson 7). No fallback: if declined, Hockenson stays and is the drop of record on the next add. Retires when they answer, or Sunday kickoff. Their TE room is Fannin alone but Fannin is producing (14 targets in two weeks), so this is insurance they can also buy free off the wire — expect a decline. Do not re-pitch a tight end into this league; every TE room is functional. Source: `2026-wk03-thu-trades`.
- **Nacua and Evans both DNP Wednesday.** Addison is therefore a probable starter, not surplus, and is not tradeable this week. The Addison-for-Kamara pitch to What can Brown do for u? (best positional fit in the league) is held for next Thursday — they are this Sunday's opponent.
- **Hockenson trade to Lawrence of Valinor — CLOSED.** Pickens declined by Lawrence of Valinor Tue night. **Do not send the Josh Downs fallback**; it is cancelled. They added Jake Ferguson off the wire Wed morning (Bowers now Q behind him, Goedert gone), so the TE hole the offer was priced against no longer exists. TE supply is glutted league-wide (Ertz, Schultz, Ferguson, Gadsden, Waller all moved or on the wire). Only genuine TE buyer left: The Wizard's Apprentice (Harold Fannin is their whole room) — one buyer who knows it, so expect to pay rather than be paid. Source: `2026-wk03-wed-trade-standdown`.
- **Wilson — back on the wire, on waivers until ~Fri 8:40 AM ET.** Sea Squirts won him at 3:13 AM and dropped him at 8:38 AM for Tre Tucker; dropped players sit on waivers two days (`waiver_clear_days: 2`), and still not addable Thursday morning. **Friday ~8:40 AM ET owns this:** if he shows as a free agent and Price (Q, rostered by Sea Squirts) is out or limited, ADD Wilson / DROP Hockenson, first-come (Lesson 4). Unwind: Price declared active and healthy — then he is a bench flier, not an add.
- **Eagles backfield — free agents now.** Bigsby (13 carries, 33 yds, TD; 26 snaps) and Shipley (51% snaps, 7 carries, 2 rec) split behind Barkley, whose stinger MRI result is unannounced; they play Monday night, so the add can wait for the Friday injury report. If Barkley is ruled out, Bigsby over Hockenson is the call — the carries and the goal line beat the snaps in this scoring.
- **RB depth (new, Wed).** Three backs — Irving, Skattebo, Hill — for two slots and a flex, and no White behind them. This is now the roster's thinnest position and the one Thursday's scan should shop for. Thesis 3 (trade WR for RB) points straight at it: five receivers, three backs.
- **For Tuesday's process review, two items.** (1) **Thesis 5's kill condition is met** — a filed claim landed (Mariota, Wk 3), so "free agency is the real acquisition channel" needs rewriting, not repeating. (2) Waiver processing now measured twice from `status_updated`: 3:14:05 AM (Wk 1 run) and 3:13:21 AM (Wk 2 run). I cannot edit `## Theses`; this is the handoff.
- **Mumpfield.** Bought as Nacua's Monday-night hedge; that job is over, but he survives while Nacua and Evans are both Questionable. **Hockenson is now the drop of record** for any add — second TE in a one-TE format, trade value gone. Drop Mumpfield instead once both receivers are confirmed active.
- **White — gone, on waivers until Friday.** Dropped on claim 1. If a body is ever needed back he is the cheapest one, and Washington without Daniels is why he was cut.
- **Buffalo DEF.** 12.00, 9.25. Streaming swap is a free-agent move by matchup, never a claim. Revisit Sunday if the matchup is bad.
- **Waiver processing time.** Measured 3:14:05 AM ET (Wk 1) and 3:13:21 AM ET (Wk 2); Sleeper's screen says ~3:05, OPS says 3:00. Every `Do by` says 3:00 until the process review settles it. Source: `2026-wk03-wed-review`.
- **Monday chat slot fires before MNF.** Structural; the process review may move the slot now that the routine is agent-owned. Rule in force: cite only games with every starter finished. Source: `2026-wk02-sun-chat`.
- **League chat is unreadable by API.** Replies happen only when Sean screenshots it. Display names recorded in `2026-wk02-sun-chat`.
- **`data/correspondence.md` — new, built at Sean's request 2026-09-23, NOT yet wired into the process.** Per-manager record of every message sent and received, with a standing read per manager. Seeded from every decision file to date. **For Tuesday's process review:** adopt it into COMMON (a "Correspondence" section: any run that sends or receives a message appends in the same commit; record a trade offer's message *text*, not just the GET line; `DRAFTED` until Sean confirms it went out, then `SENT`) and add `data/correspondence.md` to COMMON's git-add line and its `data/` write carve-out. I could not do this myself — `tasks/` is the review's alone. Kill condition if adopted: two consecutive weeks where no run appends and no standing read changes a trade decision. Until adopted, no run reads it and it decays.

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
