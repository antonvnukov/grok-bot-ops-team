# Usage and cost: the rules that came from burning the allowance

Idea: a bot team has a fixed allowance. The biggest cost is not the work. It is waking a bot that finds nothing to do, and a bot re-reading a long chat on every run.

## Rules
1. **Log `started` on every run line.** Usage data may have no bot column. Count runs per bot from your own run log (`templates/run-line.jsonl`). Without it you cannot say which bot used the allowance.
2. **Cheap check first.** Before work, a bot makes ONE cheap check (one query, one file stamp). Nothing changed: write nothing, send nothing.
3. **Pull your own queue.** On the first run of the day a bot queries its own queue once. Do not message bots to wake them. A message is a wake-up and costs a run.
4. **A script wakes the bot, not the clock.** A routine fires a bot only when a script found a changed input (`scripts/precheck.py` shows the pattern).
5. **Two rounds, then decide.** Bot-to-bot talk on one card ends after 2 rounds. The card owner writes `decided: X (because Y)` and moves on. Priority messages between bots only for a stop, or when the owner is waiting.
6. **Weekly prune.** Each week list the routines whose runs changed nothing outside logs. The owner of each pauses its routine (pause, never delete; delete needs the human's yes).
7. **Never cut the money path.** In a freeze, pause the non-money bots first. The bots that touch revenue and the reviewer keep running.
8. **Spend freeze.** A freeze is a dated rule with an end time in `ops/description-rules.md`, so it expires by itself.

## What to measure
Runs per bot per week. Runs that changed something outside logs. Stops with no class. Put the numbers in the weekly report. This repo gives no savings figure: measure your own before you quote one.
