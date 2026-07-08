from __future__ import annotations

from common import OUTPUT_DIR, read_text, write_output


def main() -> None:
    story = read_text(OUTPUT_DIR / "story_chain.md", "Story chain missing.")
    content = f"""# Contribution Statement

## Theoretical Contributions
1. Clarify the specific theoretical gap identified in prior outputs.
2. Explain how the model adds a mechanism or boundary condition rather than only restating a direct relationship.
3. State the contribution in bounded language and mark claims needing more literature support.

## Practical Contributions
1. Identify the focal management problem.
2. Explain what decision or intervention the model helps managers understand.
3. Clarify the context boundary.

## Evidence Base
{story[:2500]}

## Language Guardrail
Avoid unsupported claims such as "first study", "fills the gap completely", or "proves". Prefer "extends", "clarifies", "identifies", and "explains" when evidence supports the statement.
"""
    write_output("contribution_statement.md", content)


if __name__ == "__main__":
    main()
