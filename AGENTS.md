# AGENTS.md: READ THIS, APPLY IT, DO NOT EDIT IT

Readers: every bot in the team, and the human session (Claude Code, Codex or you) that checks the bots' work.
Owner: <OWNER>. Only the owner, or a session acting on the owner's recorded decision, changes this file.
Version: 1.0

## 1. What this repo is
Two layers, one repo:
- **Context** (written by a human session, read-only for bots): `AGENTS.md`, `ops/`, `bots/`, `skills/`.
- **Outputs** (written by bots): `tasks/<task-id>/`, plus the run log `runs/<bot-slug>.jsonl` and each bot's own `bots/<slug>/memory.md` and `routines.md`.

Three invariants:
1. A task lives in your task tracker (<TRACKER>), never in this repo. A file here or a chat message is not a task. No tracker yet? Use one `TASKS.md` file kept outside `tasks/`, one line per card with an id, status and owner.
2. A bot writes only inside `tasks/<task-id>/` for a task it holds, and to its own run log, `memory.md` and `routines.md`. Nothing else.
3. Everything outside `tasks/` is written by a human session. If it is wrong, say so in your task log. Do not fix it yourself.

## 2. Where you read context: cheapest first
Go down this ladder. Stop at the first rung that answers the question.
1. The conversation and the task card.
2. This repo.
3. A connector or API (search index, CRM, tracker). Read only.
4. Web search.
5. A browser. Read `ops/browser-rules.md` first (a stub is included; set it for your own risk tolerance).
6. Ask the owner (section 3).

Cite the file path and line for every fact you use.

## 3. The six stop classes
A bot decides small things itself and logs `decided: X (because Y)`. A bot stops and asks the owner only in these classes:
| Class | Meaning |
|---|---|
| `send` | Any outbound message to a person: email, DM, post, comment. |
| `money` | Any spend, subscription, plan change or payment. |
| `delete` | Delete, overwrite or archive data that has no copy. |
| `credential` | A key, token, password or login the bot does not already hold. |
| `brand` | A name, claim, price or number that the owner has not published. |
| `fact` | A fact only the owner knows, after the bot looked in the repo and the task. |

Every stop names its class in the log line (section 5). An approval is valid only as a button or an exact "yes" on the exact text. Free chat ("sounds good") does not count.

## 4. Where you write
| What | Where |
|---|---|
| The result of a task | `tasks/<task-id>/result.md` (first line `# <task name>`, last section `## Evidence`) |
| Raw data | `tasks/<task-id>/` next to the result |
| One log line per receipt | `tasks/<task-id>/log.jsonl` |
| One line per run | `runs/<bot-slug>.jsonl` |

## 5. Log format
`log.jsonl` line, all keys required:
```json
{"ts": "2026-01-15T11:50+01:00", "bot": "Deming", "receipt": "DONE", "task": "<task-id>", "note": "one line"}
```
`receipt` is one of: `CLAIMED`, `DONE`, `BLOCKED`, `HUMAN_HOLD`, `FAILED`, `FOLLOW_UP`.
A `BLOCKED` or `HUMAN_HOLD` note carries `[ask: send|money|delete|credential|brand|fact]`. `scripts/check.py` rejects a stop without it.

## 6. Handoffs
- One handoff between bots = ONE message with the whole batch. A reviewer returns all findings in one message.
- Two rounds of bot-to-bot talk on one card, then the card owner writes `decided: X (because Y)` and moves on.
- Work a bot cannot do (code, final copy, publish) goes to a human session as a task with a line `Done when:` that a session can run.

## 7. Deterministic first
Before a bot plans a task, it splits the task into steps. A step that a rule can decide (count, diff, check, format, route, schedule) goes to a script and uses 0 model tokens. The bot keeps only the steps that need judgement. A routine wakes a bot only when a script found something changed.

## 8. Keep your own memory in the repo
Once a week a bot writes the durable facts it learned into `bots/<slug>/memory.md` (one line per fact, at most 80 lines, never secrets, contacts or personal data). A restart or a duplicate of the bot then loses nothing.
