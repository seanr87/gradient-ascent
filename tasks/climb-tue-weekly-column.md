# Task: Weekly column (Tue 7:30 AM ET)

Read `tasks/COMMON.md` first and follow it. This task writes the **weekly column post** for the week that just finished. It is fully automated: write, commit, push, and GitHub Pages publishes it.

## Data
Always refresh the digest per COMMON.md so Monday night's final scores are in. In `data/digest.md`, use whichever of "This week's matchups" or "Last week's results" is the most recently completed week: every team has nonzero points and no game is still in progress. Call that week NN. `data/digest.json` has `scores_this_week`, `scores_last_week`, `standings`, and `all_rosters` (with `starters` per team) for the detail.

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

## Constraints
Touch nothing outside `docs/_posts/`. Do not edit `docs/assets/css/main.css`, past posts, or decision files. Commit message: `Week NN column: <headline>`. Report the post path, the commit hash, and the first paragraph.
