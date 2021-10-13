# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import datetime
import os
import sys
import filip
# pylint: disable-all

sys.path.insert(0, os.path.abspath('../..'))
sys.setrecursionlimit(1500)

# -- Project information -----------------------------------------------------

project = 'FiLiP'
copyright = f'2021-{datetime.datetime.now().year}, RWTH Aachen University, ' \
            f'E.ON Energy Research Center, ' \
            f'Institute for Energy Efficient Buildings and Indoor Climate'
author = 'E.ON ERC - EBC'

# The full version, including alpha/beta/rc tags
release = "0.1.8"

# The short X.Y version.
version = '.'.join(release.split('.')[0:2])


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.inheritance_diagram',
              'sphinx.ext.intersphinx',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages',
              'sphinx.ext.coverage',
              'm2r2',  # Enable .md files
              'sphinx.ext.napoleon',  # Enable google docstrings
              'sphinxcontrib.autodoc_pydantic'  # add support for pydantic
              ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'contents'


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'friendly'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Napoleon settings
napoleon_google_docstring = True

# autodoc_pydantic settings
autodoc_pydantic_model_show_json = False
autodoc_pydantic_settings_show_json = True
autodoc_pydantic_model_show_config_summary = True
autodoc_pydantic_model_show_validator_summary = True

# -- Options for HTML output ----------------------------------------------


# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

# Material theme options (see theme.conf for more information)
# html_theme_options = {
#
#    # Set the name of the project to appear in the navigation.
#    'nav_title': project,

# Set you GA account ID to enable tracking
# 'google_analytics_account': 'UA-XXXXX',

# Specify a base_url used to generate sitemap.xml. If not
# specified, then no sitemap will be built.
# 'base_url': 'https://project.github.io/project',

# Set the color and the accent color
#    'color_primary': 'red',
#    'color_accent': 'red',

# Set the repo location to get a badge with stats
#    'repo_url': 'https://github.com/rwth-ebc/filip',
#    'repo_name': 'Fiware Library for Python',

# Visible levels of the global TOC; -1 means unlimited
#    'globaltoc_depth': 4,
# If False, expand all TOC entries
#    'globaltoc_collapse': True,
# If True, show hidden TOC entries
#    'globaltoc_includehidden': False,
# Little logo on top left
#    'logo_icon': '&#xe869',
# }

html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "RWTH-EBC",  # Username/Group name
    "github_repo": "filip",  # Repo name
    "github_version": "master",  # Version
    "conf_py_path": "/docs/source/",  # Path in the checkout to the docs root
}

# html_logo = ""

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.

# This is required for the material theme
# Refs: https://bashtage.github.io/sphinx-material/index.html
html_sidebars = {
    "**": ["logo-text.html",
           "globaltoc.html",
           "localtoc.html",
           "searchbox.html"]
}

# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
# html_sidebars = {
#    '**': [
#        'relations.html',  # needs 'show_related': True theme option to display
#        'searchbox.html',
#    ]
# }


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'FiLiPdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'FiLiP.tex', 'FiLiP Documentation',
     'EON EBC', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'FiLiP', 'FiLiP Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'FiLiP', 'FiLiP Documentation',
     author, 'FiLiP', 'FIWARE Library for Python',
     'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
