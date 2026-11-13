# Workflow Persistence

The complete planned todo list is the core of the checkpoint, not a tool-call log. Use one plain JSON file following [workflow.schema.json](workflow.schema.json); see [workflow.example.json](workflow.example.json). No database or workflow engine is needed.

## Contents and updates

- Save all currently known plan items in the ordered `todos` array before executing the plan, including pending work. Each item has a stable ID, action, status, acceptance criterion, update time, and a short optional note. If investigation is needed to build the plan, start with that todo and expand the list before dependent work.
- Update the relevant todo when starting, completing, blocking, or revising it. Keep pending items until resolved; use `skipped` with a reason for work removed from scope. Add newly discovered required work rather than silently omitting it.
- Keep outcomes, failures, and evidence paths in concise notes. Do not create entries for individual tool calls or maintain detailed execution histories. Retries update the same todo; retain only important failure context. Do not store secrets or hidden reasoning.
- Workflow fields summarize the goal, workspace, constraints, baseline, status, timestamps, and concrete `next_action`. Baseline can be empty until investigation establishes it. `next_action` points to the next unresolved task or its recovery action, and is null on completion or cancellation.
- Use RFC 3339 timestamps with timezone. IDs must be unique. Mark a todo completed only when its acceptance criterion has evidence; put the result or evidence reference in its note. A completed workflow has only completed or explicitly justified skipped todos and no unresolved required work. Validate the JSON and these cross-field rules with `python3 <skill-root>/scripts/workflow.py validate <checkpoint>` before saving a final checkpoint and before resuming. The validator checks recorded state, not whether evidence proves acceptance.

## Storage

For implementation, default to `.impy/workflows/<workflow_id>.json` in the workspace. For read-only work, default to `~/.impy/workflows/<workspace-key>/<workflow_id>.json`, where workspace-key is the first 16 hexadecimal characters of SHA-256 of the UTF-8 absolute, resolved workspace path. Tell the user the absolute path; do not change ignore rules solely for bookkeeping. Temporary storage must be identified as subject to cleanup. If saving fails, report the blocker rather than claiming resumability.

Write UTF-8 JSON to a sibling temporary file and atomically replace the checkpoint. Use one writer per workflow. Checkpoint writes do not themselves require todos.

## Resume and close

If the path is unknown, run `python3 <skill-root>/scripts/workflow.py find <workspace>` to search both default locations, including completed checkpoints. With multiple candidates, confirm the intended task instead of choosing blindly. For a custom or temporary location, the user must retain its path.

Load the checkpoint first and confirm the task, workspace, and current authorization. Recheck relevant files, baseline, and effects before resuming: a saved running todo does not prove its last operation succeeded or failed. Never blindly repeat side effects. Continue the first unresolved required todo, updating the plan if facts changed.

Before reporting, save actual progress, concise verification results, and the next action or explicit completion. Include the checkpoint path in the final response. Blocked work remains incomplete; the checkpoint does not replace tests or grant authorization.
