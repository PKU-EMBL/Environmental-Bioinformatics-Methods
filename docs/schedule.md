# 教学进度 | Schedule

> 本页按 `lecture/` 中已上传课件组织课程模块。若课堂进度或课件版本更新，以任课教师课堂说明和本网站最新版本为准。

```{list-table}
:header-rows: 1
:widths: 10 24 34 20 12

* - Module
  - Topic
  - Core Questions
  - Methods and Concepts
  - Materials
* - L1
  - 生物学基础与环境生物信息学问题
  - 如何从环境系统中识别尚未培养或尚未充分理解的微生物及其功能？
  - microbial dark matter; sequencing as observation; environmental biotechnology; problem framing
  - [PDF](https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods/blob/main/lecture/第一讲_生物学基础.pdf)
* - L2
  - 生物信息学资源
  - 公共数据库如何支撑从基因到蛋白、从序列到功能的推理？
  - central dogma; ORF; sequence resources; alignment context; database literacy
  - [PDF](https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods/blob/main/lecture/第二讲_生物信息学资源.pdf)
* - L3
  - 基础 BLAST 分析实例
  - 一个相似性搜索结果如何被解释为同源性、功能或进化线索？
  - BLAST; GenBank/INSDC resources; query design; hit interpretation; false positives
  - [PDF](https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods/blob/main/lecture/第三讲_基础BLAST分析实例.pdf)
* - L4
  - 宏基因组分析概况及序列组装
  - 扩增子、短读段分析和基因组级分析分别能回答什么问题？
  - amplicon vs metagenome; short reads; assembly; nitrogen-cycle example; workflow levels
  - [PDF](https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods/blob/main/lecture/第四讲_宏基因组分析概况及序列组装.pdf)
* - L5-6
  - 宏基因组分析设计及组装
  - 从采样到测序再到 assembly，哪些设计选择决定后续解释的上限？
  - sampling design; DNA/RNA extraction; library construction; read depth; assembly strategy
  - [PDF](https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods/blob/main/lecture/第五-六讲_宏基因组分析设计及组装.pdf)
* - L7
  - 宏基因组分箱分析及实操
  - 如何从 contig 和 coverage 中恢复微生物基因组草图？
  - mapping; coverage/depth; binning; MAG recovery; practical workflow
  - [PDF](https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods/blob/main/lecture/第七讲_宏基因组分箱分析及实操.pdf)
* - L8
  - 封箱、基因组质量检测及进化树构建
  - 一个 MAG 何时足够可靠，可以进入下游生态和进化解释？
  - bin refinement; genome completeness/contamination; CheckM-style QC; phylogenetic tree; BASALT
  - [PDF](https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods/blob/main/lecture/第八讲_封箱、基因组质量检测及进化树的构建.pdf)
* - L9
  - 宏基因组丰度计算、功能注释及宏转录组基础
  - 基因组的存在、丰度和表达证据如何共同支持功能解释？
  - CoverM; abundance estimation; functional annotation; metabolic potential; metatranscriptomics
  - [PDF](https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods/blob/main/lecture/第九讲_宏基因组丰度计算、功能注释及转录组分析基础.pdf)
* - L10
  - 生态学理论及初步扩增子分析
  - 如何把群落构建理论、多样性指标和扩增子结果放在同一解释框架中？
  - community assembly; alpha/beta diversity; amplicon workflow; ecological inference
  - [PDF](https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods/blob/main/lecture/第十讲_生态学理论及初步扩增子分析.pdf)
* - Final
  - 课程汇报
  - 学生能否把一个环境生物信息学问题组织成清楚、可复现、可答辩的科学论证？
  - research question; workflow design; reproducibility; interpretation; oral defense
  - [Presentation Guide](project.md)
```

## Reading and Preparation

每次课前建议完成三件事：

1. 浏览对应 PDF 的标题、流程图和关键软件/数据库名称。
2. 记录一个方法问题，例如“这个工具的输入假设是什么”或“这个结果可能有哪些假阳性来源”。
3. 思考该讲内容如何服务最终课程汇报。

## Course Rhythm

课程采用“概念框架 -> 方法链条 -> 证据解释 -> 汇报表达”的节奏。前半部分建立数据库、比对和宏基因组分析的基础语言；中段进入 assembly、binning、MAG quality 和 phylogeny；后段把丰度、功能、转录和群落生态连接到研究问题中。最终课程汇报用于检验学生是否能独立组织一条可信的环境生物信息学分析路线。
