# Which work is yours, and how to hand off the rest

## Bots do
Inbox and tracker triage. Research and source gathering. Lists. Scheduled checks. Roll-ups of what other agents did. Routing a card to the right owner. Work that needs waiting, watching or browsing.

## Bots hand off
Code, scripts, edits to the repo, final copy, design, anything that publishes or sends.
Hand-off = one task in your tracker with four parts:
| Part | Example |
|---|---|
| Outcome | "3 hooks for Thursday's post" |
| Inputs | links to `tasks/<id>/result.md` and the sources |
| Skill | a name from `skills/` |
| Limits | "draft only, no publishing" |
Add a line `Done when:` with a check that a human session can run.

## Executors
| Work | Executor |
|---|---|
| Builds, scripts, repo edits, copy | A coding agent session (Claude Code, Codex, Cursor) |
| Second opinion, code review | A second coding agent |
| Research, triage, lists, checks | The bots |

## Move work across the line by evidence
Keep a table: date, bot, kind of task, result, "moves the line?". Three clean results in a kind of work a bot does not own yet = propose to move it to the bot.

## Stuck cards
A card with no new log line for 24 hours is stuck. The lead bot sends the owner of the card ONE complete message with the card id. At 48 hours it asks the human owner for a decision.
