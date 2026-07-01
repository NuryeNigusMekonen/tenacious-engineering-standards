# Engineering Baseline

This standard ensures no engineer ships work that fails on basics. It is the **first gate in the daily
build loop** — everything an engineer does on their own change before requesting review from anyone else.

There are two sets of checks, both performed by the engineer on their own work:

1. **Automated review** — tooling and AI surface mechanical and obvious issues.
2. **Human self-review** — the engineer's own judgment about whether the change actually solves the problem
   and is fit to ship.

Run **both** before opening a PR into a protected branch.

## Automated review

What you check using formatters, linters, AI assistants, and code review tools **before pushing**.

**Code review tool.** Default: **CodeRabbit free tier.** Run it locally before your code reaches anyone
else, either via the CodeRabbit CLI or the CodeRabbit VS Code extension. Both are free, run on your
machine, and don't require opening a pull request.

**AI assistants.** All Tenacious engineers use Claude Code, Cursor, GitHub Copilot, Kiro, or similar.
Three rules:

- **You own every line you commit.** Read it, understand it, test it. "The AI wrote it" is not an answer
  to a review comment.
- **AI-generated changes get stricter self-review, not looser.**
- **Project conventions live in a checked-in file the assistant reads automatically.** `AGENTS.md`
  (`CLAUDE.md` or similar) at the repo root is the cross-tool standard — Claude Code, Cursor, Copilot,
  Windsurf and others all read it. Add tool-specific files only when you need behavior beyond what
  `AGENTS.md` covers.
- **When embedded with a client, follow their AI policy.**

## Human self-review

Four questions, in order. Use them as the lens for your final pass on your own change.

1. **Does the change match the requirement?** Open the linked ticket. Read the acceptance criteria.
   Confirm the code solves the *stated* problem — not a related problem, not what you assumed it was. A
   change that passes tests but doesn't solve the stated problem is the most common form of latent defect.
2. **Does it introduce risk outside its stated scope?** Authentication, authorization, shared utilities,
   data migrations, billing, personal data, and prompt changes that affect other agent flows all get
   stricter scrutiny — regardless of how small the diff is.
3. **Is it maintainable by someone else?** Read it as if you'd never seen it before. Naming, structure,
   comments where intent is non-obvious, no clever code. The future maintainer was not in the room when
   this was written.
4. **Do the tests prove what they claim?** Tests that pass aren't the same as tests that mean something.
   Check that new tests exercise the actual behavior, fail when the behavior breaks, and aren't just
   asserting that mocks were called.

## The baseline checklist

Run this before requesting review or opening a PR. Mark each item **pass**, **fail**, or **risk**; record
fixes or deferrals in notes.

| Category | Items to confirm |
| --- | --- |
| **Code hygiene** | Code is auto-formatted to project style · Linter passes with no new warnings · No dead code, unused imports, or commented-out blocks |
| **Tests & build** | Relevant tests pass locally · Project builds, compiles, or renders cleanly · New code carries proportionate tests |
| **Secrets & data** | No credentials, tokens, or API keys in the diff · No internal URLs, dev emails, or debug labels in user-facing surfaces · No real personal or client data committed |
| **Dependencies & inputs** | New dependencies are justified and scanned · User input is validated; queries don't interpolate raw input · Authentication and authorization checks present where required |
| **Automated review tool** | CodeRabbit (or equivalent) has run on the change · Bugs it flagged are fixed · Suggestions are accepted or dismissed with a reason |
| **AI-assisted code** | Every AI-generated line is read and understood · Project rules file (e.g. `AGENTS.md`) updated if conventions changed |
| **Requirement match** | Linked ticket reopened and acceptance criteria reread · Code solves the stated problem, not an adjacent one · All acceptance criteria covered |
| **Risk surface** | Sensitive areas (auth, shared utils, migrations, billing, PII, prompts) identified · No silent change in behavior outside the stated scope |
| **Maintainability** | Names communicate intent · Structure is locatable — a future reader can find what they need · Non-obvious decisions have a brief comment explaining why |
| **Tests prove behavior** | New tests fail when the behavior breaks · Tests assert outcomes, not just that mocks were called · New env vars added to example config; new dependencies justified |

!!! note "This is your gate, not someone else's"
    The baseline is done by the engineer, on their own change, before anyone else sees it. Passing it is
    what earns the right to open a PR.
