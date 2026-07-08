from __future__ import annotations

from common import OUTPUT_DIR, read_text, write_output


def score_note(text: str) -> str:
    if "MISSING" in text or "BLOCKED" in text or "LOW CONFIDENCE" in text:
        return "cautious"
    return "manual review required"


def main() -> None:
    story = read_text(OUTPUT_DIR / "story_chain.md", "")
    cross = read_text(OUTPUT_DIR / "cross_validation_report.md", "")
    status = score_note(story + cross)
    content = f"""# Reviewer Story Check

## Overall Recommendation
{status}

## Reviewer Criteria
| Criterion | Score 1-5 | Comment |
|---|---:|---|
| Theoretical contribution |  | Check whether the theory gap is specific and not generic. |
| Story coherence |  | Check whether phenomenon, gap, model, and contribution form one chain. |
| Model clarity |  | Check whether each variable has a clear role. |
| Hypothesis logic |  | Check whether each hypothesis has theory-backed reasoning. |
| Evidence traceability |  | Check whether claims can be traced to prior outputs. |
| Benchmark use risk |  | Check text similarity and avoid importing content. |

## Mandatory Checks
- The benchmark article is used for structure only.
- The paper model is not redesigned in this Skill.
- Moderator arrows and text point to the moderated path, not directly to the outcome, unless a direct effect is explicitly specified.
- Unsupported claims are marked for additional literature support.

## Cross Validation Summary
{cross[:2000]}
"""
    write_output("reviewer_story_check.md", content)


if __name__ == "__main__":
    main()
