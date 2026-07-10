from datetime import datetime

project = "Environmental Bioinformatics Methods"
author = "PKU EMBL"
release = "2026"
copyright = f"{datetime.now().year}, {author}"
language = "zh_CN"

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

source_suffix = {
    ".md": "markdown",
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "attrs_block",
    "attrs_inline",
]

html_theme = "sphinx_book_theme"
html_title = "环境生物信息学方法 · Environmental Bioinformatics Methods"
html_short_title = "环境生物信息学方法"
html_logo = "_static/yu-lab-logo.png"
html_static_path = ["_static"]
html_css_files = ["course.css"]
html_last_updated_fmt = "%Y-%m-%d"
html_copy_source = False
html_show_sourcelink = False
html_show_sphinx = False
numfig = True

html_theme_options = {
    "repository_url": "https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods",
    "repository_branch": "main",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "use_source_button": False,
    "use_download_button": True,
    "use_fullscreen_button": True,
    "show_toc_level": 2,
    "show_navbar_depth": 2,
    "home_page_in_toc": True,
    "path_to_docs": "docs",
    "toc_title": "本页目录",
    "announcement": (
        "<strong>2026 课程文档</strong> · "
        "以研究问题为起点，以可复现证据链为核心"
    ),
    "extra_footer": (
        "Environmental Bioinformatics Methods · "
        "Problem-driven, evidence-aware, reproducible."
    ),
}
