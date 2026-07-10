# P2：宏基因组流程设计 | Metagenome Workflow Design

> 非考核训练。目标是把组装、分箱和 MAG 质量评估组织为一条带判断点的流程，而不是软件清单。

## 训练目标

- 连接 reads、contigs、mapping、coverage、bins 与 MAG 质量指标。
- 为每个阶段定义输入、输出、质量检查和失败信号。
- 说明研究设计如何限制后续恢复能力与生态解释。

## 任务

围绕一个小型环境宏基因组数据集，设计从原始 reads 到候选 MAG 的最小流程。可以实际运行部分步骤，也可以完成基于课件与官方文档的流程设计；两者必须明确区分。

## 建议产出

1. 一页流程图：数据流、工具类别、关键参数与质量门槛。
2. 决策表：每一步的输入、输出、验证指标、失败表现与替代方案。
3. 至少一个实际或示例结果图表，例如 assembly statistics、coverage 分布或 MAG quality summary。
4. 一段失败案例分析：症状、可能原因、诊断步骤和修复策略。

## 自检问题

- 组装策略是否与样本设计、测序深度和群落复杂度匹配？
- coverage 信号来自怎样的 mapping 与过滤规则？
- completeness 与 contamination 的判断依赖什么 marker 假设？
- 哪些下游结论会被碎片化、strain heterogeneity 或误分箱影响？

## 可选进阶

比较两种 binning、refinement 或质量评估策略，并定义“结果更好”的可核查标准。
