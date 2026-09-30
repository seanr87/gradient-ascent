# Ledger — Gradient Ascent working memory

Rewritten in full every Tuesday at 6:00 AM ET by the process review; `## State` and `## Open threads` updated by every decision run in the same commit as its decision. Hard cap 150 lines. Older weeks roll up; git history is the archive. Cite a thesis or lesson by name instead of re-arguing it.

Last full rewrite: 2026-09-29 (first process review, covering Week 3). Last touched: 2026-09-30.

## State
- **Week 3 final: lost 116.72 to What can Brown do for u? 124.84 (8.12).** Record 1-2, 374.77 PF, 8th of 12. NFL Week 4 opens Thu. Opponent: CorneliusJones (1-2, 343.82 PF).
- Waiver position **#7 of 12** (won a claim at seq 3, so I sit ahead of the five other winners; six non-winners hold #1-#6).
- Roster (14): QB Mariota, Daniels [Q]; RB Irving, Skattebo, **B. Allen**, J. Hill; WR Lamb, Addison, Mumpfield, Nacua [Q], Evans [Q]; TE Kincaid; K Loop; DEF Buffalo. Hockenson dropped Wed 3:13 AM.
- Holes: **TE is one deep by choice (Kincaid only).** RB is three deep behind two slots and a flex, which was the point of the claim. WR is not a hole if Nacua or Evans clears.
- Pending in Sleeper: **nothing.** All four Wk 4 claims resolved; last week's offers all dead.
- Next runs: Thu trade scan 8:00 AM, Thu TNF 5:00 PM, Sun lineup.
- Chat targets used: Wk1 Three Wise Jaylens, Wk2 CorneliusJones, Wk3 Lost in the Land of Love, then Princess Donut's Court (Mon). Sources: `2026-wk03-mon-chat`.

## Open threads
- **Daniels (QB, dislocated elbow, Questionable, expected to practice this week).** Mariota starts until he is cleared; drop Mariota that week. Check every run.
- **Nacua (WR, hip) and Evans (WR, ribs), both Questionable** after two weeks Out. Unwinds when either is active; if both sit Sunday, Mumpfield and B. Allen fill WR and FLEX.
- **B. Allen (RB-NYJ), claimed Wk 4.** Jets' starter while Breece Hall's quad heals. Unwinds when Hall returns; he is a FLEX candidate, not a hold.
- **Ollie Gordon went to The Wizard's Apprentice** (waiver #1, seq 1), who also took Keenan Allen. They are 1-2 and now waiver #12. Thursday trade target: they are deep at RB and just dropped a tight end.
- **RB depth.** Thesis 3 trade market is dead (three offers, three refusals); the wire is the only channel.
- **Addison for Kamara pitch to What can Brown do for u?** Held; Addison is a certain starter, so do not send.
- **Buffalo DEF.** 9.50 in Wk 3 (12.00, 9.25 before). Cleveland, Las Vegas, Chicago and Arizona are all free; streaming is a free-agent move, never a claim.
- **Waiver processing time.** 3:14:05 (Sep 16), 3:13:21 (Sep 23), 3:13:34 (Sep 30) — three minutes, three values, all inside 3:13-3:15. Every `Do by` stays 3:00 AM ET; Tuesday's review can settle it.
- **The digest does not show waiver results.** Sleeper files Wednesday-morning waivers under the *previous* leg, so `transactions_this_week` was empty this morning and the review had to query leg 3 directly. For Tuesday's review.
- **Wk 4 claim latency: 4 h 50 m** (file 6:20 PM ET, claims created 11:10 PM ET), inside the deadline by 3 h 49 m. For Tuesday's execution audit.
- **Double-fire.** Both Sunday-lineup routines ran in full on 2026-09-27; the guard held (one file). Sean still has to disable the seven UI routines in `SCHEDULED-TASKS.md`.
- **Fri/Sat blind spot.** Nothing decides between Thu 5 PM and Sun 9 AM. Thu TNF now pastes the swap for any Out starter. A Saturday injury sweep needs routine tools this session lacks; revisit next review.
- **Monday chat slot fires before MNF.** Rule in force: cite only games with every starter finished.
- **League chat is unreadable by API.** Names: `data/correspondence.md` holds the per-manager read (adopted into COMMON 2026-09-29).

## Theses
1. **Chain-movers over big plays.** Wk 1: every starter cleared 10; Wk 3: Lamb 19.2, Addison 18.5, Skattebo 13.5, Loop 12.6 all fine, Irving 7.8 and Kincaid 3.3 were not. Kill: the healthy nine below league-median PF three weeks running (Wk 3: 116.72 vs median about 125, watch it).
2. **Rushing QB over pocket QB.** Daniels 18.16, 17.24; Mariota 20.92 in Wk 3. Kill: Mariota under 10 twice while Stroud clears 18 in the same weeks.
3. **Trade WR for RB, and only if it changes the starting nine.** Three offers, three refusals, and the receiver room is now the thin one (Nacua and Evans Out). Kill: two straight pitches declined (three refusals in Wk 3, so it is met; retire it unless a pitch lands next week).
4. **Contested names first, winnable names last.** Proven Wk 3: the mandatory claim went first and won, and winning it cost the third claim. Kill: losing a mandatory claim to order.
5. **Rewritten Wk 3: filed claims do land; the channel is claims plus free agency.** Mariota cleared at seq 4 on a claim filed 12 minutes after the file. Waiver position decides contested names (Wilson, Mitchell lost to earlier pickers). Kill: three straight weeks with no claim won.
6. **Never roster two defenses or two kickers.** Kill: none expected.

## Scorecard
| Week | Call | Result | Grade |
|---|---|---|---|
| 1-2 (rolled up) | Wk 1: three off-file adds and a Johnson reversal, chat cited live scores (Wrong: process ×2), Hill/Waller Unknown. Wk 2: 5 claims never filed, FA pivot 1 of 3, Lamb-for-Taylor sold a top scorer (Wrong: process ×3); Kincaid/Buffalo Right, Nacua/Mumpfield hedge never made (Wrong: process), chat numbers held (Right) | 22 lines issued through Wk 2, 12 landed | 5 Right, 6 Wrong (process), 2 Unknown |
| 3 | Claim 1 Mariota (mandatory, first) | Cleared 3:13:21 AM; 20.92 at QB | Right |
| 3 | Claims 2-3 Wilson, Mitchell | Lost to Sea Squirts (#5) and Umojan; unwinnable from #8 after claim 1 | Wrong (luck) |
| 3 | Cancel Taylor trade, send Pickens for Hockenson | Taylor no answer; Pickens declined; conflict with White avoided | Right |
| 3 | Thu scan: Hockenson for Emmett Johnson | Declined by The Wizard's Apprentice | Wrong (luck); no cost |
| 3 | Thu TNF: NO ACTION, "Daniels Out" only in Detail | Swap missing as a line until Sat 1:45 PM; no points lost | Wrong (process) |
| 3 | Sat: Mariota for Daniels | 20.92 vs 0.00 | Right |
| 3 | Sun: bench Nacua (Doubtful), Addison in | Nacua 0.00, Addison 18.50 | Right |
| 3 | Sun: start Evans (Q) at FLEX, Mumpfield as hedge | Evans 11.40 played; Mumpfield on bench scored 18.30; +6.90 missed, the loss was 8.12 | Wrong (luck): played, hedge unused |
| 3 | Other starters unchanged | Lamb 19.2, Skattebo 13.5, Loop 12.6, Buffalo 9.5, Irving 7.8, Kincaid 3.3 | Right |
| 3 | Mon chat vs Princess Donut's Court; Fri/Sat chat replies | Sent; MNF not started for any starter, no live scores cited | Right |

## Execution
| Week | Run | Issued | Landed in Sleeper |
|---|---|---|---|
| 1-2 (rolled up) | all | 22 lines | 12 landed, 8 never reached the app, 2 unverifiable |
| 3 | Tue waivers (file 8:58 PM ET) | 3 claims | 3 of 3 filed, 9:10, 9:13, 9:14 PM ET (12-16 min); Mariota won, other two lost on order |
| 3 | Tue live trade correction | Cancel + send | 2 of 2, before the file existed |
| 3 | Thu trades (file 8:10 AM ET) | 1 offer | Sent by ~8:58 AM ET (confirmed in ledger commit, ~48 min); declined |
| 3 | Thu TNF | NO ACTION | n/a |
| 3 | Sat QB swap (file 1:45 PM ET) | 1 line | Landed before Sun lineup; starters at lock show Mariota. Latency n/a |
| 3 | Sun lineup (file ~9:14 AM ET) | 9 slots, 1 contingency | 9 of 9 match the starters at lock; contingency not needed. Latency n/a |
| 3 | Chats (Fri ×2, Sat, Mon) | 4 | Unverifiable |
Wk 3: 15 lines issued; 15 landed or n/a, 0 known misses, 4 unverifiable. Claim latency 12-16 minutes; first week with no miss.
Sean acts: Tue 9-10 PM ×5 (2 trades Wk 3, 3 claims Wk 3), Thu 8-9 AM ×1, Sat 1-3 PM ×1 (QB), Sun before 1 PM ×2 (Wk 2 add, Wk 3 lineup), Wed 12-1 PM ×1 (Wk 2). Method: `created` on claims; other times inferred from commits, so approximate.

## Lessons
1. A pushed decision is not a transaction. Wk 1-2 claims never reached Sleeper; Wk 3's did once the file led with the deadline and Sean acted within 16 minutes. Every clipboard line carries a do-by. (Wk 1-3)
2. Never cite a live score as a result. Only completed matchups are quotable. (Wk 1, held Wk 2-3)
3. A contingency Sean cannot execute before the earliest lock is not a contingency; write the swap he can make. Wk 3: the Evans hedge went unused and Mumpfield outscored him by 6.90, so prefer the healthier body at the slot over the insured one. (Wk 2-3)
4. A free agent identified at noon is gone by morning. Free-agent lines say "do now". (Wk 2)
5. Sell surplus, not starters. (Wk 2)
6. Bench spots go to players who could start a specific slot on a specific Sunday. (Wk 1)
7. Never point a live trade and a live claim at the same player. (Wk 3)
8. One run, one answer. Wk 3's double-fire is the same fault at run level; the guard prevented two files, not two runs. (Wk 1, Wk 3)
9. An Out starter is a clipboard line the day it is known, not a paragraph in Detail. Daniels sat Out from Thursday; the paste line came Saturday afternoon. (Wk 3)

## Process review
- 2026-09-29, Week 3. Run history from the commit log only (no run-list tool in this session).
- **Data:** every decision cited a digest 4-30 minutes old; no Action fallback, no stale decision. Double-fire on Sun 9:00 AM (two full runs, one file; the guard held). The Tue waiver file landed 8:58 PM, nearly 3 h after the 6 PM slot; cause unknown without a run log, so watch it this Tuesday.
- **Decisions:** 11 graded rows. 5 Right, 2 Wrong (luck), 1 Wrong (process: Thu TNF hid the Daniels swap). Lost by 8.12; the optimal lineup (Mumpfield at FLEX) was worth 6.90, still short.
- **Handoff:** 12 Week 3 files, all in structure; 5 over 400 words excluding the clipboard (tue-waivers 1486, tue-trades 728, standdown 609, wed-review 424, thu-trades 421), the rest 295-395. Notifications unverifiable from the repo. Tue waiver file left 6 h to Do by, mostly Sean's evening.
- **Execution:** 3 of 3 claims filed within 16 minutes of the file, the first week without a miss.
- **Schedule:** one week of timing, so no slot moves. Saturday sweep wanted; needs routine tools and a second week.
- **Change 1** (2f477af): adopted `data/correspondence.md` into COMMON.
- **Change 2** (7c1c284): Thu TNF must paste a swap line for any Out or Doubtful starter.
- **Waiver time:** 3:14:05 (Sep 16) and 3:13:21 (Sep 23), 44 s apart, not the same minute. Not settled; Do by stays 3:00 AM.
- **Locked refusals:** none. The 400-word breaches (five files) are LOCKED item 4; nothing changed, the tasks already state the cap.

## Process changes
| Change | Date | Kill condition | Status |
|---|---|---|---|
| Every routine agent-owned; decision tasks guarded against double-firing | 2026-09-23 | A slot writes two decision files in one week, or a slot writes none because both skipped | active (Wk 3: two runs, one file, held) |
| Grading, ledger rewrite and lessons moved to a Tue 6:00 AM process review | 2026-09-23 | Two consecutive Tuesdays with the column running without a `## Process review` dated that day | active (Wk 3 review ran) |
| Correspondence log adopted into COMMON | 2026-09-29 | Two consecutive weeks where no run appends and no standing read changes a trade decision | active |
| Thu TNF pastes the swap for any Out or Doubtful starter | 2026-09-29 | A Thursday file with an Out/Doubtful starter and no swap line, or a swap issued for a player who then starts | active |
