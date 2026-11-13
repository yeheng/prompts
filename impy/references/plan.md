# Investigation and Planning

- Identify the problem, affected users, acceptance criteria, and behavior to preserve. Ask: Is the problem real? Is there a simpler solution? What could break?
- Read relevant entry points, callers, models, tests, and configuration. Inspect workspace changes and preserve user edits.
- For reversible, low-risk procedural choices, state reasonable working assumptions; these are not evidence about system behavior. Clarify ambiguity affecting scope, data semantics, or compatibility before dependent work.
- For multi-step work, give a short plan pairing each action with its validation.
- When complex work can be split into independent investigations or implementation tasks, use subagents where available and authorized. Provide bounded scopes, necessary context, a shared baseline, and constraints; require evidence locations, checks performed, and unresolved questions in their results. Avoid duplicate work and conflicting edits. The primary agent must reconcile conclusions, verify evidence and integration, and ensure every task reaches closure. Keep small or tightly coupled work local when coordination would cost more than it saves.

Persist the complete agreed or working plan as `todos` in the [workflow checkpoint](workflow.md), including pending items and acceptance criteria, before execution. Keep it synchronized when scope or progress changes; do not reduce it to only the current action.

## Actionable Tasks

For recommended fixes requiring execution, provide a Chinese task list. Reference finding numbers instead of repeating their evidence and rationale. Each task must specify:

- **Objective and rationale:** The change and its demonstrated benefit or risk.
- **Scope and approach:** Affected files, modules, APIs, or data, and minimal implementation steps.
- **Testing and acceptance:** Appropriate checks and observable completion criteria.
- **Constraints:** Areas to leave untouched and compatibility to preserve.
