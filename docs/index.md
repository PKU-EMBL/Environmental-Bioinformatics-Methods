# 环境生物信息学方法

Methodologies of Environmental Bioinformatics

```{admonition} Course Positioning
:class: note
这是一门面向研究生的环境生物信息学方法课。课程以课件中的真实分析链条为主线，强调问题驱动、方法透明、证据解释与可复现汇报。
```

::::{grid} 1 2 2 2
:::{grid-item-card} 课程大纲
课程定位、能力目标、先修要求与唯一考核方式。
+++
[查看 Syllabus](syllabus.md)
:::

:::{grid-item-card} 教学进度
按课件组织的模块化课程路径与讲义链接。
+++
[查看 Schedule](schedule.md)
:::

:::{grid-item-card} 课程汇报
课程唯一考核项、汇报结构与评分维度。
+++
[查看 Presentation](project.md)
:::

:::{grid-item-card} 资源与规范
推荐工具、数据资源、学术诚信与可复现要求。
+++
[查看 Resources](resources.md)
:::
::::

## Course Thesis

环境生物信息学的核心不是运行更多软件，而是把环境生物学问题转换成可检验的计算证据链。本课程从生物学基础与公共数据库出发，逐步进入 BLAST、宏基因组组装、分箱、基因组质量检测、系统发育、丰度估计、功能注释、宏转录组与扩增子生态分析。课程希望学生最终能够像研究者一样解释数据：知道一个结果来自哪里、为什么可信、哪里可能出错，以及如何把方法讲清楚。

## Quick Facts

- 修读对象：硕士/博士研究生
- 任课教师：余珂
- 课程形式：讲授、案例拆解、方法讨论、课程汇报
- 课程材料：`lecture/` 目录中的 PDF 课件
- 考核方式：课程汇报一项

## Local Build

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r docs/requirements.txt
sphinx-build -b html docs docs/_build/html
```

```{toctree}
:maxdepth: 2
:caption: Course Navigation

syllabus
schedule
project
assignments
policies
resources
faq
```
