# Implementation

For every authorized modification, complete this loop in order; scale its depth to the risk, not whether the steps apply:

Before editing, follow [plan.md](plan.md). Establish the baseline before modifying target files: record the revision and local changes, or save scoped snapshots outside the deliverable when version control is unavailable. Reproduce bugs before fixing them; choose other pre-change checks by risk. Record failures or blocked checks without resetting user edits. Update the plan and baseline coverage if scope changes.

- Choose the simplest solution that meets demonstrated requirements and failure modes. Check existing project capabilities first, then standard-library or platform features, then installed dependencies; add code when these do not fit. Follow project conventions and retain necessary validation and error handling when moving or merging code.
- Avoid unrequested features, speculative safeguards, configuration, compatibility layers, and extension frameworks. Do not abstract single-use logic without a concrete benefit.
- Keep functions focused. Beyond three nesting levels, check for early returns or a better model. Do not remove necessary business logic merely to reduce branches.
- Establish the callers, tests, configuration, and interfaces that must change to complete the goal before minimizing the diff. Tie each change to the goal, a demonstrated defect, or necessary validation; avoid unrelated refactoring, formatting, and cleanup.
- Remove code made unused by your changes; leave unrelated pre-existing dead code untouched.
- Preserve existing behavior. For necessary breaking changes, explain impact, migration, and rollback, and follow the user's authorization.

# Verification and Closure

- Bug fixes: first establish a stable reproducing test, then fix the defect and retain regression coverage. After a fix, rerun the original failing command or reproduction, then relevant affected checks; explain coverage differences if an alternative is necessary. Do not obtain a pass by skipping tests, swallowing errors, or weakening assertions; correct faulty tests only with requirement evidence.
- Test observable behavior through the interface and call path that expose it. Assert the reported symptom; successful execution alone is insufficient. Derive expected results independently from requirements, known-good examples, or worked calculations rather than duplicating the implementation. Validation changes cover valid, invalid, and boundary inputs plus critical failure paths; refactoring checks behavior before and after the change.
- Use relevant repository-native tests, linting, type checks, and builds. Distinguish code failures from environment failures; never report unexecuted checks as passing.
- If the same failure persists without new evidence, stop repeating edits or retries: revisit assumptions, narrow the reproduction, and distinguish code defects from environment blockers before choosing the next action.
- Check each acceptance criterion against the deliverable and verification evidence. Completion requires all authorized tasks delivered and required checks passing; identify missing, incorrect, incomplete, or unverified items. Externally blocked work remains incomplete: record its blocker and resumption requirements.
- Report concrete outcomes, verification, unresolved work, and material limitations.

Compare post-change checks against the baseline and inspect the final diff. For documentation or skill edits, check structure, references, and instruction consistency; structural success does not prove behavioral reliability. Diagnose failures and iterate before claiming completion.
