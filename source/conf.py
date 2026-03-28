# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Alerta'
copyright = '2015-2026, Nick Satterly. Creative Commons Attribution-ShareAlike 3.0 License'
author = 'Nick Satterly'
version = '9.1.0'
release = '9.1'

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
myst_heading_anchors = 3

templates_path = ['_templates']
exclude_patterns = ['Thumbs.db', '.DS_Store', 'auth/*', 'examples/*', 'thrift/*', 'spelling_wordlist.txt']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster'
# html_theme = 'piccolo_theme'
html_static_path = ['_static']
html_extra_path = []

linkcheck_ignore = [
    'https://www.sto.nato.int/publications/STO%20Meeting%20Proceedings/STO-MP-SCI-300/MP-SCI-300-10.pdf',
]
