# Hints and tips for a Grok bot team

Source: a scan of public X posts, 2026-09-26 to 2026-10-26. Credits are the accounts that posted the tip. Many posts link to X Articles that could not be read, so only the post text is cited. Tips marked "single source" were not checked against vendor docs. Vendor features change: verify first.

## Where things belong
**One home per kind of information.** Job rules go in the bot's description. Today's task goes in chat. Taste goes in learned memory. A procedure goes in a skill. Timing goes in a routine. Team rules go in one shared folder. Prices and features stay in the live source. "Don't remember the answer. Remember where to get it." ([@GrokBotRadar](https://x.com/GrokBotRadar/status/2109769581837606967))
A rule buried in a three-week-old chat "is a rule waiting to get missed". ([@GrokBotRadar](https://x.com/GrokBotRadar/status/2112356169092366827))

**The description holds durable rules and is read every turn.** Grok's own account says the Description field (not a separate system prompt) carries durable role rules, and skills are saved by asking the bot or with Teach a task. ([@grok](https://x.com/grok/status/2106969676773294240)) Safety rules belong there; do not rely on memory for anything important. ([@CarolinaDill](https://x.com/CarolinaDill/status/2110049188524216756)) A job title alone is not enough. ([@silentguyy66](https://x.com/silentguyy66/status/2108957020187468171))

## Practical tricks
1. **Teach a task, then make it a skill, then a routine.** Record a short screen session, review the draft skill, add rules for empty or changed pages, run it from a routine. ([@orvexus](https://x.com/orvexus/status/2113991187514216452))
2. **Import a template instead of writing a prompt.** The vendor ships its own bot templates in the marketplace. ([@hammertime_one](https://x.com/hammertime_one/status/2112881493575917921))
3. **Have your main bot read the official guides** and recommend changes for the other bots. ([@KevinMacCauley](https://x.com/KevinMacCauley/status/2111493782172819551)) In this repo that is the Engelbart bot's job.
4. **A set of tricks from the vendor's videos**: a house rule so emails cannot give the bot orders; an auto-review the bot cannot loosen; logins the bot uses but cannot read; adding a teammate's bot. ([@0xNotFounder](https://x.com/0xNotFounder/status/2114302418997379349))
5. **Linking a SuperGrok or X Premium+ account in Settings may give a separate usage pool.** Single source, not checked against pricing docs. ([@finebutwhy](https://x.com/finebutwhy/status/2108567165821657403))
6. **The bot's computer is a full VM.** You can install tools on it. ([@ZeusRadls](https://x.com/ZeusRadls/status/2109026797203415425))
7. **Plan with a strong model, let the bot orchestrate cloud coding agents for code.** ([@solpoyo](https://x.com/solpoyo/status/2107623045552537972)) On a shared plan this saves turns, not necessarily usage. ([@cursor_ai](https://x.com/cursor_ai/status/2109783879490191502))
8. **Voice note instead of a wall of text.** ([@Sdefendre](https://x.com/Sdefendre/status/2108034485719622118))
9. **Let agents file feedback through the in-app feedback tool when they hit a bug.** ([@davis7](https://x.com/davis7/status/2108756950641254490))
10. **Approvals expire, so a night job that waits for a yes dies waiting.** End such a job with a card or a handoff. Verbs that never run without you: send, publish, pay, delete, sign, trade. ([@AleiahLock](https://x.com/AleiahLock/status/2111861644640817476)) This repo's six stop classes are the same idea.
11. **Trust one agent before you spawn many. Use a verification skill so you are not the bottleneck, and a judge agent.** ([@silentguyy66](https://x.com/silentguyy66/status/2104207220724359563))

## What we learned running a team
- **Long rules in descriptions and long chats cost you.** Move rules to the repo, keep descriptions short, point to the files.
- **Re-reading is the biggest usage cost.** A bot that re-reads a long chat each run wastes the allowance. Put a script in front of the routine; wake the bot only when something changed.
- **One batch per handoff.** One message with all findings beats one message per finding.
- **A reviewer bot before every send catches unsupported details.** Keep it, and log what it changed.

## Weak evidence: ignored
"10 repos that make your bot 10x" lists. They are engagement bait with no evidence for this platform. This repo makes no such claim.
