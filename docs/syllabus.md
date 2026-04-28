# 课程大纲 | Syllabus

## 课程基本信息 | Course Information

- 课程名称：环境生物信息学方法（Methodologies of Environmental Bioinformatics）。
- 修读对象：硕士/博士研究生。
- 任课教师：余珂（Ke Yu）。
- 教学形式：课堂讲授、课件导读、方法拆解、课堂讨论与课程汇报。
- 主线材料：`lecture/` 目录中的 PDF 课件。
- 考核方式：课程汇报一项。

## 课程定位 | Course Positioning

环境生物信息学连接环境科学、微生物生态学、分子生物学、统计推断与计算流程设计。本课程以环境微生物组研究为中心，从“我们如何观察不可培养微生物”这一问题出发，训练学生理解数据库、比对、组装、分箱、质量评估、系统发育、丰度计算、功能注释、宏转录组和扩增子生态分析之间的逻辑关系。

The course treats bioinformatics as a way of reasoning about environmental biological systems, not merely as a collection of command-line tools. Students learn to build defensible evidence chains from raw sequence data to ecological and evolutionary interpretation.

## 学习目标 | Learning Objectives

完成课程后，学生应能够：

1. 将环境生物学问题转化为可计算、可验证的分析任务。
2. 理解公共数据库、开放阅读框、同源性搜索和序列比对的基本逻辑。
3. 解释宏基因组分析从采样、测序、组装、分箱到 MAG 质量评估的关键决策。
4. 使用丰度、功能注释与转录证据讨论微生物群落的潜在功能。
5. 将生态学理论与扩增子/宏基因组结果连接起来，避免过度解释。
6. 以课程汇报形式呈现一个方法严谨、证据清楚、可答辩的分析方案或研究案例。

## 先修要求 | Prerequisites

学生不需要已经是生物信息学专家，但应具备：

- 基础分子生物学知识，包括 DNA、RNA、蛋白质与中心法则。
- 基本命令行和文件系统操作能力。
- 对统计图表、实验设计和科学假设有基本理解。
- 愿意阅读英文工具文档、数据库说明和方法论文。

## 课程主线 | Course Arc

```{list-table}
:header-rows: 1
:widths: 16 32 52

* - Unit
  - Theme
  - Methodological Focus
* - 1
  - 生物学基础与环境生物信息学问题
  - 微生物暗物质、测序视角、环境微生物资源与问题定义。
* - 2
  - 生物信息学资源
  - 核酸/蛋白序列资源、ORF、数据库检索与比对背景。
* - 3
  - 基础 BLAST 分析实例
  - 同源性搜索、数据库选择、比对结果解释与假阳性意识。
* - 4
  - 宏基因组分析概况及序列组装
  - 扩增子、短读段和基因组分析的差异；assembly 的研究意义。
* - 5-6
  - 宏基因组分析设计及组装
  - 从采样、建库、测序到组装策略的研究设计。
* - 7
  - 宏基因组分箱分析及实操
  - contig、coverage、mapping、binning 与 MAG 恢复。
* - 8
  - 封箱、基因组质量检测及进化树构建
  - MAG refinement、质量评估、系统发育定位与工具环境。
* - 9
  - 丰度计算、功能注释及宏转录组基础
  - CoverM、功能潜能、表达证据和多组学解释。
* - 10
  - 生态学理论及初步扩增子分析
  - 群落构建、多样性、扩增子分析流程与生态解释。
```

## 考核方式 | Assessment

课程考核只有课程汇报。课程汇报可采用个人或小组形式，具体组织以任课教师课堂说明为准。汇报应围绕一个环境生物信息学问题、一个方法链条或一个课件相关案例展开，重点展示学生是否能够把问题、数据、方法、结果和解释组织成一条可靠的科学论证。

建议评分维度：

- 问题定义与生物学意义：20%
- 方法选择、数据质量与分析逻辑：30%
- 可复现性、参数透明度与结果可核查性：20%
- 结果解释、局限性与替代假设讨论：20%
- 汇报表达、图表质量与答辩表现：10%

## 汇报标准 | Presentation Standard

一场优秀的课程汇报应当做到：

- 先给出清楚的研究问题，而不是先罗列软件。
- 说明数据从哪里来，质量如何，哪些步骤会影响结论。
- 用流程图或关键命令展示分析路径，但避免把汇报变成操作日志。
- 对不确定性保持诚实，包括数据库偏差、组装/分箱错误、注释歧义和生态解释边界。
- 用少量高质量图表支撑核心结论，并能回答“为什么这个结果可信”。

## 参考书 | References

1. Rodriguez-Ezpeleta, Hackenberg, and Aransay. _Bioinformatics of High Throughput Sequencing_. 978-1-4614-0781-2, 2012.
2. Hodgman, French, and Westhead. _Bioinformatics_.
