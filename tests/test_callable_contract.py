from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
RUNTIME_CONTRACT = ROOT / (
    "skills/codex-subagent-orchestrator/references/"
    "collaboration-runtime-contract.md"
)

ACTIVE_CONTRACT_FILES = (
    ROOT / "AGENTS.md",
    ROOT / "README.md",
    ROOT / "skills/agent-skills-integration/agent-skill-routing.md",
    ROOT / "skills/codex-parent-session-orchestrator/SKILL.md",
    ROOT / "skills/codex-subagent-orchestrator/SKILL.md",
    ROOT / "skills/codex-subagent-orchestrator/agents/openai.yaml",
    *sorted(
        (ROOT / "skills/codex-subagent-orchestrator/references").glob("*.md")
    ),
    *sorted(
        (ROOT / "skills/codex-subagent-orchestrator/assets/run-templates").glob(
            "*.md"
        )
    ),
)

STALE_INSTRUCTION_PATTERNS = (
    re.compile(r"use `send_input`", re.IGNORECASE),
    re.compile(r"use `close_agent`", re.IGNORECASE),
    re.compile(r"operate in forked workspaces", re.IGNORECASE),
    re.compile(r"own forked workspace", re.IGNORECASE),
    re.compile(r"\bland(?:s|ed|ing)?\b[^\n]*\bprimary workspace\b", re.IGNORECASE),
    re.compile(r"\| model \| reasoning \|", re.IGNORECASE),
    re.compile(r"4\+ workers", re.IGNORECASE),
)


def stale_instructions(text: str) -> list[str]:
    return [pattern.pattern for pattern in STALE_INSTRUCTION_PATTERNS if pattern.search(text)]


class CallableContractTests(unittest.TestCase):
    def test_runtime_contract_documents_current_callables(self) -> None:
        text = RUNTIME_CONTRACT.read_text(encoding="utf-8")
        for tool_name in (
            "spawn_agent",
            "send_message",
            "followup_task",
            "wait_agent",
            "interrupt_agent",
            "list_agents",
        ):
            with self.subTest(tool_name=tool_name):
                self.assertIn(f"`{tool_name}", text)

        self.assertIn("`fork_turns` forks conversation context only", text)
        self.assertIn("share the current working directory and filesystem", text)
        self.assertIn("not available through the `tools` object inside `functions.exec`", text)

    def test_active_contract_has_no_stale_instructions(self) -> None:
        failures: list[str] = []
        for path in ACTIVE_CONTRACT_FILES:
            matches = stale_instructions(path.read_text(encoding="utf-8"))
            if matches:
                failures.append(f"{path.relative_to(ROOT)}: {', '.join(matches)}")
        self.assertEqual([], failures, "\n".join(failures))

    def test_stale_instruction_detector_has_negative_case_coverage(self) -> None:
        bad_examples = (
            "use `send_input` for the next task",
            "use `close_agent` after completion",
            "workers operate in forked workspaces",
            "the parent lands changes in the primary workspace",
            "| model | reasoning |",
            "4+ workers are supported",
        )
        for example in bad_examples:
            with self.subTest(example=example):
                self.assertTrue(stale_instructions(example))

    def test_subagent_skill_allows_runtime_permitted_implicit_use(self) -> None:
        text = (
            ROOT / "skills/codex-subagent-orchestrator/agents/openai.yaml"
        ).read_text(encoding="utf-8")
        self.assertRegex(text, r"(?m)^\s*allow_implicit_invocation:\s*true\s*$")

    def test_orchestration_template_records_exposed_controls(self) -> None:
        text = (
            ROOT
            / "skills/codex-subagent-orchestrator/assets/run-templates/"
            "orchestration-plan.template.md"
        ).read_text(encoding="utf-8")
        self.assertIn("| target worktree | writable scope | context fork |", text)
        self.assertNotIn("| model | reasoning |", text)
        self.assertIn("observed runtime capacity", text)

    def test_entrypoints_link_to_runtime_contract(self) -> None:
        for relative_path in (
            "README.md",
            "skills/codex-subagent-orchestrator/SKILL.md",
            "skills/codex-subagent-orchestrator/references/orchestration-workflow.md",
            "skills/codex-subagent-orchestrator/references/sub-command-protocol.md",
        ):
            with self.subTest(relative_path=relative_path):
                text = (ROOT / relative_path).read_text(encoding="utf-8")
                self.assertIn("collaboration-runtime-contract.md", text)


if __name__ == "__main__":
    unittest.main()
