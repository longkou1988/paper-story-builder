# 01 Input Reading Prompt

Task: read and diagnose all required inputs before drafting.

Required checks:

1. Confirm `../paper-topic-builder/output/` exists.
2. Confirm `../paper-model-builder/output/` exists.
3. Confirm these priority files exist: `model_spec.json`, `hypothesis_table.md` or `hypothesis_table.xlsx`, `model_story_for_paper.md`, `theory_gap_matrix.xlsx`, `final_research_story.md`, and `input/benchmark_article.pdf`.
4. Load optional user notes: `input/manual_story_notes.md`, `input/target_journal_notes.md`, and `input/writing_preferences.md`.
5. Report missing files before drafting.

Do not infer missing model paths, variables, theories, or findings. Mark partial work as low confidence.
