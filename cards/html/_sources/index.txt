=============================
 Foundation Sphinx Theme Demo
=============================

This is a simple demo of the `Foundation Sphinx theme <http://github.com/peterhudec/foundation-sphinx-theme>`_.

This is a ``literal``, this is a link to :func:`foo` function and this to :class:`Bar` class.

Contents
========

.. toctree::
   
   self
   very/index
   reference


Headings
========
This is a first level heading.

Sub-Heading
-----------
This is a second level heading.

Sub-Sub-Heading
~~~~~~~~~~~~~~~
This is a third level heading.


Directives
==========

This is table of contents

.. contents:: Table of Contents

This is a topic:

.. topic:: Topic Title

    Lorem ipsum dolor sit amet, mea quot omnes appellantur ne. Iisque imperdiet has ut.

This is sidebar:
   
.. sidebar:: Sidebar Title
   :subtitle: Optional Sidebar Subtitle

   Lorem ipsum dolor sit amet, magna offendit similique ne nec.
   Ex doming sanctus labores pro, est ne dico simul laboramus.

Lorem ipsum dolor sit amet, magna offendit similique ne nec.
Ex doming sanctus labores pro, est ne dico simul laboramus.
Eam ad sint accumsan percipitur, dicta ubique expetendis ne sed.
Cu ipsum percipit electram sed. Per recusabo convenire definiebas an.
Cu atomorum splendide nec, id qui suas urbanitas.

Esse causae assentior no nec. Et justo veniam feugiat nam, elitr referrentur in est.
Dicant suscipit salutatus eum ea. Ne mei vocibus appetere democritum,
ut mel elitr graecis antiopam. Per ut vocent eripuit, duo et libris ceteros pertinacia,
cu quo erat feugiat dissentias.

Eum nemore ocurreret accusamus ne, veri verterem electram usu no.
Tantas assueverit usu cu, in quo lorem ornatus erroribus.
Dicant periculis iracundia nec ea, indoctum pericula necessitatibus eum an.
Cum ex civibus singulis adversarium, fuisset scripserit an quo. Eos elit platonem id.

This is epigraph:

.. epigraph::

   No, but, yeah, but, no, but, yeah, but, no, but, yeah but
   I know because I'm not wasting police time because you know Micha?
   Well, she saw the whole thing, right, because she was bunking off school because
   she was gonna go down the wimbley and get off with Luke Griffiths,
   only she never because he's been trying to grow a moustache but
   it just looks like pubes, so she got off with Luke Torbet instead,
   only don't tell Bethany that because she's fancied Luke Torbet ever since
   she flashed her fanny at him during Home Ec'.

   -- Vicky Pollard


This is compound:

.. compound::

   Lorem ipsum dolor sit amet, magna offendit similique ne nec.
   Ex doming sanctus labores pro, est ne dico simul laboramus.
   Eam ad sint accumsan percipitur, dicta ubique expetendis ne sed.
   Cu ipsum percipit electram sed. Per recusabo convenire definiebas an.
   Cu atomorum splendide nec, id qui suas urbanitas.

.. glossary::

   lorem
      Lorem ipsum dolor sit amet, magna offendit similique ne nec.
      Ex doming sanctus labores pro, est ne dico simul laboramus.
      Eam ad sint accumsan percipitur, dicta ubique expetendis ne sed.
      Cu ipsum percipit electram sed. Per recusabo convenire definiebas an.
      Cu atomorum splendide nec, id qui suas urbanitas.

   ipsum
      Lorem ipsum dolor sit amet, magna offendit similique ne nec.
      Ex doming sanctus labores pro, est ne dico simul laboramus.
      Eam ad sint accumsan percipitur, dicta ubique expetendis ne sed.
      Cu ipsum percipit electram sed. Per recusabo convenire definiebas an.
      Cu atomorum splendide nec, id qui suas urbanitas.


Admonitions
===========

Yellow
------

.. note:: This is a note.

.. hint:: Hint.

Green
-----

.. tip:: Tip.

.. seealso:: See also.

Red
---

.. attention:: Attention.

.. caution::Caution.

.. danger:: Danger.

.. error:: Error.

.. warning:: Warning.

.. important:: Important.

Lists
=====

* This is a bulleted list.
* It has two items, the second
  item uses two lines.

1. This is a numbered list.
2. It has two items too.

#. This is a numbered list.
#. It has two items too.

* this is
* a list

  * with a nested list
  * and some subitems

* and here the parent list continues

.. hlist::
   :columns: 3

   * A list of
   * short items
   * that should be
   * displayed
   * horizontally


Tables
======

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+

=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

Code
====

Highlighting respects the pygments theme, except for background.

::

    from foo import bar
    
    # Comment
    
    class Foo(bar.Bar):
      """
      Foo bar baz.
      """
      
      def bar(arg_1=1, arg_2=2):
         print arg_1 + arg_2
    
    d = {'a': 1, 'b': 2}

Footnotes
=========

Lorem ipsum [Ref1]_ dolor sit amet [Ref2]_, mea quot omnes appellantur ne [Ref3]_. Iisque imperdiet has ut.

.. [Ref1] Book or article reference, URL or whatever.

.. [Ref2] Book or article reference, URL or whatever.

.. [Ref3] Book or article reference, URL or whatever.

