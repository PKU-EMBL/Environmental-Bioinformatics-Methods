# 方法训练 | Non-Graded Practice

<p class="page-lead">这些任务是课程汇报前的低风险训练场。你可以只完成与选题相关的部分，也可以把产出直接转化为流程图、方法说明、质量控制表或局限性讨论。</p>

```{admonition} 考核说明
:class: important
当前课程考核只有课程汇报。下列训练不单独计分，也不要求统一提交；除非任课教师在课堂上另行说明。
```

## 训练任务 | Practice Tracks

::::{grid} 1 2 2 2
:gutter: 3

:::{grid-item-card} P0 · 计算环境与可复现性
:class-card: course-card
建立可重复创建的分析环境，记录版本、命令、输入输出与最小测试。

**适合：** 所有真实数据分析选题
+++
[打开任务模板](https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods/blob/main/assignments/hw0_environment.md)
:::

:::{grid-item-card} P1 · 序列相似性与注释
:class-card: course-card
解释 BLAST 或同类搜索的 top hits、覆盖度、相似度、E-value 与潜在假阳性。

**对应：** L2–L3
+++
[打开任务模板](https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods/blob/main/assignments/hw1_similarity.md)
:::

:::{grid-item-card} P2 · 宏基因组分析设计
:class-card: course-card
绘制从 reads 到 assembly、binning、MAG 质量评估的流程，标注失败点与替代路径。

**对应：** L4–L8
+++
[打开任务模板](https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods/blob/main/assignments/hw2_metagenome_pipeline.md)
:::

:::{grid-item-card} P3 · 生态解释与报告
:class-card: course-card
从丰度、注释或多样性结果中构建一页结论，同时区分描述、关联与机制推断。

**对应：** L9–L10
+++
[打开任务模板](https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods/blob/main/assignments/hw3_ecology_reporting.md)
:::
::::

## 推荐训练顺序 | Suggested Workflow

| 步骤 | 行动 | 最小产出 |
| --- | --- | --- |
| **01 · 选题对齐** | 从课程汇报问题中找出最不确定的方法环节 | 一句话训练目标 |
| **02 · 小规模运行** | 使用最小数据或公开示例验证流程 | 可运行命令与日志 |
| **03 · 记录判断** | 写下选择该方法、参数或阈值的理由 | 方法决策表 |
| **04 · 制造失败** | 主动测试一个边界条件或失败场景 | 失败表现与诊断 |
| **05 · 汇入汇报** | 只保留能支撑核心论点的结果 | 一张图、表或流程图 |

## 训练完成标准 | Completion Standard

一次有效训练不以“命令成功结束”为终点，而应至少留下四类可核查信息：

- **输入：** 数据来源、格式、规模与质量状态。
- **过程：** 软件版本、关键参数、运行环境与日志。
- **输出：** 文件含义、基本验证与可视化结果。
- **判断：** 结果能支持什么、不能支持什么，以及下一步如何验证。

```{admonition} 与课程汇报的关系
:class: note
训练中最有价值的内容通常不是完整输出，而是一个更清楚的参数理由、一个被识别的失败风险、一个可复现的流程节点，或一个经得起追问的替代解释。
```
