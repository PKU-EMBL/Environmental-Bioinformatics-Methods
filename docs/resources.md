# 资源 | Resources

<p class="page-lead">本页按“课程材料—数据资源—分析工具—可复现基础设施”组织入口。选择资源时，优先考虑它是否与研究问题、数据类型和证据尺度匹配。</p>

## 课程材料 | Course Materials

- [Lecture PDFs](https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods/tree/main/lecture)：课程主线课件。
- [TOOL.md](https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods/blob/main/TOOL.md)：生物信息学工具质量与可复现性检查清单。

## 数据资源 | Data Sources

- NCBI SRA / ENA：公共测序数据获取平台，适合查找环境宏基因组、扩增子或宏转录组数据。
- GenBank / INSDC：核酸序列与注释资源，适合配合 BLAST 和数据库检索练习。
- GTDB：基因组分类学框架，适合 MAG 分类和系统发育解释。
- KEGG / eggNOG / Pfam：功能注释常用资源，适合讨论 functional potential。

## 课程工具 | Course Tools

- BLAST：序列相似性搜索与同源性线索分析。
- Assembly tools：用于从短读段恢复 contig 或 scaffold，具体工具以课堂课件为准。
- Binning tools：用于从 coverage 和序列组成中恢复 MAG。
- CheckM / CheckM2：基因组完整度与污染度评估。
- CoverM：宏基因组丰度计算。
- BASALT：环境宏基因组分析相关工具包。

## 可复现工作栈 | Reproducibility Stack

- 环境管理：`conda` 或 `mamba`。
- 流程管理：`snakemake` 或 `nextflow`。
- 版本控制：`git`。
- 图表记录：保留绘图脚本、输入表格和关键参数。
- 汇报归档：保留最终幻灯片、流程图和可核查信息。

## 如何选择资源 | Selection Guide

| 需要回答的问题 | 优先核对的信息 |
| --- | --- |
| **数据是否合适？** | 采样设计、环境元数据、测序平台、读长、深度与许可条件 |
| **数据库是否合适？** | 数据覆盖范围、版本、更新时间、分类或功能体系与已知偏差 |
| **工具是否合适？** | 输入假设、算法目标、默认参数、基准测试与失败场景 |
| **结果是否可比较？** | 版本一致性、标准化方式、参考集合、过滤阈值与统计设计 |
| **流程是否可复现？** | 环境锁定、随机种子、日志、输入输出校验和与工作流记录 |

## 阅读策略 | Reading Strategy

阅读工具文档和方法论文时，优先寻找四类信息：输入假设、数据库版本、默认参数和失败场景。课程汇报中能把这些信息讲清楚，通常比简单罗列软件名称更有价值。

```{admonition} 版本意识
:class: note
数据库内容、软件默认参数和在线服务都可能更新。课程材料提供的是方法入口；在实际分析与汇报中，请记录具体版本、访问日期和关键配置，并以官方文档为最终依据。
```
