# Privacy gate and browser rules

## What stays out of the repo
Idea: a repo is a shared, copyable surface. Treat it as public even when it is private.
- Lead, client and contact details stay in your tracker or CRM. Never in the repo.
- Never in a repo: secrets, keys, webhook URLs, addresses, phones, emails, family or health data. The check script should reject a phone, email or key-like string in `bots/*/memory.md` and `routines.md` (add the regex for your data).
- Proof numbers and prices come only from ONE source file the owner keeps. A bot that cannot find the number asks. It does not round, combine or remember.

## Browser rules
Idea: match the risk to the platform. Write `ops/browser-rules.md` for your own tolerance. Example split:
- A platform where you accept the ban risk: bots may act in a browser.
- A platform where your personal account is at stake: zero bot actions, drafts only, a human sends.
- Read the browser rules before every browser or computer-use step.
