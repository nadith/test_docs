.. Ref: https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html
   goto tutorial_packages folder and run "sphinx-apidoc -o <output> <source>"

Welcome to My Test Project's documentation!
===========================================

Hello World, this is my first Sphnix documentation.
Documentation for modules

.. toctree::
   :maxdepth: 2

   modules
   license

.. autosummary::

   mypackage1
   mypackage1.mod1
   mypackage2
   mypackage2.sub1
   mypackage2.sub1.mod1
   mypackage2.sub2
   mypackage2.sub2.mod1

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
