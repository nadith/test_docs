"""My Package 02 Module 01: Example NumPy style docstrings.

This module demonstrates documentation as specified by the `NumPy
Documentation HOWTO <www.google.com>`_. Docstrings may extend over multiple lines. Sections
are created with a section header followed by an underline of equal length.



.. code-block:: ruby
   :linenos:

   Some more Ruby code.
   
.. warning::

   An important bit of information about an API that a user should be very aware of 
   when using whatever bit of API the warning pertains to. The content of the directive 
   should be written in complete sentences and include all appropriate punctuation. 
   This differs from note in that it is recommended over note for information regarding security.


.. versionadded:: version

   This directive documents the version of the project which added the described 
   feature to the library or C API. When this applies to an entire module, 
   it should be placed at the top of the module section before any prose.

.. deprecated:: version
   
   Similar to versionchanged, but describes when the feature was deprecated. 
   An explanation can also be given, for example to inform the reader what 
   should be used instead. Example:

.. note::

   Copyright1 © iMindLabs, Inc - All Rights Reserved. Unauthorized copying of this file, via any 
   medium is strictly prohibited. Proprietary and confidential.

.. note::

   .. centered:: Copyright2 © iMindLabs, Inc - All Rights Reserved. Unauthorized copying of this file, 
                 via any medium is strictly prohibited. Proprietary and confidential.    

.. moduleauthor:: Nadith Pathirage <chathurdara@gmail.com>, July 2022

.. rst-class:: special

	.. centered:: Copyright3 © iMindLabs, Inc - All Rights Reserved. Unauthorized copying of this file, 
                 via any medium is strictly prohibited. Proprietary and confidential.

.. raw:: html

   <div class="copyright_container">
   <p class="copyright_header">Copyright © Declaration</p>
   <p class="copyright_body">
   Copyright © iMindLabs, Inc. All Rights Reserved. Unauthorized copying of this file, via any medium is strictly prohibited. Proprietary and confidential
   </p>
   </div>

.. raw:: latex

   \\begin{tcolorbox}[width=\\textwidth,colback={green},title={With rounded corners},colbacktitle=yellow,coltitle=blue]    
      \\blindtext[1]
      %\\includegraphics[scale=0.5]{frogimage.png}
   \\end{tcolorbox}    

   \\begin{tcolorbox}[width=\\textwidth,colback={mypink1},title={Copyright © Declaration},outer arc=0mm,colupper=white]    
      Copyright © iMindLabs, Inc. All Rights Reserved. Unauthorized copying of this file, via any 
      medium is strictly prohibited. Proprietary and confidential
      
      Contact:
      Questions? Please contact at imindlabs@gmail.com
   \\end{tcolorbox} 

.. centered:: LICENSE AGREEMENT (CENTRED BOLD TEXT)

.. glossary::

   environment
      A structure where information about all documents under the root is
      saved, and used for cross-referencing.  The environment is pickled
      after the parsing stage, so that successive runs only need to read
      and parse new and changed documents.

   source directory
      The directory which, including its subdirectories, contains all
      source files for one Sphinx project.
      
      
.. glossary::

   term 1
   term 2
      Definition of both terms.
      
.. glossary::

   term 11 : A
   term 22 : B
      Definition of both terms.
      
"""

def function(n):
    """
    Generate an number.
    
    This is extended multiple lines summary. Second line. Third line. Forth line.
    Fifth line.
    
    Parameters
    ----------
    n : int
        The upper limit of the range to generate, from 0 to `n` - 1.
        
    See Also
    --------
    pass : Description of other function.
    :py:mod:`zipfile` : Documentation of the :py:mod:`zipfile` standard module.
      
    Examples
    --------
    Examples :term:`environment` should be written in doctest format, and should illustrate how
    to use the function.

    >>> print([i for i in example_generator(4)])
    [0, 1, 2, 3]
    
    .. codeauthor:: Guido van Rossum <guido@python.org>    
    """
    pass


"""
TETTTTTTTTTTTTTTTTTTTTTTTT~
.. sectionauthor:: Guido van Rossum <guido@python.org>   
"""
def function2(n):
    """
    Generate an number2.
    
    This is extended multiple lines summary. Second line. Third line. Forth line.
    Fifth line.
    
    Parameters
    ----------
    n : int
        The upper limit of the range to generate, from 0 to `n` - 1.
        
    See Also
    --------
    pass : Description of other function.
    :py:mod:`zipfile` : Documentation of the :py:mod:`zipfile` standard module.
      
    Examples
    --------
    Examples should be written in doctest format, and should illustrate how
    to use the function.

    >>> print([i for i in example_generator(4)])
    [0, 1, 2, 3]
    
    .. codeauthor:: Guido van Rossum <guido@python.org>
    """
    pass