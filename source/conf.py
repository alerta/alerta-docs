# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Alerta'
copyright = '2015-2023, Nick Satterly. Creative Commons Attribution-ShareAlike 3.0 License'
author = 'Nick Satterly'
version = '9.0.0rc1'
release = '9.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import sys
import os

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    # 'sphinxcontrib.spelling',
    'myst_parser',
    'sphinx_copybutton',
]

spelling_lang='en_US'
spelling_word_list_filename='spelling_wordlist.txt'
spelling_show_suggestions=False

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}

myst_enable_extensions = [
    'colon_fence',
    'strikethrough',
]

templates_path = ['_templates']
exclude_patterns = ['Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster'
# html_theme = 'piccolo_theme'
html_static_path = ['_static']
html_extra_path = []
