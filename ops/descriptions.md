# Descriptions, memory and restarts

## One home for shared rules
Idea: one source of truth. A rule pasted into 20 Descriptions drifts in 20 ways.
- Shared rules live ONLY in `AGENTS.md` and `ops/description-rules.md`.
- Every Description carries a short stub ("Hard rules: read AGENTS.md, stop classes, log every run") plus a pointer to its block. A Description holds only that bot's own job.
- Breaks without it: you change a rule and half the bots keep the old one.

## A restart loses memory and routines
Idea: a bot's own memory and routines live in the vendor's app. A restart or a duplicate can wipe them. Keep a copy in the repo.
- Weekly, each bot writes `bots/<slug>/memory.md` (durable facts, at most 80 lines, newest last, no secrets, contacts or personal data).
- Each bot also exports `bots/<slug>/routines.md`: name, trigger, on or paused, window, the prompt word for word.
- Before you restart or duplicate a bot, check both files are fresh. No fresh files = no restart.

## Rules page with a version line
Idea: a result is only auditable if you know which rules it was made under.
- Keep the live rules on one page (tracker or repo). Each run reads it first and writes its `Version:` in the first log line.
