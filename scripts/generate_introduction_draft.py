from __future__ import annotations

from common import OUTPUT_DIR, read_text, write_output


def main() -> None:
    story = read_text(OUTPUT_DIR / "story_chain.md", "Story chain not generated.")
    outline = """# Introduction Outline

1. Empirical phenomenon and managerial importance
2. Existing research conversation
3. Unresolved theoretical gap
4. Proposed model and mechanism
5. Contributions and paper positioning

Quality guardrails:
- Use benchmark article for structure only.
- Mark unsupported claims as needing additional literature support.
- Avoid first-study language unless verified.
"""
    draft = f"""# Introduction Draft

[Opening phenomenon paragraph]
Write from the focal topic and model outputs, not from the benchmark article.

[Research conversation paragraph]
Summarize what prior literature explains and what remains unclear. Every concrete literature claim must trace to prior outputs or be marked as needing additional support.

[Gap paragraph]
Use the theory gap from the topic-builder outputs. Do not invent gaps for fluency.

[Model paragraph]
Explain the antecedent, mechanism, outcome, and boundary condition from the model-builder outputs. If a moderator is included, describe the path it moderates.

[Contribution paragraph]
State bounded contributions without overclaiming.

## Source Story Chain
{story[:2500]}
"""
    write_output("introduction_outline.md", outline)
    write_output("introduction_draft.md", draft)


if __name__ == "__main__":
    main()
