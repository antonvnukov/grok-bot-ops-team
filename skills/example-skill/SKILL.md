---
name: weekly-stuck-card-sweep
description: Find cards with no new log line for 24 hours and write one nudge per card.
---
# weekly-stuck-card-sweep

1. Query the tracker: status Queued or Executing.
2. For each card, read the last line of `tasks/<id>/log.jsonl`.
3. If the last `ts` is older than 24 hours, add the card to the list. (A script does steps 1 to 3. This is deterministic.)
4. For each card on the list, write ONE complete message to the owner bot with the card id and the age.
5. If the list is empty, write nothing and send no message.

Done when: `runs/chief.jsonl` has one line for this run, and each stuck card has exactly one comment.
