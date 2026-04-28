# 环境生物信息学方法 | Methodologies of Environmental Bioinformatics

面向研究生的环境生物信息学方法课程。课程围绕真实环境样品中的微生物组数据展开，从生物学问题、公共资源与序列比对，到宏基因组组装、分箱、基因组质量评估、功能注释、宏转录组与扩增子生态分析，训练学生以研究问题驱动可复现计算分析。

A graduate-level methods course in environmental bioinformatics. The course moves from biological questions, public resources, and sequence alignment to metagenomic assembly, binning, genome quality assessment, functional annotation, metatranscriptomics, and amplicon-based ecological analysis.

[![Documentation Status](https://readthedocs.org/projects/environmental-bioinformatics-methods/badge/?version=latest)](https://environmental-bioinformatics-methods.readthedocs.io/)

## Course At A Glance

- 课程名称：环境生物信息学方法 / Methodologies of Environmental Bioinformatics
- 任课教师：余珂 / Ke Yu
- 修读对象：硕士、博士研究生
- 课程网站：<https://environmental-bioinformatics-methods.readthedocs.io/>
- 课程材料：`lecture/` 中的 PDF 课件为主线材料
- 考核方式：课程汇报一项，围绕问题定义、方法选择、数据分析、可复现性与科学解释展开

## Intellectual Scope

本课程不把生物信息学视为工具清单，而是把它作为环境生物学研究的推理框架。学生需要学习如何把生态与进化问题转译为可计算的分析设计，如何判断数据库、比对、组装、分箱和注释结果的可信度，以及如何把复杂组学结果组织成清楚、可辩护的科学论证。

By the end of the course, students should be able to:

1. Identify the computational structure behind an environmental microbiology question.
2. Use public bioinformatics resources and sequence-alignment logic with appropriate skepticism.
3. Design metagenomic workflows for assembly, binning, genome quality control, abundance estimation, and functional interpretation.
4. Connect community ecology concepts with amplicon and metagenomic evidence.
5. Present a reproducible, evidence-based analysis in a graduate seminar format.

## Lecture Arc

| Module | Topic                            | Core Methods                                                        |
| ------ | -------------------------------- | ------------------------------------------------------------------- |
| 1      | 生物学基础与环境生物信息学问题   | microbial dark matter, sequencing logic, environmental applications |
| 2      | 生物信息学资源                   | sequence databases, ORF concepts, alignment context                 |
| 3      | 基础 BLAST 分析实例              | database search, homology reasoning, result interpretation          |
| 4      | 宏基因组分析概况及序列组装       | metagenomics vs amplicons, short-read analysis, assembly            |
| 5-6    | 宏基因组分析设计及组装           | study design, sampling-to-sequencing workflow, assembly strategy    |
| 7      | 宏基因组分箱分析及实操           | contigs, coverage, binning, MAG recovery                            |
| 8      | 封箱、基因组质量检测及进化树构建 | MAG refinement, CheckM-style QC, phylogenetic placement             |
| 9      | 丰度计算、功能注释及宏转录组基础 | CoverM, functional potential, transcript evidence                   |
| 10     | 生态学理论及初步扩增子分析       | community assembly, diversity, amplicon workflow                    |

## Assessment

课程考核仅包含课程汇报。汇报可以围绕课件中的任一方法链条或真实环境生物学问题展开，要求体现：

- 清晰的问题定义与研究假设
- 数据来源、质量控制与方法选择依据
- 可复现的分析过程或流程设计
- 对结果可靠性、局限性与替代解释的讨论
- 专业、简洁、可答辩的学术表达

## Repository Structure

```text
.
├── assignments/          # 非考核练习与旧模板 / Non-graded practice templates
├── docs/                 # Sphinx + MyST 文档源文件 / Sphinx + MyST docs source
├── lecture/              # 课程讲义 PDF / Lecture slides
├── project/              # 课程汇报模板 / Presentation templates
├── LICENSE
├── README.md
└── TOOL.md               # 生信工具开发建议 / Bioinformatics tool-quality guidance
```

## Build Docs Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r docs/requirements.txt
sphinx-build -b html docs docs/_build/html
```

构建成功后打开 `docs/_build/html/index.html`。

## Citation

```bibtex
@misc{PKU-EMBL_EnvBioinfoMethods,
  author       = {{PKU-EMBL}},
  title        = {Environmental Bioinformatics Methods},
  year         = {2026},
  publisher    = {GitHub},
  journal      = {GitHub repository},
  howpublished = {\url{https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods}},
  note         = {Accessed: 2026-04-28}
}
```
