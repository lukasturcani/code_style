project = 'code-style'
copyright = '2019, Lukas Turcani'
author = 'Lukas Turcani'
version = ''
release = ''
extensions = []
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'
templates_path = []
html_static_path = []
htmlhelp_basename = 'codestyledoc'
latex_elements = {}
latex_documents = (
    master_doc,
    'code_style.tex',
    'code_style Documentation',
    'Lukas Turcani',
    'manual'
)
man_pages = [(
    master_doc,
    'code_style',
    'code_style Documentation',
    [author],
    1
)]
texinfo_documents = [(
    master_doc,
    'code_style',
    'code_style Documentation',
    author,
    'code_style',
    'Code style guidelines.',
    'Miscellaneous'
)]

html_theme_options = {
    'collapse_navigation': False
}
epub_title = project
epub_exclude_files = ['search.html']
