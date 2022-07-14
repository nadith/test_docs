# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
# sys.path.insert(1, os.path.abspath('./myhomework'))
# sys.path.insert(1, os.path.abspath('./sphinxext'))

# -- Project information -----------------------------------------------------

project = 'My Test Project'
copyright = '2021, Nadith Pathirage, Shani'
author = 'Nadith Pathirage, Shani'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage', 'numpydoc'] #'sphinx.ext.napoleon']

extensions = [
    #'matplotlib.sphinxext.plot_directive', # Ref: https://matplotlib.org/3.1.3/devel/plot_directive.html  # ReadTheDocs reports error
    "sphinx.ext.autodoc",  # Core Sphinx library for auto html doc generation from docstrings
    "sphinx.ext.autosummary",  # Create neat summary tables for modules/classes/methods etc
    "sphinx.ext.intersphinx",  # Link to other project's documentation (see mapping below)
    'sphinx.ext.todo', # https://www.sphinx-doc.org/en/master/usage/extensions/todo.html
    'sphinx.ext.ifconfig', # https://www.sphinx-doc.org/en/master/usage/extensions/ifconfig.html
    ## 'sphinx.ext.napoleon',
    "numpydoc", # ReadTheDocs reports error
    #"sphinx_autodoc_typehints",  # Automatically document param types (less noise in class signature) | Only works with 'sphinx.ext.napoleon' # ReadTheDocs reports error
    "sphinx.ext.linkcode",
    'sphinx.ext.doctest' # to execute run -> make doctest # https://stackoverflow.com/questions/9809434/auto-generate-doctest-output-with-sphinx-extension
                        # https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html
]

# https://stackoverflow.com/questions/5599254/how-to-use-sphinxs-autodoc-to-document-a-classs-init-self-method
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__', # to enable __init__ documentation globally
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

latex_elements  ={'preamble': r'''
                  \usepackage{tcolorbox}
                  \usepackage{blindtext}
                  \definecolor{mypink1}{rgb}{0.858, 0.188, 0.478}
                  '''}

# to enable __init__ documentation module-wise:  https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directive-option-automodule-special-members

todo_include_todos = True # https://www.sphinx-doc.org/en/master/usage/extensions/todo.html
todo_link_only = True
show_authors = True

# https://stackoverflow.com/questions/15394347/adding-a-cross-reference-to-a-subheading-or-anchor-in-another-page
# 'sphinx.ext.autosectionlabel'

# Ref: https://matplotlib.org/sampledoc/extensions.html
# extensions = ['matplotlib.sphinxext.only_directives',
#               'matplotlib.sphinxext.plot_directive',
#               'IPython.sphinxext.ipython_directive',
#               'IPython.sphinxext.ipython_console_highlighting',
#               'sphinx.ext.mathjax',
#               'sphinx.ext.autodoc',
#               'sphinx.ext.doctest',
#               'sphinx.ext.inheritance_diagram',
#               'numpydoc']
# 'sphinx.ext.viewcode',


releaselevel = 'beta'

# numpydoc_show_class_members = False
numpydoc_validation_checks = {"all"} # TODO: Does not work, check later
numpydoc_use_plots = True # To show plots in docstrings

# # generate autosummary even if no references
# autosummary_generate = True
# autosummary_imported_members = True


# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
# # Napoleon settings
# napoleon_google_docstring = True
# napoleon_numpy_docstring = True
# napoleon_include_init_with_doc = False
# napoleon_include_private_with_doc = False
# napoleon_include_special_with_doc = True
# napoleon_use_admonition_for_examples = False
# napoleon_use_admonition_for_notes = False
# napoleon_use_admonition_for_references = False
# napoleon_use_ivar = False
# napoleon_use_param = True
# napoleon_use_rtype = True
# napoleon_preprocess_types = False
# napoleon_type_aliases = None
# napoleon_attr_annotations = True


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

def setup(app):
    app.add_config_value('releaselevel', '', 'env')

def linkcode_resolve(domain, info):
    if domain != 'py':
        return None
    if not info['module']:
        return None
    filename = info['module'].replace('.', '/')
    return "https://somesite/sourcerepo/%s.py" % filename