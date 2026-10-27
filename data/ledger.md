# Ledger — Gradient Ascent working memory

Rewritten in full every Tuesday at 6:00 AM ET by the process review; `## State` and `## Open threads` updated by every decision run in the same commit as its decision. Hard cap 150 lines. Older weeks roll up; git history is the archive. Cite a thesis or lesson by name instead of re-arguing it.

Last full rewrite: 2026-10-27 (fifth process review, covering Week 7). Last touched: 2026-10-27.

## State
- **Week 7 final: won 125.78 to TheTroubles 29.05 (+96.73).** Record 3-4, 857.85 PF, 8th of 12. Week 8 opponent: **Princess Donut's Court** (5-2, 929.08 PF, 1st). Waiver position **#5** (digest 2026-10-27 22:03 UTC); it drifts, so re-read it every run.
- Roster (14), 2026-10-27 digest: QB Rodgers, Daniels; RB Irving, B. Allen, Pierce; WR Lamb, Nacua, Vele, Coleman, Tucker; TE Higbee, Kincaid [Q]; K Loop; DEF Buffalo (back from bye in Wk 8). **Vele on a Wk 8 bye (NO).** Holes: none; QB is two deep again.
- Wk 7 lineup scored: Irving 27.5, Lamb 23.4, Allen 19.4, Nacua 18.8, Rodgers 13.58, Pierce 12.8, Loop 7.4, Higbee 2.9, Buffalo 0.0 (bye, swap never made). Bench: Tucker 20.3, Vele 15.4, Daniels/Kincaid/Coleman 0.0. League median 116.78.
- **Waiver processing: measured 3:13-3:14 AM ET, not settled.** Sep 16 3:14:05, Sep 23 3:13:21, Sep 30 3:13:34, Oct 7 3:13:32, Oct 14 3:14:06, Oct 21 3:14:21. Six weeks, split 3:13 / 3:14, so no to-the-minute rule; every waiver Do by says **3:00 AM ET**. Claims on just-dropped players cleared on their own clock (Fri Oct 23 2:23:50 AM ET).
- Chat targets used: Wk1 Three Wise Jaylens, Wk2 CorneliusJones, Wk3 Lost in the Land of Love, Princess Donut's Court (Wk 3 Mon), Playful Secrets (Wk 4 Mon), Sea Squirts (Wk 5 Mon), TheTroubles (Wk 6 Mon), What can Brown do for u? (Wk 7 Mon).

## Open threads
- **Wk 8 is Princess Donut's Court, the league's top scorer.** No trade or hedge open. Buffalo DEF and Daniels are back from the bye; the DEF stream is a waiver claim this week, not a Sunday line (Lesson 4).
- **Kincaid [Q] ribs.** TE is Higbee or Kincaid by measured touches; Higbee scored 2.9 on a bye-week-free Wk 7.
- **Trades are opt-in** (see Process changes). Wk 5, 6 and 7 scans: NO ACTION. The Stroud-for-Vele accept (Wk 7 Tue) closed itself; SpaceElf is not buying again.
- **Sunday contingencies have no timed check.** Lineup file keeps its IF lines for Sean to check by eye; Wk 7's Nacua IF never triggered.
- **Sunday free-agent ADD/DROP pairs.** Wk 7's Tampa Bay swap was the one line that missed (see Execution, Lesson 4). Next Sunday file puts the DEF line only if the roster actually needs it, and says what the slot scores without it.
- **Dropping Coleman and Meyers eight days after claiming them.** Lesson 6 test resolved against me; Coleman was re-claimed and cleared Wk 7 (0.0, on his bye). The column owes the correction.
- **Double-fire.** Sean still has to disable the seven UI routines in `SCHEDULED-TASKS.md`; no double-fire seen in Wk 7.
- **Daylight saving ends Sun 2026-11-01.** If Sleeper clears at a fixed UTC hour the ET time moves to 2:13 AM; re-measure Wk 9 (Nov 4).
- **Monday chat slot fires before MNF.** Cite only games with every starter finished; Wk 7's file landed 4 minutes before the Do by.
- **League chat is unreadable by API.** `data/correspondence.md` holds the per-manager read.
- **Wk 8 claims filed: 5 in 3 chains.** Tampa Bay then Green Bay over Buffalo DEF; Pitts then Mason Taylor over Higbee; Bass over Loop. Unwinds at Wednesday's review; a chain that loses both leaves the incumbent and needs a Wednesday pivot.
- **Rodgers kept as Daniels' only QB cover.** Unwinds the moment the spot buys a starter; five free QBs outscored him over Wk 5-7, so the wire is the backstop.

## Theses
1. **Chain-movers over big plays.** Wk 1-3 supported; Wk 4 lost by 0.73; Wk 5 supported (158.66 vs median 130.03); Wk 6 under (83.65 vs 102.08); Wk 7 supported: 125.78 vs median 116.78, with Irving 27.5 and Lamb 23.4 over 20. Kill: the healthy nine below league-median PF three weeks running (Wk 7 over reset it).
2. **Rushing QB over pocket QB.** Daniels 18.16, 17.24, 33.26 (Wk 5); Wk 6 21.0 vs Stroud 22.98, a wash; Wk 7 untested (Daniels on a bye, Rodgers 13.58). Stroud now plays for The Butker Jihad. Kill: Daniels under 10 twice while the streamed QB clears 18 in the same weeks.
3. **RETIRED 2026-10-06: trade WR for RB.** Four offers, zero acceptances (kill met Wk 3). Trades are now opt-in, see Process changes.
4. **Contested names first, winnable names last.** Wk 5 Stroud first, won; Wk 6 all won in order; Wk 7 Cooper first, lost to waiver order (not a mandatory claim), Tucker and Coleman won behind it. Kill: losing a mandatory claim to order.
5. **Filed claims land; the channel is claims plus free agency.** Wk 7: 5 of 5 filed within 3 minutes of the file, 2 won, 3 failed behind wins as designed. Kill: three straight weeks with no claim won (Wk 3-7 each won one or more).
6. **Never roster two defenses or two kickers.** Kill: none expected.

## Scorecard
| Week | Call | Result | Grade |
|---|---|---|---|
| 1-2 (rolled up) | Wk 1: three off-file adds and a Johnson reversal, chat cited live scores (Wrong: process ×2), Hill/Waller Unknown. Wk 2: 5 claims never filed, FA pivot 1 of 3, Lamb-for-Taylor sold a top scorer (Wrong: process ×3); Kincaid/Buffalo Right, Nacua/Mumpfield hedge never made (Wrong: process), chat numbers held (Right) | 22 lines issued through Wk 2, 12 landed | 5 Right, 6 Wrong (process), 2 Unknown |
| 3 (rolled up) | Mariota claim won, Wilson/Mitchell lost on order, Taylor trade cancelled, Sat QB swap and Sun Nacua bench Right; Thu TNF swap missing until Sat (Wrong: process); Evans/Mumpfield hedge unused and Hockenson offer declined (Wrong: luck ×2); chat clean | 11 lines | 7 Right, 1 Wrong (process), 3 Wrong (luck) |
| 4 (rolled up) | Gordon claim lost on order, B. Allen won, backups cancelled as designed, Wed and Thu NO ACTION, Mon chat clean; Sun lineup lost by 0.73 with Evans and Allen benched; Mumpfield offer unverifiable | 9 rows | 5 Right, 1 Wrong (luck), 2 Unknown |
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
| 7 | Claims 1-3 Cooper, Tucker, Coleman | Cooper lost on order (5 teams claimed him), Tucker (20.3) and Coleman (0.0, bye) won in chain; Evans and Skattebo out | Right |
| 7 | Claims 4-5 Douglas, Noel (backups) | Failed behind the wins, as designed | Right |
| 7 | Tue: accept Vele for Stroud | Vele 15.4 on the bench; WR five deep, Stroud was a QB2 | Right |
| 7 | Wed review: NO ACTION | Roster full; Tucker 20.3 left on the bench by Sun, not a Wed call | Right |
| 7 | Thu scan: NO ACTION | No gap a one-for-one fills | Right |
| 7 | Thu: ADD Rodgers / DROP Vidal, QB Rodgers | Landed 54 s after the file; Rodgers 13.58 with Daniels on a bye | Right |
| 7 | Sun: ADD Tampa Bay / DROP Buffalo | Never made; Buffalo scored 0.0 on its bye | Wrong (process): sound call, never executed (Lesson 4) |
| 7 | Sun: Rodgers, Irving, Allen, Lamb, Nacua, Higbee, Loop | 13.58, 27.5, 19.4, 23.4, 18.8, 2.9, 7.4; Nacua IF never triggered | Right |
| 7 | Sun: Pierce FLEX over Tucker, Vele | 12.8 vs 20.3 and 15.4; 7.5 left, margin was 96.73 | Wrong (luck): Pierce's 61-of-64 snaps were the signal |
| 7 | Mon chat vs What can Brown do for u? | Wk 6 final 89.97 vs 106.29 matches the matchups API; no live score cited | Right |

## Execution
| Week | Run | Issued | Landed in Sleeper |
|---|---|---|---|
| 1-2 (rolled up) | all | 22 lines | 12 landed, 8 never reached the app, 2 unverifiable |
| 3 (rolled up) | all | 15 lines | 15 landed or n/a, 0 known misses, 4 unverifiable; claim latency 12-16 min; Sean acts Tue 9-10 PM ×5, Thu 8-9 AM, Sat 1-3 PM, Sun before 1 PM, Wed 12-1 PM (Wk 2) |
| 4 (rolled up) | all | 15 lines | 0 known misses, 3 unverifiable; claims filed 11:10 PM, latency 4 h 56 m; Thu offer unverifiable |
| 5 | Tue waivers (file 6:19 PM ET, digest 6:10) | 5 claims | 5 of 5 filed 6:59:38-7:00:29 PM ET, latency 41 min, 8 h 13 m before Do by (3:13); no overnight time |
| 5 | Thu trades (file 8:11 AM ET) | NO ACTION | n/a |
| 5 | Thu TNF (file 5:08 PM ET) | 2 START lines | Irving and Lamb are starters at lock; latency n/a; 3 h 07 m before 8:15 PM, none overnight |
| 5 | Sun lineup (file 9:13 AM ET, front matter says 9:25) | 9 slots, 2 contingencies | 9 of 9 match the starters; contingencies not triggered. Latency n/a |
| 5 | Mon chat (file 8:02 PM ET, front matter says 8:08) | 1 | Unverifiable; 7-13 min before the 8:15 PM Do by |
Wk 5: 15 lines, 0 known misses, 1 unverifiable. Fastest claim latency yet (41 min). The Wk 5 Wed edit broke the ledger heading (repair commit 32e29d0).
| 6 | Tue waivers (file 6:16 PM ET commit, digest 6:09) | 5 claims | 5 of 5 filed 8:04:57-8:06:21 PM ET, latency 1 h 49 m, 7 h 07 m before Do by; none overnight. 3 won, 2 failed behind them. Cleared 3:14:06 AM |
| 6 | Thu scan, Thu TNF | NO ACTION ×2 | n/a |
| 6 | Sat trade response (commit 12:42 PM ET) | decline + counter | Offer relayed 12:36 PM; decline and counter unverifiable in the API (pending offers do not log) |
| 6 | Sun lineup (commit 9:13 AM ET, front matter 9:20) | 9 slots, 3 contingencies | 9 of 9 match the starters; contingencies unverifiable. Latency n/a |
| 6 | Mon chat (commit 8:02 PM ET) | 1 | Unverifiable; 13 min before 8:15 PM Do by |
Wk 6: 18 lines (5 claims, 2 Sat, 9 lineup + 3 IF lines counted once, 1 chat), 0 known misses, 6 unverifiable. No run missed, no double-fire, no Action fallback.
Sean acts, Wk 6 added: Tue 8 PM ×5 claims (inside 90 seconds). Running tally: Tue 7-11 PM ×19, Thu 8-9 AM ×1, Sat 1-3 PM ×1, Sun before 1 PM ×2, Wed 12-1 PM ×1. Method: `created` on claims; other times inferred from commits.
| 7 | Tue waivers (file 6:19 PM ET, digest 6:09) | 5 claims | 5 of 5 filed 6:21:42-6:23:13 PM ET, latency 1 m 53 s to 3 m 24 s, 8 h 51 m before Do by; none overnight. 2 won, 3 failed behind them. Cleared 3:14:21 AM |
| 7 | Tue trade response (commit 6:28 PM ET) | accept | Accepted 7:14:18 PM ET, 46 min later; offer had been live since 12:42 PM |
| 7 | Thu scan (8:13 AM ET) | NO ACTION | n/a |
| 7 | Thu TNF (commit 5:09 PM ET) | ADD Rodgers / DROP Vidal + QB line | Add created 5:10:38 PM ET, latency 54 s; Sun starters show Rodgers |
| 7 | Sun lineup (commit 9:04 AM ET, front matter 9:20) | ADD/DROP + 9 slots + IF line | **ADD Tampa Bay / DROP Buffalo MISSED** (no transaction, Buffalo starts the digest); 9 of 9 slots match the starters; IF not triggered. 26 min before the 9:30 lock |
| 7 | Mon chat (commit 8:11 PM ET) | 1 | Unverifiable; 4 min before the 8:15 PM Do by |
Wk 7: 20 lines, 1 known miss (the Sun DEF swap), 1 unverifiable. Fastest claim and free-agent latencies yet (under 4 min, 54 s).
Sean acts, Wk 7 added: Tue 6 PM ×6 (5 claims + trade accept 7 PM), Thu 5 PM ×1, Sun morning lineup ×1 (DEF add skipped). Running tally: Tue 6-11 PM ×25, Thu 8-9 AM ×1, Thu 5 PM ×1, Sat 1-3 PM ×1, Sun before 1 PM ×3 (lineup only), Wed 12-1 PM ×1. Method: `created` on claims and adds; other times inferred from commits.

## Lessons
1. A pushed decision is not a transaction. Wk 1-2 claims never reached Sleeper; Wk 3's did once the file led with the deadline and Sean acted within 16 minutes. Every clipboard line carries a do-by. (Wk 1-3)
2. Never cite a live score as a result. Only completed matchups are quotable. (Wk 1, held Wk 2-3)
3. A contingency Sean cannot execute before the earliest lock is not a contingency; write the swap he can make. Prefer the healthier body at the slot over the insured one (Wk 3: Mumpfield beat Evans by 6.90; Wk 5: Evans 25.3 over Addison 0.0). Health is not role: Allen 20.1 beat Skattebo 8.1 at RB2, so weigh recent volume too. Wk 6: Skattebo 0.0 at FLEX after 8.1, with Pierce 15.0 and Evans 12.4 benched; a starter with no measured touches in the file's own Why is a guess. (Wk 2-6)
4. A free agent identified at noon is gone by morning. Free-agent lines say "do now". A same-file ADD/DROP riding above a lineup block is the line that gets skipped: Wk 7 Thu's add landed in 54 s, Sun's Tampa Bay swap never did and Buffalo scored 0.0 on its bye. (Wk 2, 7)
5. Sell surplus, not starters. (Wk 2)
6. Bench spots go to players who could start a specific slot on a specific Sunday. (Wk 1)
7. Never point a live trade and a live claim at the same player. (Wk 3)
8. One run, one answer. Wk 3's double-fire is the same fault at run level; the guard prevented two files, not two runs. (Wk 1, Wk 3)
9. An Out starter is a clipboard line the day it is known, not a paragraph in Detail. Daniels sat Out from Thursday; the paste line came Saturday afternoon. (Wk 3)
10. Sean files claims in the evening after the 6 PM file: Wk 3 at 9-10 PM, Wk 4 at 11 PM, Wk 5 at 7 PM, never in the afternoon, always hours before the deadline. Wk 6 at 8 PM, Wk 7 at 6:22 PM, 2-3 minutes after the file. Schedule asks for the evening. (Wk 3-7)

## Process review
- 2026-10-27, Week 7. Run history from the commit log only (no run-list tool, no `create_trigger` in this session).
- **Data:** every decision cited a digest 0-10 minutes old; no Action fallback for a decision, no stale decision, no missing slot, no double-fire. Front-matter times 1-16 minutes after commits; harmless.
- **Decisions:** 18 rows graded: 15 Right, 1 Wrong (luck), 1 Wrong (process), 0 Unknown after Wk 6's two resolved. Won 125.78-29.05. Misses: Tampa Bay swap never made (Buffalo 0.0), Pierce FLEX 7.5 under Tucker (Lesson 3).
- **Handoff:** 7 files, structure intact, all within 400 words (Tue waivers at the cap, Detail within 250). Notifications unverifiable (no run log). Sun lineup arrived 26 min before the 9:30 London lock; Thursday's Rodgers add had already covered it.
- **Execution:** 20 lines, 1 known miss (Sun DEF ADD/DROP), 1 unverifiable. Claims filed in under 4 minutes, the Rodgers add in 54 s, the lineup block landed, the add above it did not.
- **Schedule:** five weeks of timing: Sean acts Tue 6-11 PM, Thu 5 PM and Sun morning. One miss in one slot is not a cluster; no slot moves, no reminder added.
- **Waiver time:** Oct 21 cleared 3:14:21; six weeks split 3:13 (×3) and 3:14 (×3), so no rule to the minute. Do by stays 3:00 AM. Re-measure Wk 9 after DST.
- **Changes:** none made. Four rows past 4 weeks with their kill conditions unmet marked `kept` and rolled up. Reverts: none. Locked refusals: none.

## Process changes
| Change | Date | Kill condition | Status |
|---|---|---|---|
| Kept 2026-10-27 after 4+ weeks, kill conditions unmet: every routine agent-owned with double-fire guard (09-23); Tue process review (09-23); correspondence log (09-29); Thu TNF swap for any Out/Doubtful starter (09-29) | 2026-09-23 / 09-29 | see git history | kept |
| Trade scan opt-in: default NO ACTION, one proposal max, only to a manager who has replied | 2026-10-06 | A scan sends a proposal to a manager with no prior reply, or a trade is accepted and the scan missed it | active (Wk 7: scan NO ACTION, no proposal to a silent manager) |
| Sun 11:30 AM ET inactives check, silent unless a contingency triggers (routine PENDING-TOOLS) | 2026-10-06 | It pushes on a week with no triggered contingency, or a triggered contingency goes unswapped, or the routine is still not created by 2026-10-20 | reverted 2026-10-20: never created, kill date passed (1deb638) |
| Waiver processing settled at Wed 3:13 AM ET; every waiver Do by says 3:13 AM | 2026-10-13 | A measured waiver clear outside 3:13:00-3:13:59 AM ET in the next 4 weeks (re-measure Nov 4, after daylight saving ends), or a claim filed before 3:13 that fails to process | reverted 2026-10-20: Oct 14 clear at 3:14:06 AM (b52872e); Do by is 3:00 AM until a rule that fits 3:13-3:14 is proposed |
