.. |foundation| replace:: Foundation 4
.. _foundation: http://foundation.zurb.com/

=======================
Sphinx Foundation Theme
=======================

This is a Sphinx theme based on the |foundation|_ css framework.
It was created as a by-product of the `Authomatic <http://peterhudec.github.io/authomatic>`_
authentication / authorization library.

Features
--------

*	Responsive design
*	Support for SVG in ``<img/>`` tags with fallback to PNG
*	Google Analytics support
*	Fork Me On Github support
*	SEO rudiments
	
	*	SEO meta tags
	*	Open Graph meta tags
	*	Facebbok, Twitter and Google+ social buttons
	*	Authorship Google Rich Snippet

Usage
-----

Set the ``html_theme`` variable to ``'foundation'``.

.. code-block:: python
	
	# conf.py

	html_theme_path = ['_themes/foundation-sphinx-theme']
	html_theme = 'foundation'

You also need to add the ``foundation`` extension in the ``conf.py``.
The extension just injects some foundation |foundation|_ css classes
needed for creation of the top bar navigation.

.. code-block:: python
	
	# conf.py

	sys.path[0:0] = [os.path.abspath('_themes/foundation-sphinx-theme')]
	extensions = ['sphinx.ext.autodoc', 'foundation']

Styles
^^^^^^

There are two ready made styles.

*	``foundation/css/basic.css`` `See demo. <http://peterhudec.github.io/foundation-sphinx-theme/basic/html/>`_
*	``foundation/css/cards.css`` `See demo. <http://peterhudec.github.io/foundation-sphinx-theme/cards/html/>`_

If you want to customize them or make your own,
extend the ``sass`` sources in ``foundation/static/foundation/sass``.

Page Specific SEO Description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the ``..seo-description::`` directive if you want to have different SEO description
than the one specified in ``html_theme_options`` for a specific document/page.
The directive can appear anywhere in the document.
If you specify more than one, the content of the last one will be used.

.. code-block:: rst
	
	.. seo-description::

		Content of this directive overrides the seo_description
		in the html_theme_options only for this page.

	======================
	Title of Your Document
	======================

	.. seo-description::
	   
	   Value of the last seo-description directive will be used.

Options
^^^^^^^

There are these theme options available:

.. code-block:: python
	
	# conf.py
	
	html_theme_options = {
		'motto': 'Long description which appears next to logo.',

		# Your stylesheet relative to the _static dir.
		# Default is 'foundation/css/basic.css'
		'stylesheet': '/path/to/your/stylesheet.css',

		# Logo image in SVG format. If the browser doesn't support SVG
		# It will try to load JPG with the same name.
		'logo_screen': '',

		# Logo for small screens. If ommited, logo_screen will be used.
		'logo_mobile': '',

		# Path to your favicon.ico file relative to the _static dir.
		'favicon': '',

		# Use this if the top-level items of the toctree don't fit in the top-bar navigation.
		# If True, the whole toctree will be placed inside a single top-level item.
		'top_bar_force_fit': True,

		# The title of the aformentioned top-level item. Default is "Sections"
		'top_bar_content_title': 'Sections',

		# If set, Google Analytics code will be appended to body of each page.
		'google_analytics_id': 'your-google-analytics-id',

		# The "og:title", "og:type", "og:url", "og:site_name" and "og:description" Open Graph tags
		# will be generated automatically, but you should specify the
		# path to the image that you want to be used
		# in the required "og:image" property relative to the _static dir.
		'opengraph_image': 'path/to/your/opengraph-image.jpg',

		# Any custom additional OG tags
		'opengraph_tags': {
			'foo': 'bar', # will be rendered as <meta property="og:foo" content="bar" />
		},

		# The "description" meta tag will be created automatically, but
		# you can specify additional meta tags here.
		'meta_tags': {
			'foo': 'bar', # will be rendered as <meta name="foo" content="bar">
		},

		# The value for "description" and "og:description" metatags.
		# If omitted, the value of "motto" will be used.
		'seo_description': 'This is an example of the Foundation Sphinx Theme output.',

		# Use this as the base for Open Graph URLs without trailing slash.
		'base_url': 'http://example.com',

		# If true a bar with Facebook, Google+ and Twitter social buttons will be displayed
		# underneath the header.
		'social_buttons': True,

		# ID of your Facebook app associated with the Facebook Like button.
		'facebook_app_id': '123456789',

		# A Twitter ID used for the via mention of the Twitter button.
		'twitter_id': 'FoundationSphinx',

		# Flattr button settings.
		'flattr_id': 'andypipkin', # Your Flattr ID
		'flattr_title': '', # If missing docstitle or title will be used.
		'flattr_description': '', # If missing seo_description or motto will be used.
		'flattr_tags': '', # Optional.


		# If "author" and "copyright_year" are set they will override the "copyright" setting.

		# Author's name.
		'author': 'Peter Hudec',

		# Author's link.
		'author_link': 'http://peterhudec.com',

		# Year to be used in the copyright statement.
		'copyright_year': '2013',

		# Author's Google+ id. If set a G+ authorship link will be added.
		'google_plus_id': '117034840853387702598',


		# Fork me on GitHub ribbon will be displayed if "github_user", "github_repo" and "github_ribbon_image" are set:
		# https://github.com/blog/273-github-ribbons
		# Ribbons are hidden on small screens!

		# Your GitHub ID.
		'github_user': 'foundation-sphinx-theme',

		# The repository slug.
		'github_repo': 'foundation-sphinx-theme',

		# Path to the ribbon image relative to the "_static" directory.
		'github_ribbon_image': 'my-github-ribbon.png',

		# Position of the ribbon "left" or "right".
		'github_ribbon_position': 'right',
	}

