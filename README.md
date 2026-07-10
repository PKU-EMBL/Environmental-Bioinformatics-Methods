# 环境生物信息学方法 | Methodologies of Environmental Bioinformatics

> 从环境问题到可复现证据：一门面向研究生的环境生物信息学方法课程。

[![Documentation Status](https://readthedocs.org/projects/environmental-bioinformatics-methods/badge/?version=latest)](https://environmental-bioinformatics-methods.readthedocs.io/)

[课程文档](https://environmental-bioinformatics-methods.readthedocs.io/) · [教学进度](https://environmental-bioinformatics-methods.readthedocs.io/en/latest/schedule.html) · [课程汇报](https://environmental-bioinformatics-methods.readthedocs.io/en/latest/project.html) · [资源索引](https://environmental-bioinformatics-methods.readthedocs.io/en/latest/resources.html)

## 课程简介 | Course Thesis

本课程围绕真实环境样品中的微生物组数据展开，从生物学问题、公共数据库与序列比对出发，逐步进入宏基因组组装、分箱、基因组质量评估、系统发育、丰度计算、功能注释、宏转录组与扩增子生态分析。

课程不把生物信息学视为软件清单，而是把它作为环境生物学研究的推理框架。学生将学习如何把生态与进化问题转译为计算任务，判断数据库和分析结果的可信度，并把复杂组学证据组织成清楚、克制、可答辩的科学论证。

The course treats bioinformatics as a way of reasoning about environmental biological systems. It emphasizes problem framing, transparent methodological choices, reproducible evidence, and disciplined interpretation.

## 课程速览 | At a Glance

| 项目 | 说明 |
| --- | --- |
| **课程名称** | 环境生物信息学方法 / Methodologies of Environmental Bioinformatics |
| **任课教师** | 余珂 / Ke Yu |
| **修读对象** | 硕士、博士研究生 |
| **教学主线** | 10 讲 PDF 课件 + 方法讨论 + 课程汇报 |
| **考核方式** | 课程汇报一项 |
| **课程网站** | <https://environmental-bioinformatics-methods.readthedocs.io/> |

## 学习成果 | Learning Outcomes

完成课程后，学生应能够：

1. 把环境微生物学问题收敛为数据可支持、边界清楚的计算问题。
2. 对公共数据库、序列比对与功能注释保持必要的证据意识。
3. 设计并解释 assembly、binning、MAG quality、abundance 与 annotation 流程。
4. 连接序列、基因组、功能、表达与群落生态层面的证据。
5. 用可复现信息、关键图表和局限性讨论完成研究生水平的学术汇报。

## 教学主线 | Lecture Arc

| 模块 | 主题 | 核心方法 |
| --- | --- | --- |
| 1 | 生物学基础与环境生物信息学问题 | microbial dark matter, sequencing logic, problem framing |
| 2 | 生物信息学资源 | sequence databases, ORF concepts, database literacy |
| 3 | 基础 BLAST 分析实例 | similarity search, homology reasoning, hit interpretation |
| 4 | 宏基因组分析概况及序列组装 | metagenomics vs amplicons, short reads, assembly |
| 5–6 | 宏基因组分析设计及组装 | study design, sampling-to-sequencing workflow |
| 7 | 宏基因组分箱分析及实操 | mapping, coverage, binning, MAG recovery |
| 8 | 封箱、基因组质量检测及进化树构建 | refinement, genome QC, phylogenetic placement |
| 9 | 丰度计算、功能注释及宏转录组基础 | abundance, functional potential, transcript evidence |
| 10 | 生态学理论及初步扩增子分析 | community assembly, diversity, ecological inference |

## 仓库结构 | Repository Map

```text
.
├── assignments/          # 非考核方法训练模板
├── docs/                 # Sphinx + MyST 文档源文件
│   └── _static/          # Read the Docs 站点样式
├── lecture/              # 十讲课程课件 PDF
├── project/              # 课程汇报工作区与规划模板
├── TOOL.md               # 生物信息学工具质量检查清单
├── .readthedocs.yaml     # Read the Docs 构建配置
└── README.md
```

## 本地构建 | Local Build

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r docs/requirements.txt
sphinx-build -b html -W --keep-going docs docs/_build/html
```

构建成功后打开 `docs/_build/html/index.html`。站点正文采用英文 Times New Roman、中文仿宋字体栈；代码块保留等宽字体。

## 内容贡献 | Contributing

欢迎通过 Issues 或 Pull Request 修复错误、更新链接、补充方法说明或改进可复现示例。涉及数据库、软件、课程安排或外部资源时，请注明版本、访问日期与适用范围；请勿提交未授权数据、个人隐私或无法核查的结论。

## 引用 | Citation

```bibtex
@misc{PKU_EMBL_EnvBioinfoMethods,
  author       = {{PKU-EMBL}},
  title        = {Environmental Bioinformatics Methods},
  year         = {2026},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods}}
}
```

## License

本仓库内容按 [MIT License](LICENSE) 提供；外部数据、软件、图片与文献仍遵循其各自许可条款。
