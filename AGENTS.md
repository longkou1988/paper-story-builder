# paper-story-builder

本 Skill 用于基于 `paper-topic-builder` 和 `paper-model-builder` 的输出文件，并结合用户上传的对标期刊论文 PDF，生成管理学实证论文的故事链、Introduction 初稿、Theoretical Background 初稿、Hypotheses 初稿、Contribution Statement 和交叉验证报告。

## 核心定位

`paper-story-builder` 不负责重新读取 Zotero，不负责重新生成选题，不负责重新设计研究模型。它只负责把已有选题、研究模型、理论缺口、假设路径和模型说明，进一步转化为可用于管理学实证论文写作的故事链和初稿。

## 与前置 Skill 的关系

1. `paper-topic-builder` 负责从文献到选题；
2. `paper-model-builder` 负责从选题到研究模型；
3. `paper-story-builder` 负责从研究模型到论文故事链和初稿。

## 输入来源

默认读取：

1. `paper-topic-builder` 的 `literature_matrix.xlsx`；
2. `paper-topic-builder` 的 `variable_role_matrix.xlsx`；
3. `paper-topic-builder` 的 `theory_gap_matrix.xlsx`；
4. `paper-topic-builder` 的 `final_research_story.md`；
5. `paper-model-builder` 的 `model_spec.json`；
6. `paper-model-builder` 的 `hypothesis_table.md` 或 `hypothesis_table.xlsx`；
7. `paper-model-builder` 的 `model_story_for_paper.md`；
8. `paper-model-builder` 的 `model_logic_check.md`；
9. 用户上传的 `benchmark_article.pdf`。

## 对标论文使用规则

1. 可以分析对标论文的章节结构、段落功能、论证顺序、修辞动作和贡献表达方式。
2. 不得复制、改写、翻译或近似复现对标论文的原文句子。
3. 不得连续使用对标论文中的独特表达、核心句式或段落组织原文。
4. 不得把对标论文中的研究结论、变量、样本或理论伪装成本研究内容。
5. 对标论文只能作为结构范式参考，不能作为内容替代。
6. 生成文本必须基于本研究自己的变量、理论、模型、文献证据和研究情境。
7. 如果需要引用对标论文中的观点，必须明确标注为对标论文观点，并避免长篇摘录。
8. 对标论文的拆解结果应以“段落功能”“修辞动作”“结构模式”为主，而不是以原文句子为主。

## 写作原则

1. 故事链必须从现实问题出发，逐步进入理论缺口、研究问题、模型逻辑和研究贡献。
2. Introduction 必须形成清晰的 funnel structure，即从宏观现象到具体研究问题。
3. 理论背景必须服务于模型变量关系，不能写成文献堆砌。
4. 假设推导必须与 `model_spec.json` 和 `hypothesis_table` 保持一致。
5. 每条假设必须有理论依据和文献依据。
6. 中介假设必须解释作用机制。
7. 调节假设必须解释边界条件，并把调节变量指向被调节的路径，而不是简单画成指向结果变量的直接箭头。
8. 贡献声明不能夸大，必须回到 `theory_gap_matrix` 和 `model_logic_check`。
9. 不允许为了贴合对标论文结构而改变本研究模型。
10. 不允许引入没有证据支持的新变量、新理论或新路径。

## 交叉验证原则

生成初稿后，必须检查：

1. 研究问题是否对应理论缺口；
2. 理论缺口是否对应模型设计；
3. 模型路径是否对应假设；
4. 假设是否对应变量角色；
5. 变量角色是否对应文献证据；
6. Introduction 中承诺的贡献是否在模型中得到体现；
7. Contribution 是否存在夸大；
8. 对标论文结构是否只是高层范式迁移，而非文本仿写；
9. 是否存在理论、变量、方法三者不一致；
10. 是否存在审稿人会质疑的跳跃逻辑。

## 审稿人视角

所有输出都必须从 SSCI 管理学审稿人的角度进行检查，包括：研究问题是否重要、理论缺口是否真实、故事链是否连贯、变量模型是否与故事链匹配、假设推导是否充分、文献综述是否批判而不是罗列、理论贡献是否具体、实践贡献是否真实、是否存在过度承诺、是否存在范式模仿过度或文本相似风险。
