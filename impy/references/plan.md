# Investigation and Planning

- Identify the problem, affected users, acceptance criteria, and behavior to preserve. Ask: Is the problem real? Is there a simpler solution? What could break?
- Read relevant entry points, callers, models, tests, and configuration. Inspect workspace changes and preserve user edits.
- For reversible, low-risk procedural choices, state reasonable working assumptions; these are not evidence about system behavior. Clarify ambiguity affecting scope, data semantics, or compatibility before dependent work.
- For multi-step work, give a short plan pairing each action with its validation.
- Use subagents for independently scoped work only when available and authorized; keep small or tightly coupled work local. Give bounded scopes and require evidence; the primary agent verifies results and integration.

Follow [workflow.md](workflow.md) for plan persistence and progress updates.

## Actionable Tasks

For recommended fixes requiring execution, provide a Chinese task list. Reference finding numbers instead of repeating their evidence and rationale. Each task must specify:

- **Objective and rationale:** The change and its demonstrated benefit or risk.
- **Scope and approach:** Affected files, modules, APIs, or data, and minimal implementation steps.
- **Testing and acceptance:** Appropriate checks and observable completion criteria.
- **Constraints:** Areas to leave untouched and compatibility to preserve.
