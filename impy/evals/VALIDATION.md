# Behavioral Validation

Read only when maintaining or evaluating the skill. The suite defines seven development cases: three review cases plus user-edit preservation, blocked verification, severity calibration, and review-only scope. Definition is not execution evidence; consult saved reports for actual runs and their limitations. Parallel integration is not covered.

## Plan and Extend Cases

- Inspect the requested change, existing cases, and previous results. During an authorized evaluation or skill update, proactively add focused cases for affected behavior or demonstrated coverage gaps; no separate confirmation is needed for local, reversible fixture additions within scope. Ordinary code-review work does not authorize extending or running this suite.
- Start small. Prefer realistic incidents and minimal reproductions over many trivial variants. Cover both desired behavior and plausible mistakes, including correct code that must not be flagged.
- Relevant extensions include surgical fixes preserving unrelated edits, blocked checks reported as incomplete, justified severity, and independent versus coupled parallel tasks. Add only cases relevant to the evaluation; this list is not an obligation to build a large suite.
- Each case in `evals.json` needs a unique ID, a realistic prompt, input paths, and expected outcomes supported by code, tests, or documented requirements. Define base/head roles and necessary caller or production context. Keep conclusions open where requirements are unknown.
- Freeze acceptance checks before scored comparisons. Treat cases used to tune the skill as development cases; keep separate held-out cases for confirmation. Do not weaken expectations merely to make a run pass. Investigate newly discovered facts and document corrections.

## Execute Without Answer Leakage

1. Snapshot the skill and inputs; record model/configuration, tools, permissions, and test commands. Resolve fixture paths relative to the skill root.
2. Prepare a fresh context and isolated workspace for each case, arm, and trial. Compare the current skill with no skill or a frozen previous version under equivalent conditions.
3. Give executing agents only the task prompt, raw fixtures, base/head mapping, output location, and the evaluated skill where applicable. Do not pass `evals.json`, expected outcomes, grading instructions, historical reports, or the author's suspected diagnosis. Use a sanitized skill copy without eval artifacts when necessary. Prompt instructions alone are not an access-control boundary.
4. Preserve reports, available tool traces, final diffs, test outputs, duration, and token usage. Mark unavailable measurements explicitly. Store new run artifacts in a separate workspace outside the skill package; retain existing `results/smoke-1/` as historical evidence only.

## Grade and Iterate

- Check outcomes against evidence, not exact wording or section counts. Measure false positives, missed defects, attribution, scope preservation, severity justification, and truthful closure as relevant to each case.
- Use executable checks for behavior, file preservation, and test outcomes. Use an independent reviewer for semantic judgments; require evidence for each pass/fail and human adjudication for disputed findings. Do not give the reviewer an intended winning arm.
- Review execution traces as well as final answers. Separate environment failures from skill failures; neither justifies a claim that unverified behavior passed.
- Repeat trials before claiming consistency or improvement. A small single-trial suite is a smoke check, not a statistical benchmark. Report per-case results, variability, quality/cost tradeoffs, and untested capabilities.
- Change skill rules based on explicit user requirements, demonstrated failures, or evaluation evidence. Rerun affected cases and relevant regressions after changes; use held-out cases to check generalization. Do not keep adding instructions when a narrower correction suffices.

## Discovery and Loading

Use `discovery.json` for selection-stage cases. Give the selector only the catalog and request, not activation expectations. Run selected tasks separately with raw fixtures and capture actual reference reads. Extra guides may be appropriate when execution enters another phase; judge their purpose rather than matching exact read counts. Report activation false positives/negatives and unnecessary loading separately from task correctness. Unavailable traces mean unmeasured results. A generic development request without a Linus/Impy invocation does not meet the current description by itself.
