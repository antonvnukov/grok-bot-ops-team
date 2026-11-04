# Principles: the idea behind each rule

How the names were chosen: for each bot, one key principle of the person it is named after. Six were discussed and chosen when the original team was built: Beer, Simon, Hashimoto, Deming, Goldratt, Munger. Meadows and Engelbart were only "named after X"; their ideas here are my mapping and are marked so.

Each rule has three parts: the **rule**, the **idea** behind it (and whose), and **what breaks without it**. If you change a rule, change it knowing the third part.
The authors did not review this. One idea per author is a simplification.

## 1. One bot, one job
- Idea (Herbert Simon, chosen for the original team): "good enough", not "ideal" (satisficing). It holds back needless bots. His near-decomposability (loosely coupled parts) fits too.
- Breaks without it: a bot with five jobs does all five badly, and you cannot say which rule it dropped.

## 2. Six stop classes, and nothing else needs a yes
- Idea: decision rights (no single author). Decide where a decision lives before the decision comes.
- Breaks without it: the bot asks about everything and you become the bottleneck, or asks about nothing and sends something you never saw.

## 3. A stop names its class
- Idea: measure the process, not the person (Deming). A stop with no class is a defect you cannot count. Watch the trend; do not set a numeric target (Deming opposed quotas).
- Breaks without it: you cannot tell which rule is missing. With the class, a repeated stop becomes a standing rule.

## 4. A reviewer before every send
- Idea (W. Edwards Deming, chosen for the original team): the plan, do, check, act loop, and "fix the system, not the person". Honest trade-off: Deming said to cease dependence on inspection, and this reviewer is an inspection gate. We keep it because a bot send cannot be undone, and we make it feed a lessons register so the process improves and the inspection shrinks.
- Breaks without it: a writer bot sends what it believes. The reviewer checks claims against the source.

## 5. Deterministic first
- Idea: use the cheapest tool that is correct (no single author). A rule can count, diff and route; only judgement needs a model.
- Breaks without it: you pay model tokens for work a script does for free, and the answer is less reliable.

## 6. Order work by the bottleneck
- Idea (Eliyahu Goldratt, chosen for the original team): Theory of Constraints, one bottleneck at a time, and "the goal of the business is to make money". The throughput of the whole system equals the throughput of its constraint. Improving elsewhere does not raise throughput. Use the five focusing steps: identify, exploit, subordinate, elevate, repeat. (The rank formula in Goldratt's block is this repo's own.)
- Breaks without it: bots stay busy on easy work while the one stage that limits revenue waits.

## 7. Fix structure, not symptoms
- Idea (Donella Meadows; my mapping, not discussed in the original setup): leverage points. The higher the leverage point, the more the system resists the change, so propose ONE structural change with a check date. Meadows also warns that people often push a leverage point the wrong way: state the direction and the side effect.
- Breaks without it: the same fix repeats every week and the cause stays.

## 8. Every spend and every routine is questioned
- Idea (Charlie Munger, chosen for the original team): inversion and a margin of safety. Ask what makes this fail, and keep reserve.
- Breaks without it: routines that change nothing keep running and burn the allowance. See `ops/usage-and-cost.md`.

## 9. Watch the platform, turn gaps into cards
- Idea (Douglas Engelbart; my mapping, not discussed in the original setup): bootstrapping: improve the process that improves your process. Watching the platform is how the team finds its next upgrade.
- Breaks without it: a vendor ships a feature or a limit and the team learns by failing.

## 10. Every bot has a kill rule
- Idea: a fleet is a portfolio. Default for a new bot is "do not create one". Keep, improve, merge or retire, on evidence.
- Breaks without it: bots only accumulate.

## 11. One batch per handoff
- Idea: batch size is a cost (lean manufacturing, Donald Reinertsen). One message with the whole batch, one re-check after every fix.
- Breaks without it: ten messages for ten findings, ten wake-ups, ten times the usage.

## 12. Plain text in every outward draft
- Idea: simplified technical English (ASD-STE100): short sentences, common words, one idea per sentence, active voice.
- Breaks without it: drafts read as machine text, and the reviewer spends its pass on style.

## 13. Access, secrets and infrastructure as code
- Idea (Mitchell Hashimoto, chosen for the original team): treat access, secrets and infrastructure as code (the idea behind Vault and Terraform): written down, versioned, reviewable, never in a Description or a chat.
- Breaks without it: keys sit in prompts and chats, nobody knows which bot can reach what, and a restart loses the setup.
