.. seo-description::
   
   Content of this directive overrides the seo_description
   in the html_theme_options only for this page.
   But it will be overriden wit the next directive.

.. seo-description::
   
   Value of the last seo-description directive will be used.

=========
Reference
=========

Lorem ipsum dolor sit amet, ``magna offendit`` similique ne nec.
Ex doming sanctus labores pro, est ne dico simul laboramus.
Eam ad sint accumsan percipitur, dicta ubique expetendis ne sed.
Cu ipsum percipit electram sed. Per recusabo convenire definiebas an.
Cu atomorum splendide nec, id qui suas urbanitas.


Functions
=========

.. function:: foo(bar, baz=None)
   
   Lorem ipsum dolor sit amet, ``magna offendit`` similique ne nec.
   Ex doming sanctus labores pro, est ne dico simul laboramus.
   
   .. note::
   
      Admonition ``inside`` function docstring.
   
   :param str bar:
      Lorem ipsum dolor sit amet, magna offendit similique ne nec.
      
      .. tip::
      
         Admonition inside ``function`` parameters comment.
   
   :param bool baz:
      Ex doming sanctus labores pro, est ne dico simul laboramus.
   
   :returns:
      Eam ad sint accumsan percipitur, dicta ubique expetendis ne sed.

.. function:: bar(baz, *args, **kwargs)
   
   Lorem ipsum dolor sit amet, magna offendit similique ne nec.
   Ex doming sanctus labores pro, est ne dico simul laboramus.
   
   :param str bar:
      Lorem ipsum dolor sit amet, magna offendit similique ne nec.
   
   :returns:
      Eam ad sint accumsan ``percipitur``, dicta ubique expetendis ne sed.

Classes
=======

.. class:: Foo
   
   Lorem ipsum dolor sit amet, magna offendit similique ne nec.
   Ex doming sanctus labores pro, est ne dico simul laboramus.
   
   .. warning::
   
      Admonition inside class docstring.
   

   .. py:attribute:: bar
      
      Ex doming sanctus labores pro, est ne dico simul laboramus.
      
      .. note::
   
         Admonition inside attribute comment.
      
            Blockquoute text inside admonition
      
   
   .. py:attribute:: baz
      
      Eam ad sint accumsan percipitur, dicta ubique expetendis ne sed.
      
   .. method:: foo(bar, baz)
      
      Cu ipsum percipit electram sed. Per recusabo convenire definiebas an.
      
      .. tip::
   
         Admonition inside method docstring.
      
      :param str bar:
         Lorem ipsum dolor sit amet, magna offendit similique ne nec.
      
      :param bool baz:
         Ex doming sanctus labores pro, est ne dico simul laboramus.
      
      :returns:
         Eam ad sint accumsan percipitur, dicta ubique expetendis ne sed.
      
      
   .. staticmethod:: foo_static(bar, baz)
      
      Cu atomorum splendide nec, id qui suas urbanitas.
      
      :param str bar:
         Lorem ipsum dolor sit amet, magna offendit similique ne nec.
      
      :param bool baz:
         Ex doming sanctus labores pro, est ne dico simul laboramus.
      
      :returns:
         Eam ad sint accumsan percipitur, dicta ubique expetendis ne sed.
      
   .. classmethod:: foo_class(bar, baz)
      
      Quem wisi elaboraret ut pro. Qui augue comprehensam ne.
      
      :param str bar:
         Lorem ipsum dolor sit amet, magna offendit similique ne nec.
      
      :param bool baz:
         Ex doming sanctus labores pro, est ne dico simul laboramus.
      
      :returns:
         Eam ad sint accumsan percipitur, dicta ubique expetendis ne sed.
         
         .. warning::
      
            Admonition inside method return comment.
            


.. class:: Bar
   
   Lorem ipsum dolor sit amet, magna offendit similique ne nec.
   Ex doming sanctus labores pro, est ne dico simul laboramus.
   
   .. py:attribute:: bar
      
      Ex doming sanctus labores pro, est ne dico simul laboramus.
   
   .. py:attribute:: baz
      
      Eam ad sint accumsan percipitur, dicta ubique expetendis ne sed.
      
   .. method:: foo(bar, baz)
      
      Cu ipsum percipit electram sed. Per recusabo convenire definiebas an.
      
      :param str bar:
         Lorem ipsum dolor sit amet, magna offendit similique ne nec.
      
      :param bool baz:
         Ex doming sanctus labores pro, est ne dico simul laboramus.
      
      :returns:
         Eam ad sint accumsan percipitur, dicta ubique expetendis ne sed.
      
      
   .. staticmethod:: foo_static(bar, baz)
      
      Cu atomorum splendide nec, id qui suas urbanitas.
      
      :param str bar:
         Lorem ipsum dolor sit amet, magna offendit similique ne nec.
      
      :param bool baz:
         Ex doming sanctus labores pro, est ne dico simul laboramus.
      
      :returns:
         Eam ad sint accumsan percipitur, dicta ubique expetendis ne sed.
      
   .. classmethod:: foo_class(bar, baz)
      
      Quem wisi elaboraret ut pro. Qui augue comprehensam ne.
      
      :param str bar:
         Lorem ipsum dolor sit amet, magna offendit similique ne nec.
      
      :param bool baz:
         Ex doming sanctus labores pro, est ne dico simul laboramus.
      
      :returns:
         Eam ad sint accumsan percipitur, dicta ubique expetendis ne sed.
      
   