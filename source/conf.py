# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = 'Learning about Quantum 2.0'
copyright = '2021, Thomas Germain'
author = 'Thomas Germain'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx_rtd_theme',
    'sphinxcontrib.bibtex',
    'jupyter_sphinx'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_show_sourcelink = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

# html_logo = 'about-quantum_logo.png'

# -- Additional configuration ------------------------------------------------

rst_prolog = """
.. role:: red
.. role:: draft
.. role:: supnote
.. |citation| replace:: :supnote:`[citation needed]`
.. |draft| replace:: :draft:`Draft`
"""

numfig = True

autosectionlabel_prefix_document = True

bibtex_bibfiles = ['biblio/books.bib', 'biblio/lectures.bib',
                   'biblio/reviews.bib', 'biblio/articles.bib',
                   'biblio/misc.bib', 'biblio/QCE21.bib',
                   'biblio/textbooks.bib']
bibtex_default_style = 'plain'
#bibtex_reference_style = 'author_year'  # version 2.2.0

html_theme_options = {
    'navigation_depth': 3,
#    'titles_only': True,
}

# -- EOF ---------------------------------------------------------------------
