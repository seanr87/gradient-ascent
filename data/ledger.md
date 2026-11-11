# Ledger — Gradient Ascent working memory

Rewritten in full every Tuesday at 6:00 AM ET by the process review; `## State` and `## Open threads` updated by every decision run in the same commit as its decision. Hard cap 150 lines. Older weeks roll up; git history is the archive. Cite a thesis or lesson by name instead of re-arguing it.

Last full rewrite: 2026-11-10 (seventh process review, covering Week 9). Last touched: 2026-11-10 (Wk 10 Tue waivers, then the filing confirmation).

## State
- **Week 9 final: won 154.61 to Sea Squirts 117.74 (+36.87), league median 116.51.** Record **5-4**, 1144.09 PF, 6th of 12. Week 10 opponent: **Two Dumb Jaylens** (6-3, 1120.12 PF, 3rd). Waiver position **#7** (digest 2026-11-10 23:03 UTC, unchanged since 11:02; the Wk 9 win moved me up from #12); it drifts, so re-read it every run.
- Roster (14), 2026-11-10 23:03 digest: QB Daniels, Willis [**IR**, groin]; RB Irving, B. Allen, Sampson; WR Lamb, Nacua [Q], Tucker, A. Mitchell, Flournoy; TE Pitts, Kincaid; K Bass; DEF Tampa Bay. **Wk 10 hole: DEF is empty** (TB bye) and Irving is out, so RB2 is Sampson until a claim clears. No transactions by me outside the Tuesday claims in Wk 9.
- Wk 9 nine scored: Nacua 32.5, Lamb 30.0, Irving 28.5, TB 16.25, Daniels 14.56, Bass 14.1, Tucker 9.0, Allen 5.9, Pitts 3.8. Bench: Flournoy 7.3, Sampson 7.3, Kincaid 5.3, Willis 3.82, Mitchell 0.0.
- **Waiver processing: measured 3:13-3:14 AM ET, not settled.** Sep 16 3:14:05, Sep 23 3:13:21, Sep 30 3:13:34, Oct 7 3:13:32, Oct 14 3:14:06, Oct 21 3:14:21, Oct 28 3:13:58, Nov 4 3:14:41 (first post-DST clear, same wall-clock time; Wk 9 claims filed under leg 8). Eight weeks, 3:13:21 to 3:14:41, 3:13 (x4) / 3:14 (x4); no to-the-minute rule, so every waiver Do by says **3:00 AM ET**. **New 2026-11-10, from a screenshot of the claim queue: Sleeper labels the Wk 10 claims "RUNS AT Wed 3:05 am".** That is the scheduled start, and the eight measured clears sit 8-10 minutes after it, so 3:05 scheduled plus queue time explains 3:13-3:14 rather than contradicting it. First direct read of the schedule rather than an inferred clear; the process review has the evidence to settle the Do by.
- Chat targets used: Wk1 Three Wise Jaylens, Wk2 CorneliusJones, Wk3 Lost in the Land of Love, Princess Donut's Court (Wk 3 Mon), Playful Secrets (Wk 4 Mon), Sea Squirts (Wk 5 Mon), TheTroubles (Wk 6 Mon), What can Brown do for u? (Wk 7 Mon), The Wizard's Apprentice (Wk 8 Mon), Lost in the Land of Love (Wk 9 Mon, a repeat of Wk 3).

## Open threads
- **Wk 10 byes: CHI, DEN, PHI, TB** (Sleeper schedule endpoint). Irving and the TB defense are both out; Nacua still Questionable, re-read Friday.
- **Wk 10 claims filed, 5 at waiver #7:** GB DEF / Willis (backup IND), Estime / Sampson (backup Rodriguez), Douglas / A. Mitchell. All unwind Wed ~3:14 AM when waivers process; `notes.yml` carries five new lines, orphans for any claim that fails.
- **Two defenses for one week**, a deliberate exception to Thesis 6: TB (20.62 a game) sits its bye while the GB stream starts. Unwinds when GB is dropped after Wk 10 and TB resumes.
- **Willis on IR (groin), no IR slot.** He is the drop in claims 1 and 4; if both fail he is still a dead spot and goes as a free-agent drop. Closes when he leaves the roster.
- **Wk 10 is Two Dumb Jaylens (6-3, 3rd).** No trade or hedge open; waiver #7.
- **TE: Pitts 3.8 vs Kincaid 5.3 in Wk 9 (Pitts 1.6 vs 18.1 in Wk 8).** Decide on measured touches and Friday status (Lesson 3); a coin flip either way, not a roster hole.
- **Trades are opt-in** (see Process changes). Wk 5-9 scans: NO ACTION. SpaceElf is not buying again.
- **Sunday contingencies have no timed check.** Sean checks by eye; none has triggered in Wk 5-9.
- **Free-agent ADD/DROP pairs outside the Tuesday cycle.** Wk 7 Sun swap never made; Wk 8 Thu pivot took 52 h. None in Wk 9. Lesson 4. Not yet a slot cluster.
- **Claim timing recovered in Wk 10.** All five filed by 7:08 PM ET, 58 min after the 6:10 PM file and 8 h before the deadline, against Wk 9's 11:49 PM. The "after 10 PM again" condition did not trigger, so no slot move; Wk 9 stays a single outlier. Closes if Wk 11 also lands before 10 PM.
- **Notification delivery is unconfirmed, with one reported miss.** Sean says no push arrived for the Wk 9 Sun lineup (commit 9:02 AM ET). No run log, so this review cannot grade it. The slow Tue claims in Wk 9 are consistent with a late or missed push but do not prove it. Watch; no change on one report.
- **Monday chat slot fires 4-5 minutes before the 8:15 PM Do by** three weeks running (Wk 7-9). Unverifiable whether Sean posts in time; cite only finished games (Lesson 2).
- **Double-fire.** Sean still has to disable the seven UI routines in `SCHEDULED-TASKS.md`; no double-fire seen in Wk 7-9.
- **League chat is unreadable by API.** `data/correspondence.md` holds the per-manager read.

## Theses
1. **Chain-movers over big plays.** Wk 1-3 supported; Wk 4 lost by 0.73; Wk 5 supported; Wk 6 under (83.65 vs 102.08); Wk 7 supported (125.78 vs 116.78); Wk 8 supported: 131.63 vs median 124.61; Wk 9 supported: 154.61 vs median 116.51, Irving 28.5, Nacua 32.5, Lamb 30.0. Kill: the healthy nine below league-median PF three weeks running (Wk 7-9 over).
2. **Rushing QB over pocket QB.** Daniels 18.16, 17.24, 33.26 (Wk 5); Wk 6 21.0 vs Stroud 22.98, a wash; Wk 7 untested; Wk 8 Daniels 15.48 and Wk 9 14.56 against no streamed QB to compare (Willis 3.82 on the bench). Kill: Daniels under 10 twice while the streamed QB clears 18 in the same weeks.
3. **RETIRED 2026-10-06: trade WR for RB.** Four offers, zero acceptances (kill met Wk 3). Trades are now opt-in, see Process changes.
4. **Contested names first, winnable names last.** Wk 5 Stroud first, won; Wk 6 all won in order; Wk 7 Cooper first, lost to waiver order; Wk 8 Tampa Bay, Pitts, Bass all won in order (three independent drops); Wk 9 Mitchell first, all four won in order. Kill: losing a mandatory claim to order.
5. **Filed claims land; the channel is claims plus free agency.** Wk 8: 5 of 5 filed within 2 minutes of the file, 3 won, 2 failed behind wins as designed; Wk 9: 5 of 5 filed within 78 seconds of each other (5 h 37 m after the file), 4 won, Douglas died behind claim 1. Kill: three straight weeks with no claim won (Wk 3-9 each won one or more).
6. **Never roster two defenses or two kickers.** Kill: none expected.

## Scorecard
| Week | Call | Result | Grade |
|---|---|---|---|
| 1-2 (rolled up) | Wk 1: three off-file adds and a Johnson reversal, chat cited live scores (Wrong: process ×2), Hill/Waller Unknown. Wk 2: 5 claims never filed, FA pivot 1 of 3, Lamb-for-Taylor sold a top scorer (Wrong: process ×3); Kincaid/Buffalo Right, Nacua/Mumpfield hedge never made (Wrong: process), chat numbers held (Right) | 22 lines issued through Wk 2, 12 landed | 5 Right, 6 Wrong (process), 2 Unknown |
| 3 (rolled up) | Mariota claim won, Wilson/Mitchell lost on order, Taylor trade cancelled, Sat QB swap and Sun Nacua bench Right; Thu TNF swap missing until Sat (Wrong: process); Evans/Mumpfield hedge unused and Hockenson offer declined (Wrong: luck ×2); chat clean | 11 lines | 7 Right, 1 Wrong (process), 3 Wrong (luck) |
| 4 (rolled up) | Gordon claim lost on order, B. Allen won, backups cancelled as designed, Wed and Thu NO ACTION, Mon chat clean; Sun lineup lost by 0.73 with Evans and Allen benched; Mumpfield offer unverifiable | 9 rows | 5 Right, 1 Wrong (luck), 2 Unknown |
| 5 (rolled up) | Stroud claim first and won (Daniels cleared and scored 21.94 bench), backups cancelled as designed, Coleman/Meyers cleared, Thu/Wed NO ACTION, Daniels QB 33.26 over Stroud, Evans FLEX 25.3, Nacua/Irving/Loop/Kincaid/Buffalo, chat clean; Skattebo RB2 8.1 vs Allen 20.1 and Lamb 1.9 were bad outcomes; Wed edit broke the ledger heading | 13 rows | 10 Right, 2 Wrong (luck), 1 Wrong (process), 1 Unknown |
| 6 (rolled up) | Claims Vidal, Pierce, Higbee won (Pierce 15.0 best, benched; Higbee 2.2 started), backups died as designed, Wed/Thu NO ACTION, Sat decline Right, Sun QB/RB Right; Skattebo FLEX 0.0 over Pierce 15.0 and Higbee over Kincaid; Kincaid counter and three IF lines unverifiable; chat clean | 14 rows | 9 Right, 1 Wrong (process), 1 Wrong (luck), 3 Unknown |
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
| 8 | Claims 1-3 Tampa Bay, Pitts, Bass (independent drops) | All won in order at #5; Tampa Bay 15.75, Bass 16.7 started well, Pitts 1.6 | Right (Tampa Bay, Bass); Wrong (luck) (Pitts' 1.6 was an outlier from 13.1 a game) |
| 8 | Claims 4-5 Green Bay, Mason Taylor (backups) | Died behind the wins, as designed | Right |
| 8 | Wed review: NO ACTION | Roster set; waiver fell #5 to #12 as predicted | Right |
| 8 | Thu scan: NO ACTION; Thu TNF: NO ACTION | No gap a trade fills; no rostered player in Carolina-Green Bay | Right |
| 8 | Thu wire: ADD Mitchell / DROP Pierce | Pierce on IR was a dead spot; Mitchell stayed free and added 52 h later (see Execution); Mitchell 6.7 on the bench | Right (call); execution Wrong (process) is Execution's row |
| 8 | Sat wire: reaffirm Mitchell / Pierce on changed reasoning | Landed 2 h 14 m later at 7:12 PM; Barkley played, Mitchell not needed | Right |
| 8 | Sun: Daniels, Irving, Allen, Nacua, Lamb, Bass, Tampa Bay | 15.48, 23.5, 26.3, 21.0, 11.3, 16.7, 15.75; no contingency triggered | Right |
| 8 | Sun: Pitts TE over Kincaid [Q] | 1.6 vs 18.1 on the bench; 16.5 left, the win was by 44.02 | Wrong (luck): Kincaid played, Pitts' role was the signal for 13.1 a game but not for this game (Lesson 3) |
| 8 | Sun: Tucker FLEX over Mitchell, Coleman | Tucker 0.0 vs 6.7 and 0.9; 6.7 left | Wrong (luck): Tucker's 20.3 in Wk 7 was the basis; Mitchell on the bench was not a start path |
| 8 | Mon chat vs The Wizard's Apprentice | Wk 7 final 102.58 vs 109.47 matches the digest; no live score cited | Right |
| 9 | Claims 1-4 Mitchell, Willis, Flournoy, Sampson (independent drops) | All four won in order at #6; none started: Flournoy 7.3, Sampson 7.3, Willis 3.82, Mitchell 0.0 on the bench | Right (call, cleared as designed); no points gained yet |
| 9 | Claim 5 Douglas (backup) | Died behind claim 1, as designed | Right |
| 9 | Wed review: NO ACTION; Thu scan: NO ACTION; Thu TNF: NO ACTION | Douglas would start nothing; no gap a trade fills; no rostered player in JAX-BAL | Right |
| 9 | Sun: Daniels, Irving, Allen, Nacua, Lamb, Bass, Tampa Bay | 14.56, 28.5, 5.9, 32.5, 30.0, 14.1, 16.25; no contingency triggered | Right |
| 9 | Sun: Pitts TE over Kincaid | 3.8 vs 5.3; 1.5 left, the win was by 36.87 | Wrong (luck): Pitts' 13.1 role was the right read, minor miss (Lesson 3) |
| 9 | Sun: Tucker FLEX over Mitchell, Flournoy, Sampson | 9.0 vs 0.0, 7.3, 7.3 | Right |
| 9 | Mon chat vs Lost in the Land of Love | Wk 8 final 119.52 vs 66.76 cited, no live score; target repeated from Wk 3 | Right |

## Execution
| Week | Run | Issued | Landed in Sleeper |
|---|---|---|---|
| 1-2 (rolled up) | all | 22 lines | 12 landed, 8 never reached the app, 2 unverifiable |
| 3 (rolled up) | all | 15 lines | 15 landed or n/a, 0 known misses, 4 unverifiable; claim latency 12-16 min; Sean acts Tue 9-10 PM ×5, Thu 8-9 AM, Sat 1-3 PM, Sun before 1 PM, Wed 12-1 PM (Wk 2) |
| 4 (rolled up) | all | 15 lines | 0 known misses, 3 unverifiable; claims filed 11:10 PM, latency 4 h 56 m; Thu offer unverifiable |
| 5 (rolled up) | all | 15 lines | 0 known misses, 1 unverifiable; 5 claims filed 6:59-7:00 PM ET, latency 41 min, 8 h 13 m before Do by; the Wk 5 Wed edit broke the ledger heading (repair 32e29d0) |
| 6 (rolled up) | all | 18 lines | 0 known misses, 6 unverifiable; 5 claims filed 8:04-8:06 PM ET, latency 1 h 49 m, 7 h 07 m before Do by; cleared 3:14:06 AM; no double-fire, no Action fallback |
| 7 | Tue waivers (file 6:19 PM ET, digest 6:09) | 5 claims | 5 of 5 filed 6:21:42-6:23:13 PM ET, latency 1 m 53 s to 3 m 24 s, 8 h 51 m before Do by; none overnight. 2 won, 3 failed behind them. Cleared 3:14:21 AM |
| 7 | Tue trade response (commit 6:28 PM ET) | accept | Accepted 7:14:18 PM ET, 46 min later; offer had been live since 12:42 PM |
| 7 | Thu scan (8:13 AM ET) | NO ACTION | n/a |
| 7 | Thu TNF (commit 5:09 PM ET) | ADD Rodgers / DROP Vidal + QB line | Add created 5:10:38 PM ET, latency 54 s; Sun starters show Rodgers |
| 7 | Sun lineup (commit 9:04 AM ET, front matter 9:20) | ADD/DROP + 9 slots + IF line | **ADD Tampa Bay / DROP Buffalo MISSED** (no transaction, Buffalo starts the digest); 9 of 9 slots match the starters; IF not triggered. 26 min before the 9:30 lock |
| 7 | Mon chat (commit 8:11 PM ET) | 1 | Unverifiable; 4 min before the 8:15 PM Do by |
Wk 7: 20 lines, 1 known miss (the Sun DEF swap), 1 unverifiable. Fastest claim and free-agent latencies yet (under 4 min, 54 s).
| 8 | Tue waivers (file 6:14 PM ET, digest 6:03) | 5 claims | 5 of 5 filed 6:16:03-6:17:34 PM ET, latency 1 m 49 s to 3 m 20 s, 9 h before the 3:00 Do by; none overnight. 3 won, 2 failed behind them. Cleared 3:13:58 AM Wed (leg 7) |
| 8 | Wed review, Thu scan, Thu TNF | NO ACTION x3 | n/a |
| 8 | Thu wire (commit 2:51 PM ET) | ADD Mitchell / DROP Pierce | **Executed Sat 7:12:25 PM ET, 52 h 21 m later, only after the Sat reaffirm (commit 4:58 PM ET, latency 2 h 14 m).** Thu note read as "now or never"; Mitchell stayed free |
| 8 | Sun lineup (commit 9:04 AM ET, front matter 9:10) | 9 slots + 2 IF lines | 9 of 9 match the starters; IF lines not triggered. 3 h 56 m before the 1:00 PM lock. Latency n/a |
| 8 | Mon chat (commit 8:10 PM ET) | 1 | Unverifiable; 5 min before the 8:15 PM Do by |
Wk 8: 19 lines (5 claims, 2 wire, 9 lineup + 2 IF, 1 chat), 0 never reached, 1 late (Thu wire 52 h), 1 unverifiable. Notifications for all 8 files unverifiable (no run log).
Sean acts, Wk 8 added: Tue 6 PM x5, Sat 7 PM x1, Sun morning lineup x1. **Wk 9 added: Tue 11:49-11:50 PM x5 (claims, 78 seconds), Sun morning lineup x1 (matched).** Running tally: Tue 6-11 PM x35, Thu 8-9 AM x1, Thu 5 PM x1, Sat 1-3 PM x1, Sat 7 PM x1, Sun before 1 PM x5 (lineup only), Wed 12-1 PM x1. Never has acted on a Thu 2 PM file the same day. Method: `created` on claims and adds; other times inferred from commits.
| 9 | Tue waivers (file 6:12 PM ET, digest 6:03) | 5 claims | 5 of 5 filed 11:49:21-11:50:39 PM ET, latency 5 h 37 m, 3 h 10 m before the 3:00 Do by; 4 won, Douglas failed behind claim 1. Cleared 3:14:41 AM Wed (leg 8) |
| 9 | Wed review, Thu scan, Thu TNF | NO ACTION x3 | n/a. Thu TNF cites digest 18:41 UTC but committed 22:10 UTC after its own 22:09 refresh; data fresh, citation wrong |
| 9 | Sun lineup (commit 9:02 AM ET, front matter 9:10) | 9 slots + 2 IF lines | 9 of 9 match the starters (16:12 UTC digest); IF lines not triggered. 3 h 58 m before the 1:00 PM lock. Latency n/a. **Sean reports no push arrived** |
| 9 | Mon chat (commit 8:11 PM ET) | 1 | Unverifiable; 4 min before the 8:15 PM Do by |
Wk 9: 17 lines (5 claims, 9 lineup + 2 IF, 1 chat), 0 known misses, 1 unverifiable, 1 reported missing push, 1 slow (claims 5 h 37 m). No run missed, no double-fire, no Action fallback for a decision. Run history from the commit log only.

## Lessons
1. A pushed decision is not a transaction. Wk 1-2 claims never reached Sleeper; Wk 3's did once the file led with the deadline and Sean acted within 16 minutes. Every clipboard line carries a do-by. (Wk 1-3)
2. Never cite a live score as a result. Only completed matchups are quotable. (Wk 1, held Wk 2-3)
3. A contingency Sean cannot execute before the earliest lock is not a contingency; write the swap he can make. Prefer the healthier body at the slot over the insured one (Wk 3: Mumpfield beat Evans by 6.90; Wk 5: Evans 25.3 over Addison 0.0). Health is not role: Allen 20.1 beat Skattebo 8.1 at RB2, so weigh recent volume too. Wk 6: Skattebo 0.0 at FLEX after 8.1, with Pierce 15.0 and Evans 12.4 benched; a starter with no measured touches in the file's own Why is a guess. Wk 8: Kincaid [Q] played and scored 18.1 on the bench while the healthy Pitts started and scored 1.6; Questionable is not Out. Wk 9: Pitts 3.8 vs Kincaid 5.3, so a TE call is worth little either way; do not agonize over it. (Wk 2-6, 8, 9)
4. A free agent identified at noon is gone by morning. Free-agent lines say "do now". A same-file ADD/DROP riding above a lineup block is the line that gets skipped: Wk 7 Thu's add landed in 54 s, Sun's Tampa Bay swap never did and Buffalo scored 0.0 on its bye. Wk 8: the Thu 2 PM Mitchell add took 52 h, the Sat reaffirm at 5 PM took 2 h 14 m; a mid-afternoon weekday file is not a slot Sean acts in. (Wk 2, 7, 8)
5. Sell surplus, not starters. (Wk 2)
6. Bench spots go to players who could start a specific slot on a specific Sunday. (Wk 1)
7. Never point a live trade and a live claim at the same player. (Wk 3)
8. One run, one answer. Wk 3's double-fire is the same fault at run level; the guard prevented two files, not two runs. (Wk 1, Wk 3)
9. An Out starter is a clipboard line the day it is known, not a paragraph in Detail. Daniels sat Out from Thursday; the paste line came Saturday afternoon. (Wk 3)
10. Sean files claims in the evening after the 6 PM file: Wk 3 at 9-10 PM, Wk 4 at 11 PM, Wk 5 at 7 PM, never in the afternoon, always hours before the deadline. Wk 6 at 8 PM, Wk 7 at 6:22 PM, Wk 8 at 6:16 PM, 2-3 minutes after the file; Wk 9 at 11:49 PM, 5 h 37 m after it, 3 h 10 m before the deadline. Schedule asks for the evening, and the margin shrinks the later it goes. (Wk 3-9)

## Process review
- 2026-11-10, Week 9. Run history from the commit log only (no run-list or trigger tool in this session).
- **Data:** every digest 0-22 min old at decision time. One wrong citation: Thu TNF cites 18:41 UTC but ran after its own 22:09 refresh. No fallback, no missed slot, no double-fire.
- **Decisions:** 12 rows graded: 9 Right, 1 Wrong (luck: Pitts 3.8 vs Kincaid 5.3), 0 Wrong (process), 0 Unknown. Won 154.61-117.74, 38.1 over the median 116.51.
- **Handoff:** 6 files, structure intact, 157-380 words excluding the clipboard, all led with the action. Notifications unverifiable; Sean reports the Sun lineup push never arrived. Tue file had 8 h 48 m to the Do by, 4 h of it overnight.
- **Execution:** 17 lines, 0 known misses. Claims filed 11:49 PM, 5 h 37 m after the file, against 2-3 min in Wk 7-8; 3 h 10 m of margin.
- **Schedule:** seven weeks of timing. One late Tue and one reported push miss is not a cluster; no moves. Watch: Tue claims after 10 PM again in Wk 10 means a slot move or reminder.
- **Waiver time:** Nov 4 cleared 3:14:41 AM, same wall-clock time after DST. Eight weeks 3:13:21-3:14:41, not to the minute; Do by stays 3:00 AM.
- **Changes:** none made. Active process changes to check: none (all rows kept or reverted). Reverts: none. Locked refusals: none.

## Process changes
| Change | Date | Kill condition | Status |
|---|---|---|---|
| Kept 2026-10-27 after 4+ weeks, kill conditions unmet: every routine agent-owned with double-fire guard (09-23); Tue process review (09-23); correspondence log (09-29); Thu TNF swap for any Out/Doubtful starter (09-29) | 2026-09-23 / 09-29 | see git history | kept |
| Trade scan opt-in: default NO ACTION, one proposal max, only to a manager who has replied | 2026-10-06 | A scan sends a proposal to a manager with no prior reply, or a trade is accepted and the scan missed it | kept 2026-11-03 after 4 weeks (Wk 5-8 scans NO ACTION, no proposal to a silent manager) |
| Sun 11:30 AM ET inactives check, silent unless a contingency triggers (routine PENDING-TOOLS) | 2026-10-06 | It pushes on a week with no triggered contingency, or a triggered contingency goes unswapped, or the routine is still not created by 2026-10-20 | reverted 2026-10-20: never created, kill date passed (1deb638) |
| Waiver processing settled at Wed 3:13 AM ET; every waiver Do by says 3:13 AM | 2026-10-13 | A measured waiver clear outside 3:13:00-3:13:59 AM ET in the next 4 weeks (re-measure Nov 4, after daylight saving ends), or a claim filed before 3:13 that fails to process | reverted 2026-10-20: Oct 14 clear at 3:14:06 AM (b52872e); Do by is 3:00 AM until a rule that fits 3:13-3:14 is proposed |
