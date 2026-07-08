from __future__ import annotations

from common import MODEL_ROOT, OUTPUT_DIR, inventory, read_text, write_output


def main() -> None:
    data = inventory()
    model_spec = read_text(MODEL_ROOT / "output" / "model_spec.json", "")
    story = read_text(OUTPUT_DIR / "story_chain.md", "")
    hyp = read_text(OUTPUT_DIR / "hypotheses_draft.md", "")
    issues = []
    if data["critical_missing"]:
        issues.append("Critical inputs are missing; outputs should remain low-confidence drafts.")
    if "moderator" in model_spec.lower() and "path" not in hyp.lower():
        issues.append("Moderator logic may be underspecified; verify that the moderator points to the moderated path.")
    if "first study" in (story + hyp).lower():
        issues.append("Potential overclaim: verify or remove first-study language.")
    report = ["# Cross Validation Report", "", "## Issues"]
    report += [f"- {i}" for i in issues] or ["- No automatic blocking issue detected. Manual evidence checking is still required."]
    report += ["", "## Required Manual Checks", "- Check every concrete literature claim against the source output files.", "- Check benchmark-text similarity before submission.", "- Confirm model diagram moderation arrows point to paths, not directly to outcomes."]
    tasks = ["# Revision Tasks", ""]
    tasks += [f"- [ ] {i}" for i in issues] or ["- [ ] Conduct manual source-traceability review before using the draft in a manuscript."]
    write_output("cross_validation_report.md", "\n".join(report))
    write_output("revision_tasks.md", "\n".join(tasks))


if __name__ == "__main__":
    main()
