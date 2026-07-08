# paper-story-builder

中文名：论文故事链与初稿生成 Skill

作者：视频号扣子说AI

`paper-story-builder` is a Codex Skill for turning an existing empirical paper topic and research model into a management-paper story chain, Introduction draft, Theoretical Background draft, Hypotheses draft, Contribution Statement, manuscript skeleton, and reviewer-style evaluation.

It is designed as Skill 3 in this workflow:

1. `paper-topic-builder`: literature to topic.
2. `paper-model-builder`: topic to model.
3. `paper-story-builder`: model to paper story and drafts.

## 中文介绍

这个 Skill 不重新读取 Zotero，不重新生成选题，也不重新设计研究模型。它基于前两个 Skill 的输出文件，并结合用户上传的对标期刊论文 PDF，完成对标论文结构拆解、故事链构建、Introduction/Theory/Hypotheses 初稿生成、贡献声明、交叉验证和审稿人视角评价。

重要边界：`paper-story-builder` 只学习对标论文的结构和论证范式，不复制其文本表达。

## English Introduction

This Skill uses prior outputs from `paper-topic-builder` and `paper-model-builder` plus a benchmark journal article PDF to generate SSCI-style management paper writing artifacts. It supports benchmark structure analysis, rhetorical move mapping, paper story-chain construction, Introduction/Theoretical Background/Hypotheses drafts, contribution statements, cross-validation reports, and reviewer-oriented checks.

It transfers writing structure, not source text.

## Installation

Clone this repository into your Codex skills folder:

```bash
git clone https://github.com/longkou1988/paper-story-builder.git ~/.codex/skills/paper-story-builder
```

Restart Codex if the Skill list does not refresh automatically.

## Usage

Put the benchmark article PDF here:

```text
~/.codex/skills/paper-story-builder/input/benchmark_article.pdf
```

Then ask Codex:

```text
Use $paper-story-builder to read paper-topic-builder and paper-model-builder outputs plus paper-story-builder/input/benchmark_article.pdf, then generate story_chain.md, introduction_draft.md, hypotheses_draft.md, and cross_validation_report.md.
```

To only analyze the benchmark article:

```text
Use $paper-story-builder to analyze only input/benchmark_article.pdf and output benchmark_structure_analysis.md, benchmark_rhetorical_moves.md, and benchmark_section_map.json.
```

## Academic Integrity

Do not use this Skill to copy, translate, paraphrase closely, or imitate the benchmark article's distinctive wording. All generated claims must be grounded in the user's own topic, model, literature outputs, and documented notes.
