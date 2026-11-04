# Principles: the idea behind each rule

Each rule has three parts: the **rule**, the **idea** behind it (and whose), and **what breaks without it**. If you change a rule, change it knowing the third part.
The authors did not review this. One idea per author is a simplification.

## 1. One bot, one job
- Idea: satisficing and bounded rationality (Herbert Simon). A small agent with a small job fits in its context and in your head.
- Breaks without it: a bot with five jobs does all five badly, and you cannot say which rule it dropped.

## 2. Six stop classes, and nothing else needs a yes
- Idea: decision rights. Decide where a decision lives before the decision comes.
- Breaks without it: the bot asks about everything and you become the bottleneck, or asks about nothing and sends something you never saw.

## 3. A stop names its class
- Idea: measure the process, not the person (Deming). A stop with no class is a defect you cannot count.
- Breaks without it: you cannot tell which rule is missing. With the class, a repeated stop becomes a standing rule.

## 4. A reviewer before every send
- Idea: improvement loop (Deming's plan, do, check, act). The reviewer also feeds a lessons register, so the same defect does not return.
- Breaks without it: a writer bot sends what it believes. The reviewer checks claims against the source.

## 5. Deterministic first
- Idea: use the cheapest tool that is correct. A rule can count, diff and route; only judgement needs a model.
- Breaks without it: you pay model tokens for work a script does for free, and the answer is less reliable.

## 6. Order work by the bottleneck
- Idea: Theory of Constraints (Goldratt). The output of the whole system equals the output of its constraint. Improving anything else is waste.
- Breaks without it: bots stay busy on easy work while the one stage that limits revenue waits.

## 7. Fix structure, not symptoms
- Idea: leverage points (Donella Meadows). The higher the leverage point, the more the system resists the change, so propose ONE structural change with a check date.
- Breaks without it: the same fix repeats every week and the cause stays.

## 8. Every spend and every routine is questioned
- Idea: invert, and check the incentives (Charlie Munger). Ask what makes this fail and who gains from the current setup.
- Breaks without it: routines that change nothing keep running and burn the allowance. See `ops/usage-and-cost.md`.

## 9. Watch the platform, turn gaps into cards
- Idea: augment the team, and improve the way you improve (Douglas Engelbart). The team's own methods are a thing to upgrade.
- Breaks without it: a vendor ships a feature or a limit and the team learns by failing.

## 10. Every bot has a kill rule
- Idea: a fleet is a portfolio. Default for a new bot is "do not create one". Keep, improve, merge or retire, on evidence.
- Breaks without it: bots only accumulate.

## 11. One batch per handoff
- Idea: batch size is a cost. One message with the whole batch, one re-check after every fix.
- Breaks without it: ten messages for ten findings, ten wake-ups, ten times the usage.

## 12. Plain text in every outward draft
- Idea: simplified technical English (ASD-STE100): short sentences, common words, one idea per sentence, active voice.
- Breaks without it: drafts read as machine text, and the reviewer spends its pass on style.
