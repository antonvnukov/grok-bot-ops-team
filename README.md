# Grok bot ops team

A template for running a team of Grok bots (or any chat agents) with an **ops layer**: roles, six stop classes, a reviewer, run logs, routing and kill rules. Click **Use this template** to start your own.

The ops layer is the part that makes the other bots safe to leave alone. It is the part most setups skip.

## What is in the box
| Path | What it is |
|---|---|
| `AGENTS.md` | The one contract every bot reads: invariants, read ladder, six stop classes, log format |
| `ops/bots.md` | The ops roster: 7 bots, one job each |
| `ops/principles.md` | The idea behind each rule, and what breaks without it |
| `ops/usage-and-cost.md` | Run log, cheap check, weekly prune: how not to burn the allowance |
| `ops/descriptions.md`, `ops/privacy.md`, `ops/contracts.md` | One home for rules, memory and restarts, privacy gate, format contracts |
| `CREDITS.md` | Who inspired what |
| `ops/routing.md` | What bots do, what they hand to a coding agent, how a stuck card escalates |
| `bots/<slug>/block.md` | One block per bot: job, routine, kill rule, paste-ready Description |
| `bots/_template/block.md` | Copy this for a new bot |
| `skills/` | Skill format and one example |
| `scripts/check.py` | A gate for the log format (`--self-test` included) |
| `hints/HINTS.md` | Hints and tips from X, with credits |

## The six rules above every bot
1. **One bot, one job.** If the job sentence has "and", split it.
2. **Six stop classes.** A bot asks the owner only for `send`, `money`, `delete`, `credential`, `brand` or `fact`. For anything else it decides, then logs `decided: X (because Y)`.
3. **A stop names its class.** The gate rejects a `BLOCKED` log line with no `[ask: class]`.
4. **A reviewer sits before every send.** The Deming bot checks drafts and turns the owner's repeated answers into rules. Gate metric: stops with no class.
5. **Deterministic first.** A step a rule can decide goes to a script (0 tokens). The bot keeps only judgement.
6. **Every bot has a kill rule.** It names the evidence that stops the bot. A bot with no accepted work for 4 weeks goes to the Retire list.

## Names
The ops bots carry the name of an author. The name is a label for one idea, so a log line such as `Deming: PASS` tells you the rule before you open a file.

| Bot | Idea borrowed |
|---|---|
| Deming | Quality is built into the process, not checked at the end |
| Goldratt | Order all work by the bottleneck |
| Meadows | Find the leverage point, not the symptom |
| Munger | Invert, check the incentives, do the money math |
| Engelbart | Augment the team's capability |
| Simon | Satisficing: one small job per bot |
| Chief | The butler: smallest useful structure |

Caveats: none of these people reviewed or endorsed this repo. One idea per name is a simplification, and I may read some authors wrong. The name does not do the work. The rule has to live in the bot's Description, its log and the check script. You can rename every bot; the template works the same.

## Start in 15 minutes
1. Click **Use this template**. Clone your copy.
2. Replace `<OWNER>` and `<TRACKER>` in `AGENTS.md`.
3. Create the bots you need from `bots/<slug>/block.md`. Start with **Chief** and **Deming**. Add the rest only when a real job needs them.
4. Paste each block's Description into the bot. Put `AGENTS.md` where the bot can read it.
5. Run `python3 scripts/check.py --self-test`, then `python3 scripts/check.py` after the first runs.

## What this does not do
- It does not include any sales bots, contacts, prompts for outreach, or client data.
- It makes no claim that it will make a bot team go viral, earn money or save a fixed number of hours. Measure your own.
- It does not replace a human who reads what goes out.

## Hints and tips
See [`hints/HINTS.md`](hints/HINTS.md). They come from public X posts (scan of 2026-10-26) and are credited by handle. Check each against current vendor docs before you rely on it.

## License
MIT. See `LICENSE`.
