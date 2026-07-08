from __future__ import annotations

from common import MODEL_ROOT, OUTPUT_DIR, read_text, write_output


def main() -> None:
    model = read_text(MODEL_ROOT / "output" / "model_structure.md", "Model structure missing.")
    hypotheses = read_text(MODEL_ROOT / "output" / "hypothesis_table.md", "Hypothesis table missing.")
    story = read_text(OUTPUT_DIR / "story_chain.md", "Story chain missing.")
    theory_outline = f"""# Theoretical Background Outline

1. Define the core phenomenon and theoretical lens.
2. Position the antecedent and outcome.
3. Explain the mechanism.
4. Explain the boundary condition.
5. Link the model back to the focal management problem.

## Model Evidence
{model[:2000]}
"""
    theory_draft = f"""# Theoretical Background Draft

Draft this section from the model-builder outputs and the topic-builder gap analysis. Do not import substantive content from the benchmark article.

The theoretical background should explain why the model variables belong in one coherent logic chain instead of being a variable collage.

## Story Evidence
{story[:2000]}
"""
    hyp_outline = f"""# Hypotheses Outline

Use the hypothesis table as the controlling source.

{hypotheses[:2500]}
"""
    hyp_draft = f"""# Hypotheses Draft

For each hypothesis:
- State the proposed relationship.
- Explain the theoretical reason.
- Connect it to the mechanism or boundary condition.
- Mark missing literature support explicitly.

Moderation rule: the moderator should be written as changing the strength or direction of a specific path, not as a direct arrow to the dependent variable unless the model explicitly includes a direct effect.

## Source Hypotheses
{hypotheses[:2500]}
"""
    write_output("theoretical_background_outline.md", theory_outline)
    write_output("theoretical_background_draft.md", theory_draft)
    write_output("hypotheses_outline.md", hyp_outline)
    write_output("hypotheses_draft.md", hyp_draft)


if __name__ == "__main__":
    main()
