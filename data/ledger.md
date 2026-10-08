# Ledger — Gradient Ascent working memory

Rewritten in full every Tuesday at 6:00 AM ET by the process review; `## State` and `## Open threads` updated by every decision run in the same commit as its decision. Hard cap 150 lines. Older weeks roll up; git history is the archive. Cite a thesis or lesson by name instead of re-arguing it.

Last full rewrite: 2026-10-06 (second process review, covering Week 4). Last touched: 2026-10-08, Wk 5 Thursday call.

## State
- **Week 4 final: lost 114.74 to CorneliusJones 115.47 (0.73).** Record 1-3, 489.51 PF, 10th of 12. Week 5 opponent: **Umojan Protectorate** (3-1, 500.03 PF). Waiver position **#12** after winning Wk 5 claims (resets after Wk 5 results).
- Roster (14), confirmed in the 2026-10-07 16:13 UTC digest: QB Stroud, Daniels [Q, elbow]; RB Irving, Skattebo, B. Allen; WR Lamb, Addison, Nacua, Coleman, Meyers, Evans; TE Kincaid; K Loop; DEF Buffalo. Mariota, J. Hill, Mumpfield dropped.
- **Wk 5 claims: 3 of 5 cleared** (Stroud, Coleman, Meyers); Cousins and Watson cancelled by Stroud's win, as designed. Wed review: NO ACTION, no pivot.
- **Sleeper lineup shows no QB starter set** (Stroud and Daniels both unflagged as starters); the Sun lineup run must name one.
- **Wk 5 Thu (TB at DAL, 8:15 PM ET): Irving (RB) and Lamb (WR) started, no FLEX locked.** Inactives not found; Skattebo, Addison, Evans all Questionable for Sunday.
- Holes: none; roster full with 5 bench, no IR.
- Chat targets used: Wk1 Three Wise Jaylens, Wk2 CorneliusJones, Wk3 Lost in the Land of Love, Princess Donut's Court (Wk 3 Mon), Playful Secrets (Wk 4 Mon).

## Open threads
- **QB: Stroud starts unless Daniels is cleared.** Daniels Questionable (elbow, braced, no surgery); Sun lineup decides Stroud vs Daniels at practice reports (Thesis 2: Daniels preferred if healthy).
- **Coleman and Meyers (cleared Wk 5).** Both FLEX candidates against Addison and Evans (Lesson 3); Sun lineup decides with Evans' and Allen's Wk 4 benched scores in mind.
- **Thu look: Roman Wilson (WR-PIT), Romeo Doubs (WR-NE), Higbee (TE-LAR), all free.** Only if a bench spot opens; none is droppable today.
- **Trades are opt-in as of 2026-10-06** (Thesis 3 retired; see Process changes). Wk 5 scan: NO ACTION, nothing sent. Revisit if a starter is lost or Stroud/Daniels becomes surplus while Princess Donut's Court is short at QB.
- **Sun 11:30 AM ET inactives check: routine PENDING-TOOLS.** Create it with cron `CRON_TZ=America/New_York 30 11 * * 0` and the standard bootstrap prompt for `tasks/climb-sun-inactives-check.md`.
- **B. Allen (RB-NYJ), claimed Wk 4.** FLEX candidate while Hall is out; unwinds when Hall returns.
- **Waiver clock: Wk 5 measured at 3:13:32 AM ET** (`status_updated` 1791357212169, shared by all nine waiver rows, read from `/league/<id>/transactions/4` — the clears are filed under leg 4, which is why the digest's leg-5 list shows only a free-agent move). Four measurements now: 3:14:05, 3:13:21, 3:13:34, 3:13:32. The app says 3:05; the log says 3:13. Tue review to settle; Do by stays 3:00 AM until it does.
- **Buffalo DEF.** Streaming is a free-agent move, never a claim.
- **Double-fire.** Sean still has to disable the seven UI routines in `SCHEDULED-TASKS.md`.
- **Fri/Sat blind spot.** Thu TNF pastes the swap for an Out starter.
- **Monday chat slot fires before MNF.** Cite only games with every starter finished.
- **League chat is unreadable by API.** `data/correspondence.md` holds the per-manager read.

## Theses
1. **Chain-movers over big plays.** Wk 1-3 supported; Wk 4: lost by 0.73 with Evans (12.10) and Allen (9.70) benched, per-player points not in the digest. Kill: the healthy nine below league-median PF three weeks running (Wk 3 116.72, Wk 4 114.74, both under the median; Wk 5 under median means the kill is met).
2. **Rushing QB over pocket QB.** Daniels 18.16, 17.24; Mariota 20.92 in Wk 3. Wk 4 Mariota unknown. Kill: Mariota under 10 twice while Stroud clears 18 in the same weeks.
3. **RETIRED 2026-10-06: trade WR for RB.** Four offers, zero acceptances (kill met Wk 3). Trades are now opt-in, see Process changes.
4. **Contested names first, winnable names last.** Held again Wk 4: Gordon (first) lost to waiver #1, Allen (second) won. Kill: losing a mandatory claim to order.
5. **Filed claims land; the channel is claims plus free agency.** Wk 4: 4 of 4 filed, 1 won (Allen at seq 3). Kill: three straight weeks with no claim won (Wk 3 yes, Wk 4 yes).
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
| 4 | Claim 1 Gordon (RB-MIA, first) | Lost at seq 2 to The Wizard's Apprentice (waiver #1, seq 1) | Wrong (luck) |
| 4 | Claim 2 B. Allen, backup to 1 | Cleared seq 3 3:13:34 AM; 9.70 on bench | Right |
| 4 | Claims 3-4 Raymond, K. Allen (backups) | Cancelled by Allen's win, as designed | Right |
| 4 | Wed review: NO ACTION, no pivot | Roster full, no free slot starter | Right |
| 4 | Thu scan: Mumpfield for Kamara to dlef24 | No transaction, no reply relayed; sent unverifiable | Unknown |
| 4 | Thu TNF: NO ACTION | No rostered or starting Thursday players | Right |
| 4 | Sun: Mariota QB, Nacua WR2, Addison FLEX, Evans benched | Lost by 0.73; Evans 12.10 and Allen 9.70 benched, Addison and starter points not in the digest | Unknown (Addison under 11.37 would make this Wrong (process) vs Lesson 3) |
| 4 | Mon chat vs Playful Secrets | Final 123.78 vs 132.31 matches the digest; no live scores cited | Right |

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
Sean acts (through Wk 3): Tue 9-10 PM ×5 (2 trades Wk 3, 3 claims Wk 3), Thu 8-9 AM ×1, Sat 1-3 PM ×1 (QB), Sun before 1 PM ×2 (Wk 2 add, Wk 3 lineup), Wed 12-1 PM ×1 (Wk 2). Method: `created` on claims; other times inferred from commits, so approximate.
| 4 | Tue waivers (file 6:14 PM ET) | 4 claims | 4 of 4 filed 11:10-11:11 PM ET, latency 4 h 56 m, 3 h 49 m before Do by (3:00 AM) |
| 4 | Thu trades (file 8:12 AM ET) | 1 offer | No trade in Sleeper; sent unverifiable, no acceptance |
| 4 | Thu TNF | NO ACTION | n/a |
| 4 | Sun lineup (file 9:13 AM ET) | 9 slots, 2 contingencies | 9 of 9 match the digest's current starters (no lock-time view in the API); contingency unverifiable |
| 4 | Mon chat | 1 | Unverifiable |
Wk 4: 15 lines, 0 known misses, 3 unverifiable. Claim latency 4 h 56 m after a 3-minute-to-file week 3 pace; the file was on time (6:14 PM) but Sean filed at 11:10 PM.
Sean acts, Wk 4 added: Tue 11 PM ×4 claims (all inside 1 minute). Running tally: Tue 9-11 PM ×9, Thu 8-9 AM ×1, Sat 1-3 PM ×1, Sun before 1 PM ×2, Wed 12-1 PM ×1.

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
10. A deadline an hour before bed is the one Sean meets: Wk 3 and 4 claims landed at 9-11 PM, hours after a 6 PM file, never in the afternoon. Schedule asks for the evening. (Wk 3-4)

## Process review
- 2026-10-06, Week 4. Run history from the commit log only (no run-list tool; no `create_trigger` in this session).
- **Data:** every decision cited a digest 5-16 minutes old; no Action fallback, no stale decision, no double-fire, no missing slot. Tue waiver file landed 6:14 PM, on slot (Wk 3 was 3 h late).
- **Decisions:** 8 rows graded: 5 Right, 1 Wrong (luck), 2 Unknown. Lost by 0.73; Evans and Allen on the bench both beat the margin, but the Addison-vs-Evans FLEX call cannot be graded without per-player points.
- **Handoff:** 6 files, all in structure; 2 over 400 words excluding the clipboard (wed-review 424, tue-waivers 402), the rest 143-335; Detail within 250. Notifications unverifiable.
- **Execution:** 4 of 4 claims filed within a minute, 4 h 56 m after the file; no known miss, 3 lines unverifiable (trade offer, chat, contingency).
- **Schedule:** two weeks of timing: Sean acts Tue 9-11 PM and Sun morning; no miss cluster, so no slot moves.
- **Change 1** (24ded57): trades opt-in, default NO ACTION, one proposal max, only to a manager who has replied. Answers Sean's Wk 4 request.
- **Change 2** (663f1a2): Sun 11:30 AM ET inactives check, silent unless a contingency triggers. Routine PENDING-TOOLS. Answers Sean's Wk 4 request.
- **Waiver time:** 3:14:05, 3:13:21, 3:13:34 (Sep 16/23/30), all 3:13-3:14, never 3:05. Last two agree to the minute but the first does not; one more clean week settles it. Do by stays 3:00 AM.
- **Locked refusals:** none; the two 400-word overruns are LOCKED item 4, tasks already state the cap.

## Process changes
| Change | Date | Kill condition | Status |
|---|---|---|---|
| Every routine agent-owned; decision tasks guarded against double-firing | 2026-09-23 | A slot writes two decision files in one week, or a slot writes none because both skipped | active (Wk 3-4: one file per slot, held) |
| Grading, ledger rewrite and lessons moved to a Tue 6:00 AM process review | 2026-09-23 | Two consecutive Tuesdays with the column running without a `## Process review` dated that day | active (Wk 3, 4 reviews ran) |
| Correspondence log adopted into COMMON | 2026-09-29 | Two consecutive weeks where no run appends and no standing read changes a trade decision | active |
| Thu TNF pastes the swap for any Out or Doubtful starter | 2026-09-29 | A Thursday file with an Out/Doubtful starter and no swap line, or a swap issued for a player who then starts | active |
| Trade scan opt-in: default NO ACTION, one proposal max, only to a manager who has replied | 2026-10-06 | A scan sends a proposal to a manager with no prior reply, or a trade is accepted and the scan missed it | active |
| Sun 11:30 AM ET inactives check, silent unless a contingency triggers (routine PENDING-TOOLS) | 2026-10-06 | It pushes on a week with no triggered contingency, or a triggered contingency goes unswapped, or the routine is still not created by 2026-10-20 | active (pending creation) |
