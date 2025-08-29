# -- Project information -----------------------------------------------------
project = 'LA_Smart_Home-Installation tutorial'
copyright = '2024, Bot'
author = 'Bot'

# -- General configuration ---------------------------------------------------
extensions = ["myst_parser"]

from pygments.lexers import Python3Lexer
pygments_lexers = {
    "python-repl": Python3Lexer(),
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'

# 指定 logo 图片（放在 docs/_static/Logo2.png）
html_logo = "_static/Logo2.png"

# 启用静态文件目录（logo / css）
html_static_path = ['_static']

# 主题选项
html_theme_options = {
    'logo_only': True,      # 只显示 logo，不显示项目名称
    'display_version': False,  # 不显示版本号
}

# 自定义 CSS（可选，用于调整 logo 大小）
html_css_files = [
    'css/custom.css',
]
