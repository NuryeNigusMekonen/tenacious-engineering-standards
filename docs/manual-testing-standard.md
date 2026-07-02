# Manual Testing

Manual testing is the human validation gate before a change moves between environments. A tester or QA
engineer, with Tech Lead oversight, uses the software against stated criteria and records what happened.

It comes after the change is built and self-reviewed (see the
[Engineering Baseline](engineering-baseline-standard.md)) and before promotion through the
[Branch Strategy](branching-standard.md).

## What manual testing proves

Manual testing must prove that the change works for the user, not only that the code runs.

| Area | What to check |
| --- | --- |
| **Functional behavior** | The feature does what the requirement, ticket, or acceptance criteria says it should do. |
| **End-to-end flow** | The user journey works across screens, services, integrations, and data changes. |
| **Regression risk** | Existing important behavior still works after the change. |
| **Usability and visual fit** | The experience is understandable, accessible enough for the context, and not visually broken. |
| **LLM / RAG behavior** | Model outputs satisfy agreed criteria for accuracy, relevance, grounding, safety, and tone. |

Every feature is checked across all areas that apply. Do not sign off a deterministic path and skip the
model-driven part, or validate the model output while ignoring the surrounding user journey.

## When manual testing is required

Manual testing is required before promotion from `dev` to `staging` and before release from `staging` to
`production`, unless an automated suite already covers the exact release gate and the release owner accepts
the remaining risk.

Manual testing is especially required when:

- the feature is new or still changing;
- the expected result requires human judgment;
- the change affects a user journey, integration, data flow, or AI/LLM behavior;
- there is no trusted automated coverage yet;
- a defect fix needs retesting.

## Minimum test case format

A manual test case is a small, repeatable check. It does not need to be bureaucratic, but it must be clear
enough for another person to run.

| Field | Required content |
| --- | --- |
| **ID / Name** | A short identifier, such as `TC-LOGIN-001` or `Valid login redirects to dashboard`. |
| **Requirement or ticket** | The story, issue, requirement, or risk the test covers. |
| **Preconditions** | The state needed before testing, such as user role, data, environment, or account setup. |
| **Steps** | The exact actions to perform. |
| **Expected result** | What should happen if the software is correct. |
| **Actual result** | What happened during execution. |
| **Status** | `Pass`, `Fail`, `Blocked`, or `Risk Accepted`. |
| **Evidence** | Screenshot, recording, log, response payload, report link, or written observation. |

## Standard records and tools

Each project chooses the exact tool during setup, but the records below are mandatory. A team may use a
test management tool, the project tracker, GitHub issues, Basecamp, or version-controlled Markdown as long
as the required information is easy to find during review and release.

| Record | Required use | Acceptable tools |
| --- | --- | --- |
| **Test cases** | Store the checks that prove a feature, defect fix, or release path. | Test management tool, project tracker, GitHub issues, Markdown in the repo. |
| **Execution results** | Record pass/fail/blocked/risk status for each planned check. | Test run record, PR checklist, release tracker, spreadsheet only if linked from the release record. |
| **Defects** | Track failed behavior from discovery to verified closure. | Project tracker, GitHub issues, Basecamp, client-approved defect tool. |
| **Evidence** | Preserve proof behind the result. | Screenshots, screen recordings, logs, API payloads, CI links, exported reports. |
| **Frozen task set** | Version LLM/RAG inputs and criteria. | Repository file, eval dataset, or test management tool with exportable records. |

Testing records must link back to the requirement, issue, PR, or release they support. If someone cannot
trace what was tested and why, the record is not complete.

## Defect report format

Any failed manual test that is not fixed immediately must be logged as a defect.

| Field | Required content |
| --- | --- |
| **Summary** | One clear sentence describing the failure. |
| **Environment / build** | Where it happened, including branch, version, device, browser, or API environment. |
| **Steps to reproduce** | Exact actions or request payload needed to trigger the issue. |
| **Expected result** | What should have happened. |
| **Actual result** | What happened instead. |
| **Evidence** | Screenshot, recording, log, response, or trace. |
| **Severity** | Impact on the system or user: `Critical`, `High`, `Medium`, or `Low`. |
| **Priority** | Business urgency: `Urgent`, `High`, `Medium`, or `Low`. |
| **Owner / status** | Who owns the next action and whether it is new, in progress, fixed, retest, closed, or deferred. |

## How to run manual testing

1. **Confirm the scope.** Identify the changed feature, affected user journeys, integrations, data, and
   known risks.
2. **Write or update test cases.** Cover the happy path, negative path, boundary cases, and important
   regression paths.
3. **Prepare test data.** Use safe test accounts and masked or synthetic data. Do not copy production data
   into lower environments without approval.
4. **Run the tests in the target environment.** Use the build that is being promoted, not a local or stale
   build.
5. **Record results and evidence.** Every case must have a status and enough evidence to support the
   decision.
6. **Log defects immediately.** Include steps to reproduce, expected vs. actual behavior, environment,
   evidence, severity, and priority.
7. **Retest fixes.** A defect is not closed until the fix is verified and any needed regression check has
   passed.
8. **Give a promotion recommendation.** State `go`, `hold`, or `go with accepted risk`.

## Ownership

| Role | Responsibility |
| --- | --- |
| **Tester / QA Engineer** | Designs, runs, and records manual test cases, logs defects, and recommends whether the change is ready for promotion. |
| **Tech Lead** | Confirms the manual test scope is sufficient for promotion and accepts residual technical risk. |

## LLM and RAG checks

For features with LLM or RAG behavior, manual testing must use a fixed set of realistic inputs with agreed
pass/fail criteria. This is the **frozen task set**.

The frozen task set is required because model output is often judgment-based rather than exact. It turns
"looks good" into a repeatable evaluation.

1. **Collect real inputs.** Use 20-40 representative prompts, messages, documents, calls, or records.
2. **Define acceptance criteria.** State what a good answer must include, avoid, cite, classify, or decide.
3. **Freeze the set.** Keep it version-controlled with the product.
4. **Run it before promotion.** Record pass, fail, or risk for each input.
5. **Grow it deliberately.** Add new inputs when behavior expands or a new failure mode is found.

The frozen task set later becomes the handoff into the
[Automation Testing](automation-testing-standard.md) standard.

## Exit criteria

Manual testing is complete only when:

- all planned test cases have a recorded result;
- all failed or blocked cases have a linked defect, explanation, or accepted risk;
- no critical user journey is untested without explicit risk acceptance;
- LLM/RAG features have been checked against the frozen task set where applicable;
- the tester has recorded a clear recommendation: `go`, `hold`, or `go with accepted risk`.

!!! note "Not enough"
    "Looks fine" is not a test result. A promotion decision must be tied to stated criteria and recorded
    evidence.
