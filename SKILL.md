---
name: paper-story-builder
description: Build management paper story chains, benchmark article structure analysis, Introduction/Theory/Hypotheses drafts, contribution statements, manuscript skeletons, and reviewer checks from paper-topic-builder and paper-model-builder outputs plus a user-provided benchmark article PDF. Use when the user asks to turn an existing topic/model into SSCI-style empirical paper writing, analyze a benchmark article's rhetorical structure, or cross-validate story-model-hypothesis-contribution consistency.
---

# paper-story-builder

中文名称：论文故事链与初稿生成 Skill

paper-story-builder turns outputs from `paper-topic-builder` and `paper-model-builder` plus a user-provided benchmark journal article PDF into a management empirical paper story chain, Introduction draft, Theoretical Background draft, Hypotheses draft, Contribution Statement, manuscript skeleton, and reviewer-style story check.

It does not reread Zotero, regenerate topics, redesign the research model, invent variables, or create empirical results. `paper-story-builder` only learns the benchmark paper's structure and argumentation paradigm, not its wording.

## Workflow Position

Use this sequence:

1. `paper-topic-builder`: literature base to topic cards and research story.
2. `paper-model-builder`: selected topic to model specification, hypotheses, and model logic.
3. `paper-story-builder`: approved model to paper story chain and manuscript drafts.

When prior outputs are missing, stop and report what is missing instead of creating a polished draft from weak evidence.

## Required Inputs

Prioritize these files:

- `../paper-model-builder/output/model_spec.json`
- `../paper-model-builder/output/hypothesis_table.md` or `../paper-model-builder/output/hypothesis_table.xlsx`
- `../paper-model-builder/output/model_story_for_paper.md`
- `../paper-topic-builder/output/theory_gap_matrix.xlsx`
- `../paper-topic-builder/output/final_research_story.md`
- `input/benchmark_article.pdf`

Also use these when available:

- `../paper-topic-builder/output/literature_matrix.xlsx`
- `../paper-topic-builder/output/variable_role_matrix.xlsx`
- `../paper-topic-builder/output/qualitative_mechanism_matrix.xlsx`
- `../paper-topic-builder/output/variable_network_summary.md`
- `../paper-topic-builder/output/topic_cards.md`
- `../paper-topic-builder/output/model_candidates.md`
- `../paper-topic-builder/output/reviewer_evaluation.md`
- `../paper-model-builder/output/model_structure.md`
- `../paper-model-builder/output/model_logic_check.md`
- `../paper-model-builder/output/reviewer_model_evaluation.md`
- `input/target_journal_notes.md`
- `input/writing_preferences.md`
- `input/manual_story_notes.md`

If the user keeps the earlier skills under another path, ask for the exact path or use explicit files supplied by the user.

## Input Checks

Before writing drafts:

1. Check whether `paper-topic-builder` and `paper-model-builder` output folders exist.
2. Check whether `model_spec.json`, `hypothesis_table.md` or `.xlsx`, and `model_story_for_paper.md` exist.
3. Check whether `theory_gap_matrix.xlsx` and `final_research_story.md` exist.
4. Check whether `input/benchmark_article.pdf` exists and is readable.
5. Load `input/manual_story_notes.md` when the user provides extra study background, selected topic card, journal fit notes, or preferred positioning.

Failure handling:

- Missing benchmark PDF: do not generate formal story chain or manuscript draft. Ask the user to upload the PDF, or offer to run only a prior-output consistency check.
- Missing model files: ask the user to run `paper-model-builder`.
- Missing topic/theory-gap files: ask the user to run `paper-topic-builder`.
- Partial inputs: generate only a low-confidence draft if the user explicitly accepts the limitation, and label every affected section.

## Benchmark PDF Rules

Use the benchmark article only for high-level structure:

- section order
- paragraph function
- rhetorical moves
- funnel logic
- contribution placement
- transition strategy
- theory-to-hypothesis organization

Do not copy, translate, paraphrase closely, or imitate distinctive wording from the benchmark paper. Do not import the benchmark paper's variables, theories, sample, findings, or contribution as if they belonged to the user's study. If a short phrase is quoted for location evidence, keep it minimal and clearly mark it as benchmark evidence.

Mandatory sentence for all benchmark-based analysis:

`paper-story-builder 只学习对标论文的结构和论证范式，不复制其文本表达。`

## Benchmark Analysis Outputs

Create:

- `output/benchmark_structure_analysis.md`
- `output/benchmark_rhetorical_moves.md`
- `output/benchmark_section_map.json`

Analyze article title, journal, article type, section structure, Introduction paragraph count, theory organization, hypothesis development, method/results/discussion structure, contribution placement, limitations/future research style, and the overall story pattern.

For rhetorical moves, focus on paragraph function:

- establishes practical phenomenon
- summarizes prior research stream
- identifies theoretical gap
- introduces research question
- introduces theoretical lens
- previews model/design
- states contributions
- transitions to the next section

## Story Chain Rules

Generate `output/story_chain.md` from the user's own topic/model evidence. Include: research phenomenon, managerial problem, prior research progress, research limitations, theory gap, entry point, core research question, theoretical lens, model structure, variable relationships, hypothesis logic, theoretical contribution, practical contribution, mapping to the benchmark's structural paradigm, and reviewer risks.

The story must move from practical problem to theoretical problem, from theory gap to model, and from model to contribution. Do not make a variable collage. Do not change the model just to fit the benchmark article.

## Introduction Rules

Create `output/introduction_outline.md` and `output/introduction_draft.md`.

Use English by default unless the user requests Chinese. Use a management SSCI style with a funnel structure: broad phenomenon, specific managerial problem, prior research stream, unresolved theoretical gap, research question, theoretical lens, model and design preview, contributions, and paper roadmap.

Every important claim should trace back to prior skill outputs, benchmark structure analysis, or a note saying `needs additional literature support`. Do not overstate novelty or claim "first study" without explicit evidence.

## Theoretical Background Rules

Create `output/theoretical_background_outline.md` and `output/theoretical_background_draft.md`.

Organize around model logic, not a literature list. Include core theory, variable definitions, prior research, theory gap, theoretical integration, and overall model explanation. Every theory must serve a specific path or mechanism. Mark unsupported claims as `needs additional literature support`.

## Hypotheses Rules

Create `output/hypotheses_outline.md` and `output/hypotheses_draft.md`.

Hypotheses must strictly follow `model_spec.json` and `hypothesis_table`. Do not add unapproved paths.

Use path-specific logic:

- Direct effect: explain why the independent variable relates to the dependent variable.
- Mediation: explain the process mechanism.
- Moderation: explain the boundary condition and point the moderator to the relationship/path, not only to an outcome variable.
- Chain mediation: explain the ordering logic.
- Moderated mediation: explain the conditional indirect effect.

If theory or literature evidence is weak, label it as `needs additional literature support`.

## Contribution Statement Rules

Create `output/contribution_statement.md` with theoretical contribution, method contribution, context contribution, and practical contribution. Each contribution must map to `theory_gap_matrix`, `model_logic_check`, `story_chain`, or a documented user note. Avoid vague claims such as "enriches the literature." State which mechanism, boundary condition, context, or explanatory limitation is addressed.

## Manuscript Skeleton Rules

Create `output/manuscript_skeleton.md` with Title, Abstract placeholder, Keywords placeholder, Introduction, Theoretical Background, Hypotheses Development, Methodology placeholder, Results placeholder, Discussion placeholder, Theoretical Contributions, Practical Implications, Limitations and Future Research placeholder, and References placeholder.

Do not fabricate data, samples, results, coefficients, p-values, or significance.

## Cross-Validation Rules

Create `output/cross_validation_report.md` using:

`Check_Item | Status | Evidence | Problem | Revision_Suggestion | Priority`

Statuses: `Pass`, `Minor Issue`, `Major Issue`, `Insufficient Evidence`.

Priorities: `High`, `Medium`, `Low`.

Check whether research question, theory gap, model, hypotheses, variable roles, contribution, writing claims, and benchmark structure transfer are mutually consistent. If inconsistency exists, state the problem before generating fluent prose.

## Reviewer Story Check

Create `output/reviewer_story_check.md` from the viewpoint of an SSCI management reviewer. Evaluate storyline clarity, theoretical gap clarity, research question value, model-story fit, hypothesis logic, benchmark paradigm transfer, text similarity risk, contribution specificity, journal fit, and writing readiness.

Use 1-5 scores for storyline clarity, theoretical gap clarity, model-story fit, hypothesis logic, contribution specificity, journal fit, and writing readiness. Use `Low`, `Medium`, or `High` for overall risk. Recommendation choices: `Strongly recommend`, `Recommend`, `Revise before use`, `Not recommend`.

## Bundled Prompts

Use prompts in `prompts/` for focused subtasks:

- `01_input_reading_prompt.md`: input discovery and missing-file diagnosis
- `02_benchmark_pdf_analysis_prompt.md`: benchmark PDF structure analysis
- `03_benchmark_rhetorical_moves_prompt.md`: rhetorical move extraction
- `04_story_chain_building_prompt.md`: story chain construction
- `05_introduction_writing_prompt.md`: Introduction outline and draft
- `06_theoretical_background_prompt.md`: theoretical background outline and draft
- `07_hypotheses_writing_prompt.md`: hypotheses development
- `08_contribution_statement_prompt.md`: contribution statement
- `09_cross_validation_prompt.md`: consistency and similarity-risk validation
- `10_reviewer_story_check_prompt.md`: reviewer-style evaluation

## Bundled Scripts

Use scripts in `scripts/` when useful:

- `read_prior_skill_outputs.py`: check and summarize prior outputs
- `analyze_benchmark_pdf.py`: extract benchmark PDF text and headings
- `build_benchmark_section_map.py`: create a structured section map
- `build_story_chain.py`: create a story-chain scaffold from available inputs
- `generate_introduction_draft.py`: create Introduction outline and draft scaffold
- `generate_theory_hypotheses_draft.py`: create theory and hypotheses scaffold
- `cross_validate_story_model.py`: generate a validation report
- `export_manuscript_skeleton.py`: assemble manuscript skeleton

Scripts provide scaffolding and file checks. Codex must still apply academic judgment and must not treat script output as validated scholarship.

## Output Files

Expected outputs:

- `output/benchmark_structure_analysis.md`
- `output/benchmark_rhetorical_moves.md`
- `output/benchmark_section_map.json`
- `output/story_chain.md`
- `output/introduction_outline.md`
- `output/introduction_draft.md`
- `output/theoretical_background_outline.md`
- `output/theoretical_background_draft.md`
- `output/hypotheses_outline.md`
- `output/hypotheses_draft.md`
- `output/contribution_statement.md`
- `output/manuscript_skeleton.md`
- `output/cross_validation_report.md`
- `output/reviewer_story_check.md`
- `output/revision_tasks.md`

## Usage Examples

`Use $paper-story-builder to read paper-topic-builder and paper-model-builder outputs plus paper-story-builder/input/benchmark_article.pdf, then generate story_chain.md, introduction_draft.md, hypotheses_draft.md, and cross_validation_report.md for Topic Card 1.`

`Use $paper-story-builder to analyze only input/benchmark_article.pdf and output benchmark_structure_analysis.md, benchmark_rhetorical_moves.md, and benchmark_section_map.json. Do not generate my paper draft.`

## Academic Integrity Boundary

This skill supports structural learning, not textual imitation. Keep the user's research content separate from the benchmark paper's content. When evidence is insufficient, mark it directly. When a claim cannot be traced to prior outputs, user notes, or real literature evidence, do not present it as established fact.
