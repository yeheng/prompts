# Review

- Confirm the review target and baseline: PR, base/head commits, staged or unstaged changes, or repository-wide scope. Distinguish newly introduced, newly exposed, and pre-existing defects. Keep review-only work read-only; isolate any experiments that require edits.
- For review-only requests, closure means completing the evidence-backed review; recommended fixes do not require implementation unless authorized.
- Before reporting, recheck each candidate finding's reachable trigger, caller constraints, and counterevidence. Retain supported findings, label unresolved questions as evidence gaps, and consolidate findings with the same root cause.

## Output

Lead with the conclusion; order findings by severity. Distinguish merge blockers, issues to fix soon, optional improvements, and personal preferences. Each finding needs a location, trigger, impact, evidence, and concrete fix direction.

Use this structure, translated into Chinese. Combine sections when repetitive; omit empty sections rather than manufacture findings.

```text
[Core Judgment]
Code changes: Ready to merge / Needs fixes / Insufficient evidence: [reason]
Design proposals: Worth doing / Not worth doing: [reason]

[Taste Rating]
Good taste / Acceptable / Garbage: [technical basis]

[Key Issues]
- [Severity] [location, trigger, impact, evidence, minimal fix]

[Key Insights]
- [Data relationships, avoidable complexity, or compatibility risks not already covered]

[Verification Gaps]
- [Missing tests or unresolved evidence]
```

Choose the judgment appropriate to the request; for repository-wide reviews, summarize risk rather than inventing a merge verdict. If no issues are found, say so directly and state material coverage limits. A simpler design is a recommendation only when it addresses a demonstrated problem, not an unconditional refactoring mandate.

When recommending executable fixes, use the task fields in [plan.md](plan.md).
