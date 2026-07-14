# Task: Summerize
- **Branch**: task/tenacious-engineering-standards-3499
- **Repo**: NuryeNigusMekonen/tenacious-engineering-standards
- **Context**: inline
- **Created**: 2026-07-14T04:31:39Z

## Description
Summerize

## Subtasks
- [x] Audit the repo to scope what "summarize" should apply to (README/index.md already have a one-sentence TL;DR and card summaries from prior tasks; a consolidated one-page digest of all 11 standards does not yet exist)
- [x] Read every doc in `docs/` in full to extract each standard's core, non-negotiable rule
- [x] Draft `STANDARDS_SUMMARY.md` at repo root: one-page digest with a one-line takeaway per standard plus the full core-rules list
- [x] Cross-check every line of the summary against its source doc for accuracy (no invented rules, no dropped nuance)
- [x] Run verification and record why `make lint && make test` doesn't apply to this repo
- [x] Write `PROOF.md` with results, files changed, and a walkthrough
- [ ] Commit, push, and open the PR

## Verification
Run: `make lint && make test`

## Instructions
1. Read this file to understand your task scope
2. If no subtasks are listed above, break this task into 3-7 concrete subtasks
   and add them as a checklist in this file before starting implementation.
   **Register each subtask in the database** so it can be tracked:
   `curl -s -X POST http://localhost:7700/api/task-db/7/subtasks -H 'Content-Type: application/json' -d '{"title": "<subtask title>"}'`
3. Implement each subtask in order, checking them off as you go
4. After completing each subtask, update its status:
   `curl -s -X PATCH http://localhost:7700/api/task-db/subtasks/{id} -H 'Content-Type: application/json' -d '{"status": "done"}'`
5. Run verification (see ## Verification above)
6. Create `PROOF.md` with: test results, files changed, brief walkthrough
7. Commit all changes and push: `git add -A && git commit -m 'feat: <summary>' && git push -u origin task/tenacious-engineering-standards-3499`
8. Create a PR: `gh pr create --base main --title '<task title>' --body 'Automated PR from agent task' --fill 2>/dev/null || true`
9. Exit when complete

## Do not
- Install system packages or tools (no apt, brew, npm -g, pip install). If a tool is missing, skip that step and note it in PROOF.md
- Modify files outside this worktree's scope
- Commit .env files
- Merge from other branches (let CI handle it)
- Spend time debugging infrastructure issues (SSH, auth, permissions) — report them and move on
