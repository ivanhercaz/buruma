#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Buruma Team'
SITENAME = 'Buruma Documentation'
SUBTITLE = "A Pelican theme based on Bulma and flexbox"
SITENAME_SLOGAN = SUBTITLE
SITEURL = ''

PATH = 'content'

# Region/lang
TIMEZONE = 'Europe/London'
DATE_FORMATS = {"en": "%b %d, %Y"}
DEFAULT_LANG = 'en'

# Feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# NOT INTEGRATED
"""
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)
"""

# Social widget
# NOT INTEGRATED
"""
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
"""

DEFAULT_PAGINATION = 5

# Theme
THEME = "../"

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["i18n_subsites", ]
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"],
}

# Buruma settings
MENUITEMS_NAVBAR = ()

MENUITEMS_NAVBAR_FEATURED = (("Contact",
                              "/contact",
                              "is-link"),
                             ("GitHub",
                              "https://github.com/ivanhercaz/buruma",
                              "is-primary"),
                             ("Report",
                              "https://github.com/ivanhercaz/buruma/issues",
                              "is-warning"))

NAVBAR_STYLE = "is-info"
CATS_STYLE = {"Documentation": "is-primary",}

FOOTER = ("Este sitio web funciona gracias a <a href='https://getpelican.com'>Pelican</a>, "
          "un gestor de contenido desarrollado en <a href='https://python.org'>Python</a> y "
          "utiliza la plantilla <a href='https://github.com/ivanhercaz/buruma'>Buruma</a>.")

LICENSE = True
LICENSE_NOTICE = ("<p><a rel='license' href='https://creativecommons.org/licenses/by-sa/4.0/'>"
                  "<img alt='Licencia Creative Commons' style='border-width: 0'"
                  "src='https://i.creativecommons.org/l/by-sa/4.0/88x31.png' /></a><br />This "
                  "work is under a <a rel='license' class='license-text'"
                  "href='https://creativecommons.org/licenses/by-sa/4.0'>Creative Commons "
                  "Attribution-ShareAlike 4.0 International license</a>.")

ABOUT_EXTRACT_STATUS = False
ABOUT_EXTRACT = ("<p>Here you can find the documentation about Buruma, a Pelican theme built with "
                 "Bulma, a modern CSS framework based on Flexbox. If you don't find "
                 "something, you can <a href='https://github.com/ivanhercaz/buruma/issues'>report "
                 "it</a>. Your issue will be attended as soon as possible.</p>"
                 "<p>Do you miss something on Buruma? "
                 "<a href='https://github.com/ivanhercaz/buruma/issues'>Ask for it!</a> Buruma is"
                 "a new born theme, so it may lack many interesting features.</p>")
