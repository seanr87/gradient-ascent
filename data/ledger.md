# Ledger — Gradient Ascent working memory

Rewritten in full every Tuesday at 6:00 AM ET by the process review; `## State` and `## Open threads` updated by every decision run in the same commit as its decision. Hard cap 150 lines. Older weeks roll up; git history is the archive. Cite a thesis or lesson by name instead of re-arguing it.

Last full rewrite: 2026-10-20 (fourth process review, covering Week 6). Last touched: 2026-10-22 (Wk 7 trade scan).

## State
- **Week 6 final: lost 83.65 to Playful Secrets 100.97 (-17.32).** Record 2-4, 731.82 PF, 8th of 12. Week 7 opponent: **TheTroubles** (2-4, 624.06 PF, 10th). Waiver position **#5** (digest 2026-10-20 6:09 PM); it drifts, so re-read it every run.
- Roster (14), 2026-10-21 digest: QB Daniels; RB Irving, B. Allen, Vidal, Pierce; WR Lamb, Nacua, Vele, Coleman, Tucker; TE Kincaid [Q], Higbee; K Loop; DEF Buffalo. No IR slot. Waiver position **#9**. Stroud-for-Vele completed.
- Wk 6 lineup scored: Daniels 21.0, Allen 15.4, Lamb 13.5, Nacua 12.0, Buffalo 8.25, Irving 6.9, Loop 4.4, Higbee 2.2, Skattebo 0.0. Bench: Stroud 22.98, Pierce 15.0, Evans 12.4 (MNF), Kincaid 7.8, Vidal 6.5. Pierce at FLEX and Kincaid at TE alone is +20.6, a 3.3-point win.
- **Wk 7 claims resolved:** Coleman and Tucker cleared; Cooper lost to What can Brown do for u?; Douglas and Noel died with the wins and are free. The API log shows no waiver transactions, so results are read from rosters.
- **Waiver processing: measured 3:13-3:14 AM ET, not settled.** Sep 16 3:14:05, Sep 23 3:13:21, Sep 30 3:13:34, Oct 7 3:13:32, Oct 14 3:14:06. The 3:13 change was reverted 2026-10-20 (kill met), so every waiver Do by says **3:00 AM ET** again; claims filed by 7-8 PM Tuesday never come near either.
- Holes: none. WR five deep; QB2 is a wire move if Daniels is flagged.
- Chat targets used: Wk1 Three Wise Jaylens, Wk2 CorneliusJones, Wk3 Lost in the Land of Love, Princess Donut's Court (Wk 3 Mon), Playful Secrets (Wk 4 Mon), Sea Squirts (Wk 5 Mon), TheTroubles (Wk 6 Mon).

## Open threads
- **FLEX / TE for Week 7 is open.** FLEX is Pierce (61 of 64 Wk 6 snaps, 15.0) or Vidal (25 snaps, 6.5) unless a claim lands a receiver. TE is Higbee 2.2 vs Kincaid 7.8 [Q]; decide on measured touches (Lesson 3), not health.
- **QB is one deep once the trade lands.** Daniels only; he missed Wks 3-4. If he is flagged, stream from the wire — Rodgers 59.98, Murray, Geno Smith and Penix are all free — and the spot comes from the weakest back, not from a claim.
- **Trades are opt-in** (see Process changes). Wk 5, Wk 6 and Wk 7 scans: NO ACTION. Wk 7 reopens only if Daniels is flagged or Irving [Q] is ruled out with no RB on the wire.
- **Kincaid-for-Keenan-Allen: rejected by WCHolland 2026-10-17 12:53 PM** (transaction history, relayed 2026-10-20). Closed. Kincaid stays, TE is Higbee or Kincaid by matchup, the Allen note is deleted.
- **Sunday contingencies have no timed check.** Inactives routine retired 2026-10-20 (never created). Lineup file keeps its IF lines for Sean to check by eye. Skattebo's 0.0 is now answered: he played 6 snaps, healthy and unused.
- **Dropping Coleman and Meyers eight days after claiming them.** Lesson 6 test resolved against me; the column owes the correction. Coleman is re-claimed this week as chain A's fallback, which the column also owes.
- **Buffalo DEF.** Streaming is a free-agent move, never a claim.
- **Double-fire.** Sean still has to disable the seven UI routines in `SCHEDULED-TASKS.md`.
- **Daylight saving ends Sun 2026-11-01.** If Sleeper clears at a fixed UTC hour the ET time moves to 2:13 AM; re-measure Wk 9 (Nov 4).
- **Monday chat slot fires before MNF.** Cite only games with every starter finished.
- **League chat is unreadable by API.** `data/correspondence.md` holds the per-manager read.

## Theses
1. **Chain-movers over big plays.** Wk 1-3 supported; Wk 4 lost by 0.73 with Evans and Allen benched; Wk 5 supported: 158.66 against a league median of 130.03, with Nacua, Irving, Daniels and Evans over 25. Wk 6: 83.65 against a league median of 102.08, under (Daniels 21.0 only above 15). Kill: the healthy nine below league-median PF three weeks running (Wk 5 over reset it; Wk 6 is 1 of 3).
2. **Rushing QB over pocket QB.** Daniels 18.16, 17.24, 33.26 (Wk 5) against Stroud 21.94 on the bench; Mariota 20.92 in Wk 3. Wk 6: Daniels 21.0 vs Stroud 22.98, a wash. Kill, restated now Mariota is gone: Daniels under 10 twice while Stroud clears 18 in the same weeks.
3. **RETIRED 2026-10-06: trade WR for RB.** Four offers, zero acceptances (kill met Wk 3). Trades are now opt-in, see Process changes.
4. **Contested names first, winnable names last.** Held Wk 5: Stroud (mandatory) first, won at the first seq. Wk 6: Vidal, Pierce, Higbee all won in order, none contested away. Kill: losing a mandatory claim to order.
5. **Filed claims land; the channel is claims plus free agency.** Wk 5: 5 of 5 filed, 3 won; Wk 6: 5 of 5 filed, 3 won. Kill: three straight weeks with no claim won (Wk 3-6 each won one or more).
6. **Never roster two defenses or two kickers.** Kill: none expected.

## Scorecard
| Week | Call | Result | Grade |
|---|---|---|---|
| 1-2 (rolled up) | Wk 1: three off-file adds and a Johnson reversal, chat cited live scores (Wrong: process ×2), Hill/Waller Unknown. Wk 2: 5 claims never filed, FA pivot 1 of 3, Lamb-for-Taylor sold a top scorer (Wrong: process ×3); Kincaid/Buffalo Right, Nacua/Mumpfield hedge never made (Wrong: process), chat numbers held (Right) | 22 lines issued through Wk 2, 12 landed | 5 Right, 6 Wrong (process), 2 Unknown |
| 3 (rolled up) | Mariota claim won, Wilson/Mitchell lost on order, Taylor trade cancelled, Sat QB swap and Sun Nacua bench Right; Thu TNF swap missing until Sat (Wrong: process); Evans/Mumpfield hedge unused and Hockenson offer declined (Wrong: luck ×2); chat clean | 11 lines | 7 Right, 1 Wrong (process), 3 Wrong (luck) |
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
| 6 | Claims 1-3 Vidal, Pierce, Higbee | All cleared; Pierce 15.0 and Vidal 6.5 benched, Higbee 2.2 started | Right (claims); Pierce was the best claim and sat |
| 6 | Claims 4-5 Cooper, Goedert (backups) | Failed behind the wins, as designed | Right |
| 6 | Wed review: NO ACTION | Roster full, no better slot | Right |
| 6 | Thu scan: NO ACTION | Sea Squirts' ask would not change the nine | Right |
| 6 | Thu TNF: NO ACTION | No Seattle or Denver player on either roster | Right |
| 6 | Sat: decline five-for-one for Nacua | Nacua 12.0 as WR2; four cuts avoided | Right |
| 6 | Sat: counter Kincaid for K. Allen | No completed trade in the log; pending, unverifiable | Unknown |
| 6 | Sun: Daniels QB over Stroud | 21.0 vs 22.98 on the bench; 1.98 left, Thesis 2 | Right |
| 6 | Sun: Allen RB2 over Skattebo | 15.4 vs 0.0 | Right |
| 6 | Sun: Skattebo FLEX over Pierce, Evans, Vidal | 0.0 vs 15.0, 12.4, 6.5; 15.0 left, the loss was 17.32 | Wrong (process): Skattebo's 8.1 and 0.0 in two weeks was the signal, and the file passed on Pierce for a hamstring guess |
| 6 | Sun: Higbee TE over Kincaid | 2.2 vs 7.8; 5.6 left | Wrong (luck): 13 catches in two games was real volume |
| 6 | Sun: Irving, Lamb, Nacua, Loop, Buffalo | 6.9, 13.5, 12.0, 4.4, 8.25 | Right (healthy, no better option) |
| 6 | Sun: three IF-inactive contingencies | None verifiable; no inactives check ran | Unknown |
| 6 | Mon chat vs TheTroubles | Built on Wk 5 finals; no live score cited | Right |

## Execution
| Week | Run | Issued | Landed in Sleeper |
|---|---|---|---|
| 1-2 (rolled up) | all | 22 lines | 12 landed, 8 never reached the app, 2 unverifiable |
| 3 (rolled up) | all | 15 lines | 15 landed or n/a, 0 known misses, 4 unverifiable; claim latency 12-16 min; Sean acts Tue 9-10 PM ×5, Thu 8-9 AM, Sat 1-3 PM, Sun before 1 PM, Wed 12-1 PM (Wk 2) |
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
| 6 | Tue waivers (file 6:16 PM ET commit, digest 6:09) | 5 claims | 5 of 5 filed 8:04:57-8:06:21 PM ET, latency 1 h 49 m, 7 h 07 m before Do by; none overnight. 3 won, 2 failed behind them. Cleared 3:14:06 AM |
| 6 | Thu scan, Thu TNF | NO ACTION ×2 | n/a |
| 6 | Sat trade response (commit 12:42 PM ET) | decline + counter | Offer relayed 12:36 PM; decline and counter unverifiable in the API (pending offers do not log) |
| 6 | Sun lineup (commit 9:13 AM ET, front matter 9:20) | 9 slots, 3 contingencies | 9 of 9 match the starters; contingencies unverifiable. Latency n/a |
| 6 | Mon chat (commit 8:02 PM ET) | 1 | Unverifiable; 13 min before 8:15 PM Do by |
Wk 6: 18 lines (5 claims, 2 Sat, 9 lineup + 3 IF lines counted once, 1 chat), 0 known misses, 6 unverifiable. No run missed, no double-fire, no Action fallback.
Sean acts, Wk 6 added: Tue 8 PM ×5 claims (inside 90 seconds). Running tally: Tue 7-11 PM ×19, Thu 8-9 AM ×1, Sat 1-3 PM ×1, Sun before 1 PM ×2, Wed 12-1 PM ×1. Method: `created` on claims; other times inferred from commits.

## Lessons
1. A pushed decision is not a transaction. Wk 1-2 claims never reached Sleeper; Wk 3's did once the file led with the deadline and Sean acted within 16 minutes. Every clipboard line carries a do-by. (Wk 1-3)
2. Never cite a live score as a result. Only completed matchups are quotable. (Wk 1, held Wk 2-3)
3. A contingency Sean cannot execute before the earliest lock is not a contingency; write the swap he can make. Prefer the healthier body at the slot over the insured one (Wk 3: Mumpfield beat Evans by 6.90; Wk 5: Evans 25.3 over Addison 0.0). Health is not role: Allen 20.1 beat Skattebo 8.1 at RB2, so weigh recent volume too. Wk 6: Skattebo 0.0 at FLEX after 8.1, with Pierce 15.0 and Evans 12.4 benched; a starter with no measured touches in the file's own Why is a guess. (Wk 2-6)
4. A free agent identified at noon is gone by morning. Free-agent lines say "do now". (Wk 2)
5. Sell surplus, not starters. (Wk 2)
6. Bench spots go to players who could start a specific slot on a specific Sunday. (Wk 1)
7. Never point a live trade and a live claim at the same player. (Wk 3)
8. One run, one answer. Wk 3's double-fire is the same fault at run level; the guard prevented two files, not two runs. (Wk 1, Wk 3)
9. An Out starter is a clipboard line the day it is known, not a paragraph in Detail. Daniels sat Out from Thursday; the paste line came Saturday afternoon. (Wk 3)
10. Sean files claims in the evening after the 6 PM file: Wk 3 at 9-10 PM, Wk 4 at 11 PM, Wk 5 at 7 PM, never in the afternoon, always hours before the deadline. Wk 6 at 8 PM. Schedule asks for the evening. (Wk 3-6)

## Process review
- 2026-10-20, Week 6. Run history from the commit log only (no run-list tool, no `create_trigger` in this session).
- **Data:** every decision cited a digest 1-16 minutes old; no Action fallback, no stale decision, no double-fire, no missing slot. Front-matter times 7-9 minutes after commits (Tue, Sun); harmless.
- **Decisions:** 15 rows graded: 9 Right, 1 Right/split, 1 Wrong (luck), 1 Wrong (process), 2 Unknown. Lost 83.65-100.97; Skattebo 0.0 at FLEX with Pierce 15.0 benched, Higbee over Kincaid, 20.6 in all (Lesson 3).
- **Handoff:** 7 files, structure intact, Detail within 250. The Sat trade response ran 418 words excluding the clipboard (cap 400). Notifications unverifiable (no run log).
- **Execution:** 18 lines, 0 known misses. Claims filed 8:05 PM, 1 h 49 m after the file, 7 h 07 m before the deadline.
- **Schedule:** four weeks of timing: Sean acts Tue 7-11 PM and Sun morning, no miss; no slot moves.
- **Reverted (kill met):** waiver time 3:13 AM (b52872e): the Oct 14 clear was 3:14:06. Do by is 3:00 AM again.
- **Reverted (kill met):** Sun 11:30 inactives check (1deb638): never created, kill date passed. Task file is a pointer.
- **Waiver time:** Sep 16 3:14:05, Sep 23 3:13:21, Sep 30 3:13:34, Oct 7 3:13:32, Oct 14 3:14:06. The real clear is 3:13-3:14; 3:00 is a safe, unused buffer.
- **New changes:** none. Locked refusals: none.

## Process changes
| Change | Date | Kill condition | Status |
|---|---|---|---|
| Every routine agent-owned; decision tasks guarded against double-firing | 2026-09-23 | A slot writes two decision files in one week, or a slot writes none because both skipped | active (Wk 3-4: one file per slot, held) |
| Grading, ledger rewrite and lessons moved to a Tue 6:00 AM process review | 2026-09-23 | Two consecutive Tuesdays with the column running without a `## Process review` dated that day | active (Wk 3, 4 reviews ran) |
| Correspondence log adopted into COMMON | 2026-09-29 | Two consecutive weeks where no run appends and no standing read changes a trade decision | active |
| Thu TNF pastes the swap for any Out or Doubtful starter | 2026-09-29 | A Thursday file with an Out/Doubtful starter and no swap line, or a swap issued for a player who then starts | active |
| Trade scan opt-in: default NO ACTION, one proposal max, only to a manager who has replied | 2026-10-06 | A scan sends a proposal to a manager with no prior reply, or a trade is accepted and the scan missed it | active |
| Sun 11:30 AM ET inactives check, silent unless a contingency triggers (routine PENDING-TOOLS) | 2026-10-06 | It pushes on a week with no triggered contingency, or a triggered contingency goes unswapped, or the routine is still not created by 2026-10-20 | reverted 2026-10-20: never created, kill date passed (1deb638) |
| Waiver processing settled at Wed 3:13 AM ET; every waiver Do by says 3:13 AM | 2026-10-13 | A measured waiver clear outside 3:13:00-3:13:59 AM ET in the next 4 weeks (re-measure Nov 4, after daylight saving ends), or a claim filed before 3:13 that fails to process | reverted 2026-10-20: Oct 14 clear at 3:14:06 AM (b52872e); Do by is 3:00 AM until a rule that fits 3:13-3:14 is proposed |
