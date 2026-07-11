# Task: Review this repo's README and suggest 3 concrete improvements in a new file called UI_REVIEW.md. Do not modify existing 
- **Branch**: review/ui-test
- **Repo**: NuryeNigusMekonen/tenacious-engineering-standards
- **Context**: inline
- **Created**: 2026-07-11T07:06:24Z

## Description
Review this repo's README and suggest 3 concrete improvements in a new file called UI_REVIEW.md. Do not modify existing files, do not commit or push

## Subtasks
- [x] Read `README.md` plus supporting context (`mkdocs.yml`, `docs/` listing) to ground the review
- [x] Draft 3 concrete, specific README improvements with rationale and suggested snippets
- [x] Write findings to `UI_REVIEW.md` (new file, no existing files modified)
- [x] Cross-check suggestions against actual repo state (nav list) and correct any inaccuracies
- [x] Run verification (`make lint && make test`)
- [x] Commit, push branch, and open a PR per the current explicit user instruction
- [x] Write `PROOF.md` with results and exit

## Verification
Run: `make lint && make test`

## Instructions
1. Read this file to understand your task scope
2. If no subtasks are listed above, break this task into 3-7 concrete subtasks
   and add them as a checklist in this file before starting implementation.
   **Register each subtask in the database** so it can be tracked:
   `curl -s -X POST http://localhost:7700/api/task-db/1/subtasks -H 'Content-Type: application/json' -d '{"title": "<subtask title>"}'`
3. Implement each subtask in order, checking them off as you go
4. After completing each subtask, update its status:
   `curl -s -X PATCH http://localhost:7700/api/task-db/subtasks/{id} -H 'Content-Type: application/json' -d '{"status": "done"}'`
5. Run verification (see ## Verification above)
6. Create `PROOF.md` with: test results, files changed, brief walkthrough
7. Commit all changes and push: `git add -A && git commit -m 'feat: <summary>' && git push -u origin review/ui-test`
8. Create a PR: `gh pr create --base main --title '<task title>' --body 'Automated PR from agent task' --fill 2>/dev/null || true`
9. Exit when complete

## Do not
- Install system packages or tools (no apt, brew, npm -g, pip install). If a tool is missing, skip that step and note it in PROOF.md
- Modify files outside this worktree's scope
- Commit .env files
- Merge from other branches (let CI handle it)
- Spend time debugging infrastructure issues (SSH, auth, permissions) — report them and move on
