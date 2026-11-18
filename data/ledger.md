# Ledger — Gradient Ascent working memory

Rewritten in full every Tuesday at 6:00 AM ET by the process review; `## State` and `## Open threads` updated by every decision run in the same commit as its decision. Hard cap 150 lines. Older weeks roll up; git history is the archive. Cite a thesis or lesson by name instead of re-arguing it.

Last full rewrite: 2026-11-17 (eighth process review, covering Week 10). Last touched: 2026-11-18 (Wk 11 post-waiver review).

## State
- **Week 10 final: lost 77.96 to Two Dumb Jaylens 123.75 (-45.79), league median 123.94, my season low.** Record **5-5**, 1222.05 PF, 7th of 12 (digest 2026-11-17 11:01 UTC). Week 11 opponent: **The Butker Jihad** (5-5, 1238.93 PF, 6th). Waiver position **#2** (was #6; it rose because four teams ahead won claims and I filed none); it drifts, so re-read it every run. **League settings: 8 of 12 make the playoffs, playoffs start Wk 15, trade deadline Wk 11.**
- Roster (14), 2026-11-17 19:02 ET digest: QB Daniels; RB Irving, B. Allen, Rodriguez; WR Lamb, Nacua [IR], Tucker, Mumpfield, Flournoy; TE Pitts, Kincaid; K Bass; DEF Tampa Bay, Green Bay. Nacua is a dead spot until Wk 15. Wk 11 four-week averages in this scoring: Irving 26.50, Lamb 20.73, Daniels 17.27, B. Allen 14.43, Bass 12.83, Flournoy 11.75, Kincaid 10.23, Rodriguez 8.50, Tucker 7.67, Pitts 5.40, Mumpfield 4.28; Tampa Bay 23.00, Green Bay 13.56.
- **Wk 11 byes ATL, CLE, GB, LAR, NE, SEA idle four of my fourteen: Pitts, Mumpfield, Nacua and Green Bay.** All but Nacua are this week's claim drops. No Thursday player on the roster (IND @ HOU).
- Wk 10 nine scored: Daniels 21.76, Lamb 18.20, Green Bay 9.00, Bass 7.70, Kincaid 7.30 (FLEX), Allen 6.10, Pitts 5.50, Tucker 1.40, Rodriguez 1.00. Bench: Flournoy 17.10, Mumpfield 11.10; Irving and Tampa Bay on bye, Nacua IR.
- **Waiver processing: settled 2026-11-17. Sleeper runs it Wed 3:05 AM ET (its own queue label, "RUNS AT Wed 3:05 am"); the clears post 3:13-3:15 AM: Sep 16 3:14:05, Sep 23 3:13:21, Sep 30 3:13:34, Oct 7 3:13:32, Oct 14 3:14:06, Oct 21 3:14:21, Oct 28 3:13:58, Nov 4 3:14:41, Nov 11 3:14:11, Nov 18 3:14:40 (tenth measured clear, inside the settled window). Do by stays 3:00 AM ET.** Sleeper processes in rounds (`seq`): every team's first claim in priority order, then every team's second; a contested name is winnable only as claim 1.
- **Wk 11 claims never reached Sleeper.** Leg 10 holds thirteen claims from seven teams at 3:14:40 AM ET and none from this roster; failed claims are recorded there (three were), so this was non-execution, not defeat. Lemon, Sutton, Hutchinson and Waller were all still free six hours later; only Ayomanor went, to Two Dumb Jaylens on a seq-11 claim. Pivot filed Wed 9:35 AM ET as three free-agency adds.
- **Sleeper's transaction feed is on leg = NFL week - 1.** `pull_sleeper.py` asks for leg 11 and gets an empty list; this week's moves live in leg 10. Every digest this week has shown no transactions for that reason, not because the league was quiet.
- **Trade: omarhouse's Bates-for-Bass DM (2026-11-13) declined and countered GET Warren / SEND Bass in the Sat 2026-11-14 file.** Sleeper's leg 10 and 11 transaction logs hold no trade of any status as of 2026-11-17 11:01 UTC, so whether the counter went out is unknown. Warren's `notes.yml` line stays while the offer is live.
- Chat targets used: Wk1 Three Wise Jaylens, Wk2 CorneliusJones, Wk3 Lost in the Land of Love, Princess Donut's Court (Wk 3 Mon), Playful Secrets (Wk 4 Mon), Sea Squirts (Wk 5 Mon), TheTroubles (Wk 6 Mon), What can Brown do for u? (Wk 7 Mon), The Wizard's Apprentice (Wk 8 Mon), Lost in the Land of Love (Wk 9 Mon, repeat of Wk 3), The Butker Jihad (Wk 10 Mon). Untargeted: Umojan Protectorate only.

## Open threads
- **Nacua on IR (MCL and PCL sprains, turf toe), earliest return Wk 15, no IR slot.** Held as a dead bench spot for the playoffs. Unwinds if the Rams' timeline slips past Wk 15, a roster crunch needs the spot, or a contender relays a starter-for-Nacua offer before the Wk 11 deadline (Wk 10 scan priced Swift from Umojan as the only shape worth taking).
- **Wk 11 pivot pending execution (3 free-agency adds, filed Wed 9:35 AM ET):** Hutchinson/Green Bay, Lemon/Mumpfield, Sutton/Pitts. First-come, so every hour is risk. Unwinds when a digest shows all three rostered; Hutchinson is moot after Thu 8:15 PM ET kickoff, the others after Sunday's lock.
- **One tight end once Pitts is dropped.** Kincaid alone at TE, no IR slot. Waller (9.62) and Mayer were both still free on Wednesday as the hedge. Unwinds on a Kincaid injury, which becomes a noon-weekday wire file (Lesson 4).
- **Trades are opt-in** (see Process changes). Wk 5-10 scans: NO ACTION. Live: the Warren-for-Bass counter to omarhouse, status unknown (no transaction in the API; Sean has not relayed a reply). Unwinds on accept, decline or the deadline. theBigScone reply drafted. WR2/FLEX is still the gap: Tucker 7.67 is the weakest starter and tonight's three WR claims are the answer, not a trade.
- **Trade deadline ambiguity.** Sleeper `trade_deadline` = 11. Read as trades allowed through Wk 11 (the Wk 11 Thu scan is the last), but if trades stop when Wk 11 opens, that scan is too late. The Thursday scan settles it from the league settings or a failed offer before it writes anything.
- **Bass is movable** because McLaughlin (K-TB, 11.79, back from bye) and Sanders (K-NYJ, 14.1 over Wk 6-9) are free against Bass' 12.03. Closes if both are rostered by someone else.
- **Sunday contingencies have no timed check.** Sean checks by eye; none has triggered in Wk 5-10. Wk 10 carried five lines, none triggered.
- **Free-agent ADD/DROP pairs outside the Tuesday cycle.** Wk 7 Sun swap never made; Wk 8 Thu 2 PM pivot took 52 h; Wk 10 Wed noon pivot landed in 30 min. Wed noon works, mid-afternoon does not (Lesson 4).
- **Claim timing: Wk 11 never landed at all.** Wk 8-10 all filed within the hour; Wk 11's five lines are absent from Sleeper's log entirely, the largest single miss since Wk 2. Closes when a week's claims appear in the leg log again.
- **Notification delivery is unverifiable.** One reported miss (Wk 9 Sun), none reported in Wk 10. Every Monday chat message in `correspondence.md` is still DRAFTED, never confirmed SENT; a relay from Sean is the only way to grade the slot.
- **Monday chat fires 2-5 minutes before the 8:15 PM Do by four weeks running** (Wk 7-10; 2 min in Wk 10). No move until a late post is confirmed; the move, when earned, is `climb-mon-league-chat` to Mon 7:00 PM ET (every Sunday game is final by then).
- **Double-fire.** The Tue 9:30 PM slot ran twice in Wk 7 and Wk 10 (digest commits 3 min apart), once in Wk 8-9; harmless by design, no file. Every other slot ran once. Sean still has to disable the seven UI routines in `SCHEDULED-TASKS.md`.
- **Thesis 4's rounds model does not explain Ayomanor.** Two Dumb Jaylens at waiver #11 won him at seq 11 while Lost in the Land of Love at #4 failed at seq 8 on the same player. For Tuesday's review, not for a decision run.
- **Interactive sessions skip the refresh.** The Sat trade response was written in a session Sean opened, on a 2 h 05 m old digest, and named a kicker on his bye (Lesson 8). Any session that writes a decision follows COMMON's setup in full.
- **League chat is unreadable by API.** `data/correspondence.md` holds the per-manager read.

## Theses
1. **Chain-movers over big plays.** Wk 1-3 supported; Wk 4 lost by 0.73; Wk 5 supported; Wk 6 under (83.65 vs 102.08); Wk 7-9 supported (Wk 9: 154.61 vs median 116.51); Wk 10 under, 77.96 vs 123.94, with Nacua on IR and Irving on bye, so not the healthy nine. Kill: the healthy nine below league-median PF three weeks running (count 0; Wk 10 does not qualify).
2. **Rushing QB over pocket QB.** Daniels 18.16, 17.24, 33.26 (Wk 5); Wk 6 21.0 vs Stroud 22.98, a wash; Wk 8 15.48, Wk 9 14.56, Wk 10 21.76 (the only starter above 20) against no streamed QB to compare. Kill: Daniels under 10 twice while the streamed QB clears 18 in the same weeks.
3. **RETIRED 2026-10-06: trade WR for RB.** Four offers, zero acceptances (kill met Wk 3). Trades are now opt-in, see Process changes.
4. **Contested names first, winnable names last.** Wk 5-9 held in order; Wk 10: Green Bay first (mandatory) won; Estime lost on priority (#4 over #7, unwinnable); Douglas lost in round 1 to Playful Secrets' first claim at #9, so he was winnable only as claim 1 and the deliberate override cost nothing. Rounds mean "contested first" is literal: only claim 1 beats another team's first claim. Kill: losing a mandatory claim to order.
5. **Filed claims land; the channel is claims plus free agency.** Wk 8: 5 of 5 filed within 2 min, 3 won; Wk 9: 5 of 5, 4 won; Wk 10: 5 of 5 filed 54-55 min after the file, 2 won, 2 claimed by others, 1 died as designed. Kill: three straight weeks with no claim won (Wk 3-10 each won one or more).
6. **Never roster two defenses or two kickers.** One deliberate one-week exception, Wk 10 (Tampa Bay's bye); back to one on Tuesday. Kill: none expected.

## Scorecard
| Week | Call | Result | Grade |
|---|---|---|---|
| 1-2 (rolled up) | Wk 1: three off-file adds and a Johnson reversal, chat cited live scores (Wrong: process ×2), Hill/Waller Unknown. Wk 2: 5 claims never filed, FA pivot 1 of 3, Lamb-for-Taylor sold a top scorer (Wrong: process ×3); Kincaid/Buffalo Right, Nacua/Mumpfield hedge never made (Wrong: process), chat numbers held (Right) | 22 lines issued through Wk 2, 12 landed | 5 Right, 6 Wrong (process), 2 Unknown |
| 3 (rolled up) | Mariota claim won, Wilson/Mitchell lost on order, Taylor trade cancelled, Sat QB swap and Sun Nacua bench Right; Thu TNF swap missing until Sat (Wrong: process); Evans/Mumpfield hedge unused and Hockenson offer declined (Wrong: luck ×2); chat clean | 11 lines | 7 Right, 1 Wrong (process), 3 Wrong (luck) |
| 4 (rolled up) | Gordon claim lost on order, B. Allen won, backups cancelled as designed, Wed and Thu NO ACTION, Mon chat clean; Sun lineup lost by 0.73 with Evans and Allen benched; Mumpfield offer unverifiable | 9 rows | 5 Right, 1 Wrong (luck), 2 Unknown |
| 5 (rolled up) | Stroud claim first and won (Daniels cleared and scored 21.94 bench), backups cancelled as designed, Coleman/Meyers cleared, Thu/Wed NO ACTION, Daniels QB 33.26 over Stroud, Evans FLEX 25.3, Nacua/Irving/Loop/Kincaid/Buffalo, chat clean; Skattebo RB2 8.1 vs Allen 20.1 and Lamb 1.9 were bad outcomes; Wed edit broke the ledger heading | 13 rows | 10 Right, 2 Wrong (luck), 1 Wrong (process), 1 Unknown |
| 6 (rolled up) | Claims Vidal, Pierce, Higbee won (Pierce 15.0 best, benched; Higbee 2.2 started), backups died as designed, Wed/Thu NO ACTION, Sat decline Right, Sun QB/RB Right; Skattebo FLEX 0.0 over Pierce 15.0 and Higbee over Kincaid; Kincaid counter and three IF lines unverifiable; chat clean | 14 rows | 9 Right, 1 Wrong (process), 1 Wrong (luck), 3 Unknown |
| 7 (rolled up) | Cooper lost on order (5 teams claimed him), Tucker and Coleman won, backups died as designed, Vele-for-Stroud accepted, Wed/Thu NO ACTION, Thu Rodgers add landed in 54 s and scored 13.58; Sun Tampa Bay swap never made and Buffalo scored 0.0 on its bye (Wrong: process, Lesson 4); Pierce FLEX 12.8 over Tucker 20.3 (Wrong: luck); chat clean | 11 rows | 9 Right, 1 Wrong (process), 1 Wrong (luck) |
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
| 10 | Claim 1 Green Bay / Willis | Won at #7 as claim 1; 9.0 at DEF with Tampa Bay on bye; Umojan and CorneliusJones failed behind me | Right |
| 10 | Claim 2 Estime / Sampson | Lost to The Wizard's Apprentice at #4 (Estime 2.1 for them); backup Rodriguez cleared | Right (lost on priority, unwinnable from #7) |
| 10 | Claim 3 Douglas / Mitchell (Thesis 4 override) | Lost in round 1 to Playful Secrets' first claim at #9 (Douglas 0.9 for them); only claim 1 could have won him, and claim 1 was the mandatory defense | Right |
| 10 | Claims 4-5 Indianapolis, Rodriguez (backups) | IND died as designed; Rodriguez cleared, started RB2 with Irving on bye, 1.0 | Right (call); the 1.0 is luck, no third back existed |
| 10 | Wed pivot: ADD Mumpfield / DROP Mitchell | Landed in 30 min; 11.1 on the bench, more than six starters, but never a start path | Right |
| 10 | Thu scan: NO ACTION; Thu TNF: START Daniels | The scan's trigger (a manager making contact) fired two days later; Daniels 21.76 | Right |
| 10 | Sat: DECLINE Bates for Bass | Bass 7.7 to Bates 5.0 in Wk 10; no transaction of any status in the API, so the decline is unverifiable | Right (call) |
| 10 | Sat: counter GET Warren / SEND Bass; reply to theBigScone | No trade in Sleeper's leg 10-11 log; Warren 8.1 on his bench, Bass 7.7 | Unknown |
| 10 | Sat: IF accepted, ADD McLaughlin / DROP Mumpfield | McLaughlin was on bye; the Sun file had to correct it to Sanders; untriggered | Wrong (process): a conditional add that could not play, written on a 2 h 05 m old digest (Lesson 8) |
| 10 | Sun: Daniels, Allen, Rodriguez, Lamb, Bass, Green Bay | 21.76, 6.1, 1.0, 18.2, 7.7, 9.0; no alternative at RB with Irving on bye; four IF lines untriggered | Right |
| 10 | Sun: Pitts TE over Kincaid | 5.5 vs 7.3; 1.8 left | Wrong (luck), minor (Lesson 3) |
| 10 | Sun: Kincaid FLEX and Tucker WR2 over Flournoy | 7.3 and 1.4 vs Flournoy 17.1 (Mumpfield 11.1); the best swap leaves 15.7, the margin was 45.79 | Wrong (luck): targets 9/4/4/3 with Pickens back was a real signal and Flournoy scored anyway; both swaps still lose by 26 |
| 10 | Mon chat vs The Butker Jihad | Wk 10 final 120.53-156.59 and Pickens 40.0 on his bench match the matchups API; no live score; first-time target | Right |

## Execution
| Week | Run | Issued | Landed in Sleeper |
|---|---|---|---|
| 1-2 (rolled up) | all | 22 lines | 12 landed, 8 never reached the app, 2 unverifiable |
| 3 (rolled up) | all | 15 lines | 15 landed or n/a, 0 known misses, 4 unverifiable; claim latency 12-16 min; Sean acts Tue 9-10 PM ×5, Thu 8-9 AM, Sat 1-3 PM, Sun before 1 PM, Wed 12-1 PM (Wk 2) |
| 4 (rolled up) | all | 15 lines | 0 known misses, 3 unverifiable; claims filed 11:10 PM, latency 4 h 56 m; Thu offer unverifiable |
| 5 (rolled up) | all | 15 lines | 0 known misses, 1 unverifiable; 5 claims filed 6:59-7:00 PM ET, latency 41 min, 8 h 13 m before Do by; the Wk 5 Wed edit broke the ledger heading (repair 32e29d0) |
| 6 (rolled up) | all | 18 lines | 0 known misses, 6 unverifiable; 5 claims filed 8:04-8:06 PM ET, latency 1 h 49 m, 7 h 07 m before Do by; cleared 3:14:06 AM; no double-fire, no Action fallback |
| 7 (rolled up) | all | 20 lines | 1 known miss (the Sun Tampa Bay / Buffalo swap), 1 unverifiable; claims filed 6:21-6:23 PM ET, latency under 4 min; Thu Rodgers add 54 s; trade accepted 46 min after the file; cleared 3:14:21 AM; the Tue 9:30 PM slot ran twice |
| 8 | Tue waivers (file 6:14 PM ET, digest 6:03) | 5 claims | 5 of 5 filed 6:16:03-6:17:34 PM ET, latency 1 m 49 s to 3 m 20 s, 9 h before the 3:00 Do by; none overnight. 3 won, 2 failed behind them. Cleared 3:13:58 AM Wed (leg 7) |
| 8 | Wed review, Thu scan, Thu TNF | NO ACTION x3 | n/a |
| 8 | Thu wire (commit 2:51 PM ET) | ADD Mitchell / DROP Pierce | **Executed Sat 7:12:25 PM ET, 52 h 21 m later, only after the Sat reaffirm (commit 4:58 PM ET, latency 2 h 14 m).** Thu note read as "now or never"; Mitchell stayed free |
| 8 | Sun lineup (commit 9:04 AM ET, front matter 9:10) | 9 slots + 2 IF lines | 9 of 9 match the starters; IF lines not triggered. 3 h 56 m before the 1:00 PM lock. Latency n/a |
| 8 | Mon chat (commit 8:10 PM ET) | 1 | Unverifiable; 5 min before the 8:15 PM Do by |
Wk 8: 19 lines (5 claims, 2 wire, 9 lineup + 2 IF, 1 chat), 0 never reached, 1 late (Thu wire 52 h), 1 unverifiable. Notifications for all 8 files unverifiable (no run log).
| 9 | Tue waivers (file 6:12 PM ET, digest 6:03) | 5 claims | 5 of 5 filed 11:49:21-11:50:39 PM ET, latency 5 h 37 m, 3 h 10 m before the 3:00 Do by; 4 won, Douglas failed behind claim 1. Cleared 3:14:41 AM Wed (leg 8) |
| 9 | Wed review, Thu scan, Thu TNF | NO ACTION x3 | n/a. Thu TNF cites digest 18:41 UTC but committed 22:10 UTC after its own 22:09 refresh; data fresh, citation wrong |
| 9 | Sun lineup (commit 9:02 AM ET, front matter 9:10) | 9 slots + 2 IF lines | 9 of 9 match the starters (16:12 UTC digest); IF lines not triggered. 3 h 58 m before the 1:00 PM lock. Latency n/a. **Sean reports no push arrived** |
| 9 | Mon chat (commit 8:11 PM ET) | 1 | Unverifiable; 4 min before the 8:15 PM Do by |
Wk 9: 17 lines (5 claims, 9 lineup + 2 IF, 1 chat), 0 known misses, 1 unverifiable, 1 reported missing push, 1 slow (claims 5 h 37 m). No run missed, no Action fallback for a decision. Run history from the commit log only.
| 10 | Tue waivers (file 6:10 PM ET, commit 6:12, digest 6:03) | 5 claims | 5 of 5 filed 7:06:08-7:07:53 PM ET in file order (seq 3, 12-15), latency 53 m 43 s to 55 m 28 s, 7 h 52 m before the 3:00 Do by; none overnight. 2 won, 2 claimed by others, IND died as designed. Cleared 3:14:11 AM Wed (leg 9). The 10:30 PM check ran silent (digest 10:39 PM) |
| 10 | Wed review (commit 12:10 PM ET, digest 12:04) | ADD Mumpfield / DROP Mitchell | Created 12:40:20 PM ET, latency 29 m 54 s; the same session committed the note cleanup at 12:41 (one run, two commits, not a double-fire) |
| 10 | Thu scan (8:07 AM ET); Thu TNF (5:12 PM ET) | NO ACTION; START Daniels | n/a; Daniels started, the only QB on the roster |
| 10 | Sat trade response (interactive session; commit 2:34 PM ET, front matter 2:50, digest 12:29) | DECLINE, counter with message, 1 IF add, 1 chat reply | No trade of any status in leg 10-11 as of 2026-11-17 11:01 UTC: decline and counter unverifiable; IF untriggered and McLaughlin correctly never added. 22 h 26 m before the Sun 1:00 PM Do by, 8 h overnight |
| 10 | Sun lineup (commit 9:09 AM ET, front matter 9:15, digest 9:02) | 9 slots + 5 IF lines | 9 of 9 match the starters (matchups API); no IF triggered. 3 h 51 m before the 1:00 PM lock. Latency n/a |
| 10 | Mon chat (commit 8:13 PM ET, digest 8:09) | 1 | Unverifiable; 2 min before the 8:15 PM Do by |
Wk 10: 27 lines (5 claims, 1 pivot, 1 START, 5 Sat lines, 9 lineup + 5 IF, 1 chat), 0 known misses, 6 unverifiable (the 5 Sat lines and the chat). Every slot ran; no Action fallback for a decision. Run history from the commit log only (the clone was shallow and was deepened to Oct 19 for this audit).
Sean acts, Wk 10 added: Tue 7:06-7:08 PM ×5 (claims), Wed 12:40 PM ×1 (pivot), Sun morning lineup ×1 (matched); Sat ~2:28 PM he relayed a DM, which is a session, not an execution. Running tally: Tue 6-11 PM ×40, Wed 12-1 PM ×2, Thu 8-9 AM ×1, Thu 5 PM ×1, Sat 1-3 PM ×1, Sat 7 PM ×1, Sun before 1 PM ×6 (lineup only). Never has acted on a Thu 2 PM file the same day. Method: `created` on claims and adds; other times inferred from commits.

## Lessons
1. A pushed decision is not a transaction. Wk 1-2 claims never reached Sleeper; Wk 3's did once the file led with the deadline and Sean acted within 16 minutes. Every clipboard line carries a do-by. (Wk 1-3)
2. Never cite a live score as a result. Only completed matchups are quotable. (Wk 1, held Wk 2-10)
3. A contingency Sean cannot execute before the earliest lock is not a contingency; write the swap he can make. Prefer the healthier body at the slot over the insured one (Wk 3: Mumpfield beat Evans by 6.90; Wk 5: Evans 25.3 over Addison 0.0). Health is not role: Allen 20.1 beat Skattebo 8.1 at RB2, so weigh recent volume too. Wk 6: a starter with no measured touches in the file's own Why is a guess. Wk 8: Kincaid [Q] scored 18.1 on the bench while Pitts started for 1.6; Questionable is not Out. Wk 9 and 10: Pitts 3.8 vs Kincaid 5.3, then 5.5 vs 7.3; a TE call on this roster is worth little either way. Wk 10: Flournoy benched for Kincaid at FLEX and Tucker at WR2 on a three-game target slope (9/4/4/3) and scored 17.1 to their 7.3 and 1.4; a slope is weaker evidence than a four-week floor, and neither swap would have closed a 45.79 margin. (Wk 2-6, 8-10)
4. A free agent identified at noon is gone by morning. Free-agent lines say "do now". A same-file ADD/DROP riding above a lineup block is the line that gets skipped: Wk 7 Thu's add landed in 54 s, Sun's Tampa Bay swap never did and Buffalo scored 0.0 on its bye. Wk 8: the Thu 2 PM Mitchell add took 52 h, the Sat reaffirm at 5 PM took 2 h 14 m; Wk 10: the Wed noon pivot landed in 30 min. Noon and 5 PM work; a mid-afternoon weekday file is not a slot Sean acts in. (Wk 2, 7, 8, 10)
5. Sell surplus, not starters. (Wk 2)
6. Bench spots go to players who could start a specific slot on a specific Sunday, and so do conditional adds: Wk 10's Saturday file named McLaughlin as the kicker to add if a trade landed, and Tampa Bay was on bye that week. Check the bye before naming a free agent. (Wk 1, 10)
7. Never point a live trade and a live claim at the same player. (Wk 3)
8. One run, one answer, and every run refreshes. Wk 3's double-fire is the same fault at run level; the guard prevented two files, not two runs. Wk 10: a session Sean opened on Saturday wrote a decision on a 2 h 05 m old digest without running the pull; an interactive session that writes a decision file is a run and follows COMMON's setup in full. (Wk 1, 3, 10)
9. An Out starter is a clipboard line the day it is known, not a paragraph in Detail. Daniels sat Out from Thursday; the paste line came Saturday afternoon. (Wk 3)
10. Sean files claims in the evening after the 6 PM file: Wk 3 at 9-10 PM, Wk 4 at 11 PM, Wk 5 at 7 PM, Wk 6 at 8 PM, Wk 7 at 6:22 PM, Wk 8 at 6:16 PM, Wk 9 at 11:49 PM, Wk 10 at 7:06 PM; never in the afternoon, always hours before the deadline. Schedule asks for the evening, and the margin shrinks the later it goes. (Wk 3-10)

## Process review
- 2026-11-17, Week 10. Run history from the commit log only (no run-list or trigger tool in this session; the clone was shallow and was deepened to Oct 19 to audit the Tuesday-night slots).
- **Data:** the six routine files were 5-13 min from their digest; the Sat interactive file was 2 h 05 m (no refresh), the only stale decision since Wk 5. No Action fallback used for a decision. Every slot ran and wrote its file; ten note slots fired (the Fri 10:19 slot ran at 11:08). The Tue 9:30 PM slot ran twice (also in Wk 7), harmless by design.
- **Decisions:** 13 rows graded: 9 Right, 2 Wrong (luck: the TE and FLEX/WR2 calls against Flournoy's 17.1), 1 Wrong (process: a conditional add on his bye), 1 Unknown (the Warren counter). Lost 77.96-123.75, 46 under the median 123.94; no bench swap closes 45.79. Theses 1, 2, 4, 5 hold; Thesis 6's one-week exception ends Tuesday.
- **Handoff:** 7 files, structure intact, all led with the action; 282-407 words excluding the clipboard (Wed review 407, 7 over the cap; Sat exactly 400), Detail 71-179. Notifications unverifiable, no miss reported. Tue file 8 h 48 m to the Do by, 4 h overnight; Sat 22 h 26 m, 8 h overnight; Mon chat 2 min.
- **Execution:** 27 lines, 0 known misses, 6 unverifiable (the 5 Sat lines and the chat). Claims filed 54-55 min after the file, the pivot in 30 min. Sean acts Tue 7 PM, Wed 12:40 PM, Sun morning.
- **Schedule:** eight weeks of timing, no cluster of misses, no slot moved. The Mon chat's 2-minute margin stays a watch until a late post is confirmed; the earned move is the chat routine to 7:00 PM ET, which this session could not make anyway (no trigger tools).
- **Waiver time:** Nov 11 cleared 3:14:11 AM (leg 9), the ninth measurement. Settled: Sleeper runs waivers Wed 3:05 AM ET, clears post 3:13-3:15; Do by stays 3:00 AM. Change 1 (40ad13a), eight files corrected.
- **Changes:** 1 of 2 made (waiver time, 40ad13a). Reverts: none (no active rows to check). Locked refusals: none. Not made: the word cap is one file over by 7 words, not a process fault; the Sat refresh miss is a session habit, written into Lesson 8, not a routine.

## Process changes
| Change | Date | Kill condition | Status |
|---|---|---|---|
| Kept 2026-10-27 after 4+ weeks, kill conditions unmet: every routine agent-owned with double-fire guard (09-23); Tue process review (09-23); correspondence log (09-29); Thu TNF swap for any Out/Doubtful starter (09-29) | 2026-09-23 / 09-29 | see git history | kept |
| Trade scan opt-in: default NO ACTION, one proposal max, only to a manager who has replied | 2026-10-06 | A scan sends a proposal to a manager with no prior reply, or a trade is accepted and the scan missed it | kept 2026-11-03 after 4 weeks (Wk 5-8 scans NO ACTION, no proposal to a silent manager) |
| Sun 11:30 AM ET inactives check, silent unless a contingency triggers (routine PENDING-TOOLS) | 2026-10-06 | It pushes on a week with no triggered contingency, or a triggered contingency goes unswapped, or the routine is still not created by 2026-10-20 | reverted 2026-10-20: never created, kill date passed (1deb638) |
| Waiver processing settled at Wed 3:13 AM ET; every waiver Do by says 3:13 AM | 2026-10-13 | A measured waiver clear outside 3:13:00-3:13:59 AM ET in the next 4 weeks, or a claim filed before 3:13 that fails to process | reverted 2026-10-20: Oct 14 clear at 3:14:06 AM (b52872e) |
| Waiver time settled: Sleeper runs it Wed 3:05 AM ET, clears post 3:13-3:15, Do by stays 3:00 AM; stated in `tasks/COMMON.md`, both Tue waiver tasks, the Wed review task, `OPS-MANUAL.md`, `README.md`, the registry and this ledger (40ad13a) | 2026-11-17 | A measured clear before 3:05:00 or after 3:20:00 AM ET in the next 4 weeks (Nov 18 to Dec 9), or a claim filed before 3:00 AM that Sleeper reports unprocessed on timing | active |
