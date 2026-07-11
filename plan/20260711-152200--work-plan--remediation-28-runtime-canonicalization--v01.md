# Remediation 28 Runtime Canonicalization and Archive Recovery Plan

Plan Type: Work Plan
Workstream: Project remediation queue 28, canonicalization and archive recovery
Version: 01
Status: Implementation Complete
Created: 2026-07-11 15:22:00 KST
Last Updated: 2026-07-11 16:51:02 KST
Supersedes or Related Plan: Related to the approved queue entry `28 - canonicalization and archive` in AndroaBrain
Current Completion State: Runtime contract implementation, canonical `saebyeok` recovery, preservation manifest, self-review, and required validation are complete; the branch is ready for its concluding local commit
Completed So Far: Added the collaboration runtime SSOT; updated routing, skills, protocols, templates, and README; added and passed six regression tests; restored `saebyeok` from its verified private canonical remote; verified archive and legacy provenance; wrote the numbered non-destructive restoration manifest; completed a final self-review after the independent reviewer was unavailable
Remaining Work: No implementation work remains. The parent will create the concluding conventional local commit and record its SHA in the uncommitted numbered handoff.
Current Blockers: Upstream grants the active account READ permission only, so the current contract forbids a branch push. This does not block the required local completion.
Next Step: Create the local commit, update the uncommitted numbered handoff with its SHA and the push-permission result, then stop.

## Scoreboard

Current Score: 50/100
Score Source: provisional
Last Updated: 2026-07-11 16:51:02 KST
Score Rationale: All approved implementation, recovery, manifest, and validation work is complete. The score remains at the repository's maximum allowed provisional value because the user has not supplied an authoritative score.
What Improved: The runtime callable contract is centralized and regression-tested, `saebyeok` is restored at its canonical path, every named legacy and archive item has deterministic preservation evidence and a non-destructive recovery command, and no protected source or history was deleted.
What Remains Unsatisfactory: Upstream branch publication is unavailable to the active READ-only account, and the planned independent reviewer could not run because of its usage limit; the resumed user instruction required self-review without creating another agent.
Actions To Raise Or Maintain The Score: Preserve the local commit and numbered handoff, and let a later authorized maintainer choose whether to publish the branch through a permitted remote.

Score History:

- 2026-07-11 15:22:00 KST - 48/100 provisional. The scan and isolation phase is complete, but all user-visible deliverables and acceptance checks remain open. The value stays below the repository's provisional-score ceiling.
- 2026-07-11 15:24:06 KST - 48/100 provisional. The central-document coordination plan was narrowed: leave the already-written queue change untouched, make no further central or existing project-note edits, and write only the numbered handoff without committing or pushing the vault.
- 2026-07-11 15:30:23 KST - 50/100 provisional. The runtime SSOT, maintained workflow updates, and six regression tests are complete; the score is capped by local policy while recovery and delivery remain unfinished.
- 2026-07-11 16:51:02 KST - 50/100 provisional. Runtime implementation, `saebyeok` recovery, manifest materialization, self-review, and the changed regression suite are complete; the value remains capped until the user provides a score.

## Approval Record

Treat the user's delegation message, the queue's common execution contract, and the later collision-prevention correction as explicit approval for this complete workstream. The user specifically instructed this session to begin immediately, avoid another approval wait, finish implementation, verification, documentation, and branch delivery, and change only queue item 28. The later correction is authoritative for shared documentation: do not make any further change to the central queue or any existing AndroaBrain project note, do not undo the already-written queue change, write the final result only to `AI-Sessions/conversations/2026-07-11-remediation-28.md`, and do not commit or push the vault. These instructions satisfy the repository's plan-first approval purpose while also overriding any local wording that would otherwise require another conversational pause. Do not request routine approval during execution. Stop only for the hard gates named by the user and the ledger: expenditure, legal consent, first external publication, a real transaction, destructive deletion, or Git history rewriting. None of the planned actions crosses those gates.

## Objective

Bring the preserved local project inventory and the Codex orchestration documentation back into agreement with current reality without editing the central project map and without deleting any source, worktree, archive object, or Git history. The completed result must let integration session 29 and a future operator answer three questions from durable evidence: which orchestration calls are actually available and how agents share state; which local path is canonical for each duplicated or legacy project; and exactly how every preserved auxiliary or archived artifact can be verified and restored.

The work should correct contracts, not redesign the product. It should preserve the repository's useful scan, plan, implement, verify, review discipline and its bounded repair loop. It should replace only the stale runtime assumptions: nonexistent collaboration calls, invented worker-specific model controls, incorrect forked-filesystem behavior, and parent-landing steps that do not match a shared working directory. It should also prevent the same drift from returning by adding a narrow automated documentation check that uses tools already available on the machine.

## Confirmed Facts

The remediation ledger authorizes item 28 and explicitly forbids creating the next numbered thread. A later collision-prevention instruction delegates the terminal central-ledger update to integration session 29, so this session must not edit the queue again even though it had already changed its row to `running`. Cache deletion belongs to item 29 and is outside this workstream. Source directories, worktrees, and histories must remain intact.

The original `Codex-Subagent-Orchestrator` checkout was clean but stale. Its local `main` and cached `origin/main` initially pointed to `a0e2df9`, while a live fetch advanced `origin/main` to `7109f0c`. The isolated branch `agent/28-canonicalization-runtime-contract` was therefore created from the fetched remote head rather than from the stale checkout. The current documentation still names `send_input` and `close_agent`, describes workers as editing forked filesystems whose results must be landed by the parent, and asks the parent to choose model and reasoning fields that are not part of the callable spawn schema.

The available collaboration surface is concrete and bounded. A parent can create a worker with `spawn_agent`, pass a non-triggering message with `send_message`, trigger another turn on an idle worker with `followup_task`, interrupt an active worker with `interrupt_agent`, inspect live agents with `list_agents`, and wait for mailbox state with `wait_agent`. `fork_turns` controls how much conversation context a new worker receives; it does not create an independent filesystem. All agents in the tree see the same current directory and filesystem, so overlapping writes can race immediately. Collaboration calls must be issued directly and are not nested inside the general JavaScript orchestration wrapper. The active runtime has four total concurrency slots including the parent, but documentation should describe capacity as runtime-provided rather than hardcode a universal team size.

The previously empty local `saebyeok` directory conflicted with current operational evidence. Its canonical private repository was verified and restored at `/Users/androa/Documents/saebyeok`, with `main` at `57f3b03024414f5bff4665334e328cab859edd29`. The legacy and auxiliary directories remain valuable because some are worktrees with commits not present on the canonical branch and some are complete earlier implementations. Their preservation status is recorded as fact rather than treating any old directory as safe to delete.

## Scope Boundaries

Change the orchestration repository only where current runtime assumptions are stated or validated. Keep plan-first policy, evidence requirements, role separation, and bounded review behavior unless they depend directly on the stale tool or workspace model. Introduce a single canonical runtime-contract reference if that is the smallest way to prevent repeated drift, and make the surrounding skill, workflow, protocol, templates, and README point to that contract consistently. Do not update vendored upstream content and do not perform unrelated prose cleanup.

For `saebyeok`, either restore the canonical repository into the already empty path after verifying the remote and default branch, or leave a small README pointer if clone authority, repository identity, or local collision cannot be established safely. Do not invent a new repository and do not overwrite any local content.

For archive recovery, create one central machine-readable manifest plus a human-readable handoff rather than scattering partial claims across every legacy directory. Cover `certisnap-ios-polish`, `enmirror-quality`, legacy `fateRank`, legacy `muskflow`, legacy `sensereset`, and every direct item below `_archive`. Each record must include the observed path and type, remote identity when applicable, branch and head, how unique commits were determined, a deterministic checksum with its algorithm and scope, the canonical or replacement project, preservation intent, and a non-destructive restoration command or procedure. If a field cannot be established, record `unknown` with the reason; never fabricate it.

Do not read `.env`, credentials, keystores, signing assets, or secret values. Checksums may cover tracked Git content or archive bytes without printing contents. Remote URLs must be sanitized if they contain user information. Do not add generated dependencies, clean caches, delete archives, prune worktrees, force-push, rebase shared history, or merge another session's branch.

## Phase One: Correct The Callable Runtime Contract

Start from the fetched remote baseline and re-read the final versions of every file that will be changed. Establish one authoritative reference that states the exact callable names, required arguments at a human-operational level, direct-call restriction, context-fork meaning, shared-filesystem behavior, concurrency discovery, message and follow-up distinction, interruption semantics, and the absence of a close operation. Make the reference explicit that tool availability is supplied by the active runtime and must be inspected rather than inferred from old documentation.

Update the subagent skill and its operating references so planning and scheduling decisions follow the actual runtime. Replace parent-landing language with shared-workspace coordination rules: assign disjoint writable scopes, use separate Git worktrees when branch isolation is needed, assume edits are visible immediately, and have the parent inspect and accept the shared final state rather than cherry-pick an invisible worker fork. Replace model and reasoning selection requirements with the controls that actually exist, especially worker mission, task name, context fork depth, timing, and writable scope. Replace `send_input` and `close_agent` with the correct distinctions among messaging, follow-up turns, interruption, waiting, and live-agent inspection.

Update templates and the bilingual README only to the extent needed to make new runs record the real fields. Preserve the repository's overall workflow terminology. Ensure no current document instructs an operator to call a missing collaboration tool, assumes each worker owns an isolated filesystem, or promises a callable parameter that the runtime does not expose.

## Phase Two: Add Contract Regression Validation

Add a dependency-free static validation command appropriate for this documentation repository. The check should fail when forbidden stale call names or forked-filesystem landing assumptions reappear in the maintained local orchestration surface. It should also confirm that the canonical reference contains every currently required callable name and the shared-filesystem warning. Exclude the vendored upstream repository and historical plan artifacts so intentional quotations or third-party content do not create noise.

Keep the test readable enough that a later runtime change can update the allowlist and assertions in one place. Document the validation command in the README and run it from a clean shell. Also perform direct repository-wide searches for stale phrases after the test passes, because the test itself is part of the change and needs independent confirmation.

## Phase Three: Recover Canonical Paths And Build Restoration Evidence

Use live local Git metadata and authenticated repository metadata to identify the canonical `saebyeok` remote. Confirm default branch, current head, and the merged commit noted by the latest handoff. If the empty directory can be safely populated without overwriting anything, clone the verified repository there and validate its status and remote. If not, write the pointer file with the verified canonical URL, expected branch, and clone command, and state why a clone was not performed.

Inventory each named auxiliary and legacy repository without modifying its history. Determine unique commits by comparing commit reachability with the declared canonical replacement or relevant remote references, not merely by comparing head hashes. For tracked-tree checksums, use a deterministic listing and hash method that excludes ignored caches and secret files. For archive files, hash the archive byte stream directly. For archive directories, define a stable path-and-content hashing procedure so the result can be reproduced. Record symlinks and empty directories explicitly. Restoration procedures must copy or clone into a new destination, verify the expected hash or commit, and avoid destructive replacement.

Treat a nonzero unique-commit count as a strong `do_not_delete` signal. Treat zero unique commits as evidence of Git reachability only, not as permission to delete untracked artifacts. Flag signing material, release binaries, financial records, and other protected classes without hashing secret contents into logs if their location is encountered. Defer all cache-size cleanup and deletion recommendations to queue item 29.

## Phase Four: Write The Numbered Integration Handoff

Do not update the central queue, project map, storage record, or any existing AndroaBrain project note. Leave the already-written `running` queue edit exactly as it is. After all code, recovery, manifest, verification, and review work is complete, create only `/Users/androa/Documents/ObsidianVaults/AndroaBrain/AI-Sessions/conversations/2026-07-11-remediation-28.md`. Follow the vault frontmatter and Save Filter rules, and make that single handoff self-contained enough for integration session 29 to perform the one-time central updates.

The handoff must state the final result status, current thread identifier, canonical paths, manifest location, branch and commit evidence, pull request or remote blocker, exact validation commands and outcomes, preservation guarantees, remaining hard gates, and `next number: none - parallel queue; item 29 performs central integration`. It must explicitly tell session 29 that the central row is still `running` because this session was instructed not to touch it again. Do not stage, commit, or push any AndroaBrain file.

## Phase Five: Verify, Review, And Publish

Run the new contract test, repository searches, Markdown structure checks, Git whitespace checks, manifest parser or schema checks, checksum regeneration comparison, and non-destructive restoration dry checks. Confirm that the source directories still exist, no worktree or history was removed, and no build cache was cleaned. Confirm that all modified repositories have only intended changes staged.

Use a separate read-only reviewer after the last writable change. Ask the reviewer to compare the final documentation against the actual collaboration tool schema, check shared-filesystem race guidance, inspect manifest completeness and restoration safety, identify secret exposure, and verify queue scope. If review finds a material defect that fits this approved workstream, apply one bounded repair and rerun the exact failed proof. Do not broaden into other numbered remediation tasks.

Before each code-repository commit, summarize the exact diff as required by the global Git rules. Use conventional commit messages. Push the Orchestrator branch if authenticated permission allows it and open a draft pull request against the remote default branch. If the upstream repository rejects writes, preserve the local commit, create or use an authorized fork only if that is a normal branch-delivery step and does not publish private material, and document the exact remote blocker. Never stage, commit, or push the AndroaBrain handoff, and never push directly to `main` or `master`.

## Risks And Mitigations

The largest technical risk is documenting a runtime snapshot too broadly and making it stale again. Mitigate this by separating stable semantics from discovered capacity, saying that the runtime advertises available controls, and testing only the callable surface actually required by the current contract. Avoid claiming a universal worker limit based on this one session.

The largest coordination risk is that all agents and parallel remediation sessions share files. Mitigate it with read-only inventory workers, one isolated worktree for Orchestrator writes, explicit file ownership, exact-path staging, and a final status refresh immediately before commit. Never reset or discard a dirty shared worktree.

The largest archive risk is treating a checksum as proof that an artifact is redundant. A checksum proves identity only against the same scoped input; it does not prove remote backup, semantic replacement, or absence of untracked data. The manifest must keep those claims separate and default to preservation.

The largest publication risk is repository permission. Preserve local conventional commits and exact commands, then report a branch-delivery blocker if the remote rejects the push. A push conflict should be resolved by fetching and integrating only the narrow code-repository changes, never by force or history rewrite. The vault is deliberately excluded from publication by the user's collision-prevention correction.

## Validation Strategy

Accept the runtime contract only when the maintained non-vendored documentation contains every callable required by the current surface, contains no stale callable instruction, explains that context fork and filesystem isolation are different, and explains how to prevent overlapping writes. Accept the regression check only when it passes normally and fails in a controlled temporary mutation or equivalent negative-case invocation.

Accept `saebyeok` recovery only when the local target is either a clean clone of a verified remote and branch or a pointer whose repository identity and clone command were verified. Accept the restoration manifest only when a standard parser can load it, every required target has a record, every checksum can be regenerated, every Git head exists, and every restoration procedure is non-destructive by construction.

Accept documentation synchronization only when the single numbered handoff has valid frontmatter, identifies the manifest and commits, states this thread id and final item result for session 29, leaves every existing project note and all further queue content untouched, and remains uncommitted and unpushed in the vault. Accept branch delivery only when the intended code-repository commits exist, remote tracking or the exact permission blocker is recorded, and any draft pull request targets the correct default branch.

## Definition Of Done

The work is complete when the callable and shared-workspace contract is accurate and regression-checked; the empty `saebyeok` path is safely restored or points to the verified canonical repository; the named auxiliary, legacy, and archive artifacts all have complete non-destructive recovery records; no source, history, worktree, or archive was removed; all relevant checks pass; the final allowed read-only review finds no unresolved material issue; the single uncommitted AndroaBrain handoff contains the final result and integration instructions; and the changed code repository has an intentional conventional commit plus the strongest safe branch delivery permitted without direct default-branch push.

If a true hard gate remains, finish every safe step and record `blocked_approval` with the precise gate in the numbered handoff for session 29 to apply centrally. Ordinary upstream permission failure is a delivery blocker to report with a preserved local commit, not permission to rewrite history or broaden the task. Cache cleanup, storage reclamation, deletion, and all central queue or project-note updates remain explicitly deferred to item 29.
