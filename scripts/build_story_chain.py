from __future__ import annotations

from common import MODEL_ROOT, TOPIC_ROOT, inventory, read_text, write_output


def main() -> None:
    data = inventory()
    model_story = read_text(MODEL_ROOT / "output" / "model_story_for_paper.md", "不足以判断")
    final_story = read_text(TOPIC_ROOT / "output" / "final_research_story.md", "不足以判断")
    missing = data["critical_missing"]
    status = "FORMAL DRAFT READY" if not missing else "LOW CONFIDENCE / PARTIAL ONLY"
    lines = [
        "# Story Chain",
        "",
        f"Status: {status}",
        "",
        "## Core Phenomenon",
        "Derive only from `final_research_story.md` and `model_story_for_paper.md`.",
        "",
        "## Management Problem",
        final_story[:2000],
        "",
        "## Theory Gap",
        "Use `theory_gap_matrix.xlsx` as the evidence base. Claims requiring exact cells should be checked manually if spreadsheet extraction is unavailable.",
        "",
        "## Model Logic",
        model_story[:2500],
        "",
        "## Story Chain Formula",
        "Phenomenon -> managerial tension -> theory gap -> model mechanism -> boundary condition -> contribution.",
        "",
        "## Non-Negotiable Checks",
        "- Do not regenerate topics.",
        "- Do not redesign the model.",
        "- Do not import variables, theory, sample, or findings from the benchmark article.",
        "- Moderators must point to the moderated path, not directly to the outcome.",
    ]
    if missing:
        lines += ["", "## Missing Inputs"] + [f"- {m}" for m in missing]
    write_output("story_chain.md", "\n".join(lines))


if __name__ == "__main__":
    main()
