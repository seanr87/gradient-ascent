# Ledger — Gradient Ascent working memory

Rewritten in full every Tuesday at 6:00 AM ET by the process review; `## State` and `## Open threads` updated by every decision run in the same commit as its decision. Hard cap 150 lines. Older weeks roll up; git history is the archive. Cite a thesis or lesson by name instead of re-arguing it.

Last full rewrite: 2026-10-13 (third process review, covering Week 5). Last touched: 2026-10-17 (Wk 6 Saturday trade response).

## State
- **Week 5 final: won 158.66 to Umojan Protectorate 151.04 (7.62).** Record 2-3, 648.17 PF, 7th of 12. Week 6 opponent: **Playful Secrets** (4-1, 677.27 PF, #1). Waiver position **#12** (digest 2026-10-15, after the Wk 6 claims cleared).
- Roster (14), confirmed in the 2026-10-14 digest: QB Stroud, Daniels; RB Irving, Skattebo, B. Allen, Vidal, Pierce; WR Lamb [Q], Nacua, Evans; TE Kincaid, Higbee; K Loop; DEF Buffalo.
- Wk 5 lineup scored: Nacua 33.7, Daniels 33.26, Irving 33.0, Evans 25.3 (FLEX), Loop 14.2, Skattebo 8.1, Buffalo 6.0, Kincaid 3.2, Lamb 1.9. Bench: Stroud 21.94, Allen 20.1, Coleman 7.2, Meyers 2.7, Addison 0.0.
- **Waiver processing settled: Wed 3:13 AM ET** (Process changes). Every waiver Do by says 3:13 AM.
- Waiver position is **#10** in the 2026-10-17 digest, not the #12 recorded Wednesday; it drifts with other teams' claims, so re-read it every run rather than trusting the ledger.
- **2026-10-17, first inbound trade offer of the season.** WCHolland (The Wizard's Apprentice, 1-4) offered his whole five-man bench for Puka Nacua. Declined: 14 of 14 roster spots, no IR slot, so four of mine get cut to fit. Countered Kincaid for Keenan Allen.
- Holes: none. Wk 6 claims 1-3 all cleared (Vidal, Pierce, Higbee); 4-5 cancelled. Wed review: NO ACTION, no pivot.
- Chat targets used: Wk1 Three Wise Jaylens, Wk2 CorneliusJones, Wk3 Lost in the Land of Love, Princess Donut's Court (Wk 3 Mon), Playful Secrets (Wk 4 Mon), Sea Squirts (Wk 5 Mon), TheTroubles (Wk 6 Mon).

## Open threads
- **Wk 6 Sun lineup (2026-10-18):** Daniels, Irving, Allen, Lamb, Nacua, Higbee, FLEX Skattebo, Loop, Buffalo. Evans (Q, Achilles, MNF) benched; Daniels is MNF with no fallback (Stroud locks 9:30 AM London).
- **RB2 / FLEX resolved Wk 6:** Allen RB2 (Hall out 3rd game), Skattebo FLEX. Grade after the games; Vidal and Pierce are the bench RBs.
- **QB: Daniels starts, Stroud is the bench hedge.** Revisit if Daniels is flagged; one of the two is surplus if a QB-short manager engages. WCHolland rosters exactly one QB (Prescott) and is the better target than Princess Donut's Court, who roster three; not sold the day before a Sunday.
- **Trades are opt-in** (see Process changes). Wk 5 and Wk 6 scans: NO ACTION. Revisit if a starter is lost.
- **Kincaid-for-Keenan-Allen counter sent to WCHolland 2026-10-17, pending.** Unwinds if he declines or does not answer by the Thu Wk 7 scan; if it lands, Kincaid is gone and Higbee is the only TE, and Sunday weighs Allen against Evans at FLEX. Notes.yml carries an Allen line that is an orphan until it clears.
- **Sun 11:30 AM ET inactives check: routine still PENDING-TOOLS, absent from the commit log.** Create it with cron `CRON_TZ=America/New_York 30 11 * * 0` and the standard bootstrap prompt for `tasks/climb-sun-inactives-check.md`. Kill date 2026-10-20.
- **Contingency, check 11:30 AM-12:30 PM ET:** Allen, Skattebo or Irving inactive → Vidal in his slot; second absence → Pierce (1:00 PM lock).
- **Contingency, check 3:30 PM ET:** Higbee inactive → Kincaid at TE (Higbee locks 4:05, Kincaid 4:25). Pierce hinges on Barkley's hamstring.
- **TE:** Higbee starts over Kincaid in Wk 6; if the Kincaid counter lands, Higbee is the only TE.
- **Dropping Coleman and Meyers eight days after claiming them.** Lesson 6 test from Wk 5 resolved against me; the column owes the correction.
- **Buffalo DEF.** Streaming is a free-agent move, never a claim.
- **Double-fire.** Sean still has to disable the seven UI routines in `SCHEDULED-TASKS.md`.
- **Daylight saving ends Sun 2026-11-01.** If Sleeper clears waivers at a fixed UTC hour, the ET time moves to 2:13 AM; re-measure Wk 9 (Nov 4) before trusting 3:13.
- **Monday chat slot fires before MNF.** Cite only games with every starter finished.
- **League chat is unreadable by API.** `data/correspondence.md` holds the per-manager read.

## Theses
1. **Chain-movers over big plays.** Wk 1-3 supported; Wk 4 lost by 0.73 with Evans and Allen benched; Wk 5 supported: 158.66 against a league median of 130.03, with Nacua, Irving, Daniels and Evans over 25. Kill: the healthy nine below league-median PF three weeks running (Wk 3 and 4 under, Wk 5 over; reset).
2. **Rushing QB over pocket QB.** Daniels 18.16, 17.24, 33.26 (Wk 5) against Stroud 21.94 on the bench; Mariota 20.92 in Wk 3. Kill, restated now Mariota is gone: Daniels under 10 twice while Stroud clears 18 in the same weeks.
3. **RETIRED 2026-10-06: trade WR for RB.** Four offers, zero acceptances (kill met Wk 3). Trades are now opt-in, see Process changes.
4. **Contested names first, winnable names last.** Held Wk 5: Stroud (mandatory) first, won at the first seq. Kill: losing a mandatory claim to order.
5. **Filed claims land; the channel is claims plus free agency.** Wk 5: 5 of 5 filed, 3 won. Kill: three straight weeks with no claim won (Wk 3, 4, 5 each won one or more).
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
| 5 | Claim 1 Stroud (QB, mandatory, first) | Filed 6:59:38 PM; cleared seq 1 at 3:13:32 AM; Daniels cleared Sun so he scored 21.94 on the bench | Right |
| 5 | Claims 2-3 Cousins, Watson (backups) | Cancelled by Stroud's win, as designed | Right |
| 5 | Claims 4-5 Coleman, Meyers | Both cleared from #12; 7.2 and 2.7 on the bench, neither on a start path | Unknown (no start yet; Lesson 6 test pending) |
| 5 | Wed review: NO ACTION | Roster full; ledger heading had to be repaired in a follow-up commit | Right (call); Wrong (process) on the ledger edit |
| 5 | Thu scan: NO ACTION | No hole a one-for-one fixes; none sent | Right |
| 5 | Thu TNF: START Irving, START Lamb | Irving 33.0; Lamb 1.9 | Right (Irving); Wrong (luck) (Lamb) |
| 5 | Sun: Daniels QB over Stroud | 33.26 vs 21.94 | Right |
| 5 | Sun: Evans FLEX over Addison, Allen, Coleman | Evans 25.3 vs Allen 20.1, Coleman 7.2, Addison 0.0 | Right |
| 5 | Sun: Skattebo RB2 over Allen | 8.1 vs 20.1 on the bench; 12.0 left, the win margin was 7.62 | Wrong (luck): Skattebo healthy; Lesson 3 addendum |
| 5 | Sun: Nacua, Irving, Loop, Kincaid, Buffalo; both contingencies | 33.7, 33.0, 14.2, 3.2, 6.0; neither contingency triggered | Right |
| 5 | Mon chat vs Sea Squirts | Final 158.80 vs 116.76 matches the digest; every starter finished, no live score cited | Right |

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
| 5 | Tue waivers (file 6:19 PM ET, digest 6:10) | 5 claims | 5 of 5 filed 6:59:38-7:00:29 PM ET, latency 41 min, 8 h 13 m before Do by (3:13); no overnight time |
| 5 | Thu trades (file 8:11 AM ET) | NO ACTION | n/a |
| 5 | Thu TNF (file 5:08 PM ET) | 2 START lines | Irving and Lamb are starters at lock; latency n/a; 3 h 07 m before 8:15 PM, none overnight |
| 5 | Sun lineup (file 9:13 AM ET, front matter says 9:25) | 9 slots, 2 contingencies | 9 of 9 match the starters; contingencies not triggered. Latency n/a |
| 5 | Mon chat (file 8:02 PM ET, front matter says 8:08) | 1 | Unverifiable; 7-13 min before the 8:15 PM Do by |
Wk 5: 15 lines, 0 known misses, 1 unverifiable. Fastest claim latency yet (41 min). The Wk 5 Wed edit broke the ledger heading (repair commit 32e29d0).
Sean acts, Wk 5 added: Tue 7 PM ×5 claims (inside 1 minute). Running tally: Tue 7-11 PM ×14, Thu 8-9 AM ×1, Sat 1-3 PM ×1, Sun before 1 PM ×2, Wed 12-1 PM ×1. Method: `created` on claims; other times inferred from commits.

## Lessons
1. A pushed decision is not a transaction. Wk 1-2 claims never reached Sleeper; Wk 3's did once the file led with the deadline and Sean acted within 16 minutes. Every clipboard line carries a do-by. (Wk 1-3)
2. Never cite a live score as a result. Only completed matchups are quotable. (Wk 1, held Wk 2-3)
3. A contingency Sean cannot execute before the earliest lock is not a contingency; write the swap he can make. Prefer the healthier body at the slot over the insured one (Wk 3: Mumpfield beat Evans by 6.90; Wk 5: Evans 25.3 over Addison 0.0). Health is not role: Allen 20.1 beat Skattebo 8.1 at RB2, so weigh recent volume too. (Wk 2-5)
4. A free agent identified at noon is gone by morning. Free-agent lines say "do now". (Wk 2)
5. Sell surplus, not starters. (Wk 2)
6. Bench spots go to players who could start a specific slot on a specific Sunday. (Wk 1)
7. Never point a live trade and a live claim at the same player. (Wk 3)
8. One run, one answer. Wk 3's double-fire is the same fault at run level; the guard prevented two files, not two runs. (Wk 1, Wk 3)
9. An Out starter is a clipboard line the day it is known, not a paragraph in Detail. Daniels sat Out from Thursday; the paste line came Saturday afternoon. (Wk 3)
10. Sean files claims in the evening after the 6 PM file: Wk 3 at 9-10 PM, Wk 4 at 11 PM, Wk 5 at 7 PM, never in the afternoon, always hours before the deadline. Schedule asks for the evening. (Wk 3-5)

## Process review
- 2026-10-13, Week 5. Run history from the commit log only (no run-list tool; no `create_trigger` in this session).
- **Data:** every decision cited a digest 1-9 minutes old; no Action fallback, no stale decision, no double-fire, no missing slot. Two front-matter times are 6-12 minutes later than their commits (Sun, Mon); harmless.
- **Decisions:** 11 rows graded: 6 Right, 1 Right/Wrong split, 2 Wrong (luck), 1 Unknown. Won 158.66-151.04. Skattebo at RB2 left 12.0 on the bench (Allen 20.1 vs 8.1); Daniels over Stroud and Evans at FLEX were right.
- **Handoff:** 6 files, structure intact, Detail within 250; the Tue waiver file ran 406 words excluding the clipboard (item 4 cap, task already states it). Notifications unverifiable. Wed review edit broke the ledger heading and needed a repair commit.
- **Execution:** 15 lines, 0 known misses. Claims filed 41 minutes after the 6:19 PM file (7:00 PM), 8 h 13 m before the deadline, none overnight.
- **Schedule:** three weeks of timing: Sean acts Tue 7-11 PM and Sun morning, no miss; no slot moves. Sun inactives routine still not created (kill date 2026-10-20).
- **Change 1** (057afef): waiver processing settled at Wed 3:13 AM ET; every file stating a time corrected; Do by now 3:13.
- **Waiver time:** Sep 16 3:14:05, Sep 23 3:13:21, Sep 30 3:13:34, Oct 7 3:13:32. Last three agree to the minute; the 3:05 on Sleeper's screen is not the processing time.
- **Locked refusals:** none.

## Process changes
| Change | Date | Kill condition | Status |
|---|---|---|---|
| Every routine agent-owned; decision tasks guarded against double-firing | 2026-09-23 | A slot writes two decision files in one week, or a slot writes none because both skipped | active (Wk 3-4: one file per slot, held) |
| Grading, ledger rewrite and lessons moved to a Tue 6:00 AM process review | 2026-09-23 | Two consecutive Tuesdays with the column running without a `## Process review` dated that day | active (Wk 3, 4 reviews ran) |
| Correspondence log adopted into COMMON | 2026-09-29 | Two consecutive weeks where no run appends and no standing read changes a trade decision | active |
| Thu TNF pastes the swap for any Out or Doubtful starter | 2026-09-29 | A Thursday file with an Out/Doubtful starter and no swap line, or a swap issued for a player who then starts | active |
| Trade scan opt-in: default NO ACTION, one proposal max, only to a manager who has replied | 2026-10-06 | A scan sends a proposal to a manager with no prior reply, or a trade is accepted and the scan missed it | active |
| Sun 11:30 AM ET inactives check, silent unless a contingency triggers (routine PENDING-TOOLS) | 2026-10-06 | It pushes on a week with no triggered contingency, or a triggered contingency goes unswapped, or the routine is still not created by 2026-10-20 | active (pending creation; still absent Wk 5) |
| Waiver processing settled at Wed 3:13 AM ET; every waiver Do by says 3:13 AM | 2026-10-13 | A measured waiver clear outside 3:13:00-3:13:59 AM ET in the next 4 weeks (re-measure Nov 4, after daylight saving ends), or a claim filed before 3:13 that fails to process | active |
