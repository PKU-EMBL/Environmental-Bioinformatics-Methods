# 资源 | Resources

## Course Materials

- [Lecture PDFs](https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods/tree/main/lecture)：课程主线课件。
- [TOOL.md](https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods/blob/main/TOOL.md)：生物信息学工具质量与可复现性检查清单。

## Data Sources

- NCBI SRA / ENA：公共测序数据获取平台，适合查找环境宏基因组、扩增子或宏转录组数据。
- GenBank / INSDC：核酸序列与注释资源，适合配合 BLAST 和数据库检索练习。
- GTDB：基因组分类学框架，适合 MAG 分类和系统发育解释。
- KEGG / eggNOG / Pfam：功能注释常用资源，适合讨论 functional potential。

## Tools Mentioned Across The Course

- BLAST：序列相似性搜索与同源性线索分析。
- Assembly tools：用于从短读段恢复 contig 或 scaffold，具体工具以课堂课件为准。
- Binning tools：用于从 coverage 和序列组成中恢复 MAG。
- CheckM / CheckM2：基因组完整度与污染度评估。
- CoverM：宏基因组丰度计算。
- BASALT：环境宏基因组分析相关工具包。

## Reproducibility Stack

- 环境管理：`conda` 或 `mamba`。
- 流程管理：`snakemake` 或 `nextflow`。
- 版本控制：`git`。
- 图表记录：保留绘图脚本、输入表格和关键参数。
- 汇报归档：保留最终幻灯片、流程图和可核查信息。

## Reading Strategy

阅读工具文档和方法论文时，优先寻找四类信息：输入假设、数据库版本、默认参数和失败场景。课程汇报中能把这些信息讲清楚，通常比简单罗列软件名称更有价值。
