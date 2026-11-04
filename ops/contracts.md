# Contracts between bots and scripts

## Format contracts
Idea: a script that parses a file is a reader with no judgement. A renamed heading blanks a field and nothing alerts.
- If a script parses a heading or a key, write the exact string in the bot's block (example: `## 1. Bottleneck this week: <stage> (<reason>)`).
- Add the check to `scripts/check.py` in the same change. Log-format errors found by the gate are cheaper than errors found in a report.

## The answer path
Idea: a handoff is two-way. If the bot sends work out and never reads the answer, the card dies.
- Out: the bot makes a task for a coding session (`ops/routing.md`) with a `Done when:` line.
- Back: the coding session writes the result to one file (for example `handoff/results.md`, rewritten daily). At run start the bot greps its name or card id there.

## Move work by evidence
Keep the track-record table in `ops/routing.md`. Three clean results in a kind of work a bot does not own = propose to move it.
