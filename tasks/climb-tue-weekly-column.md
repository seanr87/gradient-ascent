# Task: Weekly column (Tue 7:30 AM ET)

Read `tasks/COMMON.md` first and follow it. This task writes the **weekly column post** for the week that just finished. It is fully automated: write, commit, push, and GitHub Pages publishes it.

## Data
COMMON.md already refreshed the digest at the start of this run, so Monday night's final scores are in. Exception to COMMON's setup step 4: this run also reads every decision file for week NN (the week just finished), because it grades them; the digest header will already say week NN+1. In `data/digest.md`, use whichever of "This week's matchups" or "Last week's results" is the most recently completed week: every team has nonzero points and no game is still in progress. Call that week NN. `data/digest.json` has `scores_this_week`, `scores_last_week`, `standings`, and `all_rosters` (with `starters` per team) for the detail.

## When to skip
If no week has completed results yet (preseason, or before the Week 1 Monday night game is final), or if `docs/_posts/` already has a post for week NN, do not write anything. Report `SKIPPED: <reason>` and stop. Never publish a column on a guess.

## The post
Write `docs/_posts/YYYY-MM-DD-week-NN.md` (today's date) with front matter:

```
---
layout: post
title: "Week NN: <a short, dry headline>"
date: YYYY-MM-DD 07:30:00 -0400
---
```

500 to 900 words. First-person Claude as manager, dry, confident, lightly sarcastic, no exclamation points. Content, in this order:
1. **My result.** Score, opponent, won or lost, and one honest sentence on why.
2. **What I decided and what the data said.** Walk this week's files in `docs/_decisions/` (waivers, review, trades, Thursday, lineup): the calls I made, and which turned out right or wrong, stated plainly. Misses get named. Nothing gets quietly revised.
3. **Superlatives.** Three to five, drawn from actual scores and lineups in the digest: highest and lowest score, closest game, worst bench decision you can see in `all_rosters` (a benched player outscoring a starter at the same position), the week's most pointless transaction, and so on. Name the team and the manager display name. Dry, specific, earned.
4. **Next.** Two or three sentences on what Tuesday's waiver run needs to fix.

If `docs/_decisions/` has no entries for week NN, write the column from the digest alone and note that the paperwork was not filed.

The first paragraph is the excerpt shown on the home page and the column index, so make it stand alone.

## After the post is written: the self-improvement loop
This run is the only one that rewrites the ledger beyond `## State` and `## Open threads`. Do these five steps in order, in the same commit as the post.

1. **Grade.** For each of week NN's calls (every clipboard line and every start/bench call in that week's decision files), add a row to `## Scorecard` in `data/ledger.md`: `Week | Call | Result | Right/Wrong/Unknown`, with a one-line cause in the Result column. Wrong because of luck (the call was sound, the outcome was not) and wrong because of process (the call was unsound, or was never executed) are graded separately and labelled so: `Wrong (luck)` or `Wrong (process)`. A call whose result cannot be known yet is `Unknown`, never guessed.
2. **Execution audit.** Compare every clipboard line from week NN to the Sleeper transactions and lineups in the digest (and the week's transaction endpoint if the digest slice is short) and log issued vs. landed per run in `## Execution`. If anything did not land, the column says so plainly, in the "What I decided" section, naming the line.
3. **Rewrite the ledger** to the 150-line cap: refresh `## State` and `## Open threads`, keep only the last 3 weeks of `## Scorecard` in full and roll older weeks into a single summary line each (right/wrong/unknown counts and the one call that mattered), and do the same for `## Execution`. Re-check every thesis against the week's results and record a kill condition met as the thesis retired.
4. **Distill.** Add or update a `## Lessons` entry only when it has evidence from actual results, citing the week that taught it. Merge duplicates. Drop any lesson disproven twice. Never more than 10.
5. **Propose, don't self-edit.** If a lesson has now held for 2+ weeks, or a `Wrong (process)` call had a cause that lives in a `tasks/` file, open at most one pull request per week that edits the relevant `tasks/` file:
   - Branch `process/wkNN-<short-slug>` off `master`, containing only the `tasks/` edit. Push the branch; never commit it to `master`.
   - Open the PR with the GitHub MCP tools. Title: `Process: <rule in ≤10 words>`. Body: the evidence weeks (which Scorecard rows or Lessons) and the exact diff rationale, one paragraph.
   - Never merge it yourself. Do not open a second one while last week's is still open; mention the open one instead.
   - Mention the PR link in the push notification.

   Routines never commit changes to `tasks/` directly. Instructions a run writes for itself need a human merge as a drift check.

## Constraints
Write only `docs/_posts/` and `data/ledger.md` on `master` (plus a `tasks/` edit on a PR branch under step 5). Do not edit `docs/assets/css/main.css`, past posts, or decision files. Commit message: `Week NN column: <headline>`. Push per COMMON.md. There is no deadline and no clipboard for this run, so the run's final output is exactly two things and nothing else: `NO ACTION` in a code fence, and the link to the published post (plus the PR link on its own line if one was opened).
