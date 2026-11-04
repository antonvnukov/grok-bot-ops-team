# Shared Description rules, in full

Shared rules live here and in `AGENTS.md`. They are never pasted into each bot's Description. Every Description carries only this stub plus its own job.

## The stub (same text in every Description)
Hard rules for every bot: read AGENTS.md and your block in bots/<your-slug>/ first. A newer AGENTS.md wins over this stub. Stop only in the six classes (send, money, delete, credential, brand, fact), and name the class. Log every run. Full text: ops/description-rules.md.

## Dated rules
A temporary rule (for example a spend freeze) is written here with an end date, so it expires by itself:
- Format: `## <rule name> (until YYYY-MM-DD HH:MM <timezone>)`, then the rule, then the reason and where the evidence is.
