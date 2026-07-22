# Collaboration Runtime Contract

This reference describes the collaboration surface that is callable in the current Codex runtime. Treat the runtime-provided tool schema as authoritative if it changes. Do not infer capabilities from older repository prose.

## Callable Tools

Call collaboration tools directly from the parent agent. They are not available through the `tools` object inside `functions.exec`.

- `spawn_agent({ task_name, message, fork_turns? })` creates one bounded child agent. `task_name` uses lowercase letters, digits, and underscores. `fork_turns` is `"all"`, `"none"`, or a positive integer encoded as a string and controls how much conversation context is copied to the child.
- `send_message({ target, message })` delivers a message to an existing agent without starting a new turn.
- `followup_task({ target, message })` gives an existing agent another task. It starts a turn when the target is idle and otherwise delivers the task at a safe message boundary.
- `wait_agent({ timeout_ms? })` waits for a mailbox or status update. It is a synchronization aid, not a source of worker-result content by itself.
- `interrupt_agent({ target })` interrupts the target's current turn. The agent remains available for later messages or follow-up tasks.
- `list_agents({ path_prefix? })` reports the live agent tree and should be used to discover current status and capacity.

There is no callable `close_agent` operation in this runtime. There is no worker-specific model or reasoning argument on `spawn_agent`. Do not document or request controls that the active schema does not expose.

## Context And Filesystem Semantics

`fork_turns` forks conversation context only. It does not create a forked filesystem, branch, index, or worktree.

All agents in the same collaboration tree share the current working directory and filesystem. A worker's file edit is visible to the parent and sibling agents immediately. Git branch changes, index changes, commits, and worktree metadata are shared state too.

Apply these coordination rules:

- default explorers, reviewers, and validators to read-only
- give simultaneous writers disjoint file scopes
- serialize work that touches the same file, interface, Git index, or branch
- create a separate Git worktree before launch when a worker needs branch or checkout isolation, and give the worker that exact path
- inspect the shared diff and rerun validation after the last writer finishes
- never describe a worker result as waiting to be landed from an invisible fork; acceptance means reviewing the changes already present in the designated shared worktree

## Capacity And Lifecycle

Concurrency is supplied by the active runtime and can vary. Use `list_agents` to inspect current agents and available scheduling room. Do not hardcode a universal worker count.

Use the smallest useful team. `spawn_agent` is for a new bounded role, `send_message` is for information that should not start a turn, and `followup_task` is for additional work that should run. Use `wait_agent` only when the parent cannot make useful progress without an update. Use `interrupt_agent` to stop an active turn, not as cleanup or deletion.

Completed and interrupted agents may remain addressable. Their presence is not evidence that another worker slot is available; rely on the runtime's current scheduling result and `list_agents` output.

## Parent Acceptance Responsibility

Shared state does not remove the parent's responsibility. The parent still owns task decomposition, non-overlapping writable scopes, acceptance criteria, status visibility, final diff review, validation, and the final user-facing verdict.

For writable work, the worker should report the exact shared path it used, files changed, commands run, and residual risks. The parent should verify those claims in the designated worktree before acceptance or publication.
