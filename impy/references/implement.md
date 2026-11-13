# Implementation

For every authorized modification, complete this loop in order; scale its depth to the risk, not whether the steps apply:

Before editing, follow [plan.md](plan.md) and persist the full todo list. Establish the baseline before modifying target files: record the revision and local changes, or save scoped snapshots outside the deliverable when version control is unavailable. Run relevant existing checks and reproduce bugs first; record failures or blocked checks without resetting user edits. Update the plan and baseline coverage if scope changes.

- Choose the simplest, most direct solution that robustly handles demonstrated requirements, boundaries, and failure modes. Add complexity only when evidence shows the simpler approach is insufficient.
- Avoid unrequested features, speculative safeguards, configuration, compatibility layers, and extension frameworks. Do not abstract single-use logic without a concrete benefit.
- Keep functions focused. Beyond three nesting levels, check for early returns or a better model. Do not remove necessary business logic merely to reduce branches.
- Tie each change to the goal, a demonstrated defect, or necessary validation. Reuse project implementations and conventions; avoid unrelated refactoring, formatting, and cleanup.
- Remove code made unused by your changes; leave unrelated pre-existing dead code untouched.
- Preserve existing behavior. For necessary breaking changes, explain impact, migration, and rollback, and follow the user's authorization.



# Verification and Closure

- Bug fixes: first establish a stable reproducing test, then fix the defect and retain regression coverage.
- Validation changes: cover valid, invalid, and boundary inputs plus critical failure paths. Refactoring: verify behavior before and after the change.
- Use relevant repository-native tests, linting, type checks, and builds. Distinguish code failures from environment failures; never report unexecuted checks as passing.
- Every authorized task must close with its deliverable finished, required checks passing, failures resolved, and acceptance criteria supported by observable evidence. Plans, partial implementations, or passing subsets of required checks are not completion. The assignment is complete only when all its tasks close.
- Track unfinished tasks. If externally blocked, report the affected task, blocker, and resumption requirements; keep it explicitly incomplete.
- Report changes or findings, validation, outstanding tasks, and material limitations.

Compare post-change checks against the baseline and inspect the final diff. For documentation or skill edits, check structure, references, and instruction consistency; structural success does not prove behavioral reliability. Diagnose failures and iterate before claiming completion.
