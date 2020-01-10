#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Buruma Team'
SITENAME = 'Buruma Demo Site'
SITEURL = 'https://netlify--affectionate-hypatia-0ab213.netlify.com/'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Buruma configuration
THEME = "../"

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["i18n_subsites", ]
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"],
}

MENUITEMS_NAVBAR = (('Home', SITEURL),
                    ('About', '/p/about.html'),
                    ('Docs', 'p/docs.html'),
                    ('Contact', 'p/contact.html'))

MENUITEMS_NAVBAR_FEATURED = (("Featured 1", "#", "is-info"),
                             ("Featured 2", "#", "is-primary"),
                             ("Featured 3", "#", "is-warning"))

NAVBAR_STYLE = "is-link"
CATS_STYLE = {"Conocimiento libre": "is-primary",
              "Divulgación científica": "is-success",
              "Meta": "is-warning"}

FOOTER = ("This website is generated thanks to <a href='https://getpelican.com'>Pelican</a>, "
          "a content management system developed in <a href='https://python.org'>Python</a>. "
          "It is using <a href='https://github.com/ivanhercaz/buruma'>Buruma</a>.")

LICENSE = True
LICENSE_NOTICE = ("<p><a rel='license' href='https://creativecommons.org/licenses/by-sa/4.0/'>"
                  "<img alt='Licencia Creative Commons' style='border-width: 0'"
                  "src='https://i.creativecommons.org/l/by-sa/4.0/88x31.png' /></a><br />This "
                  "work is under a <a rel='license' class='license-text'"
                  "href='https://creativecommons.org/licenses/by-sa/4.0'>Creative Commons "
                  "Attribution-ShareAlike 4.0 International license</a>.")


ABOUT_EXTRACT_STATUS = True
ABOUT_EXTRACT = ("<p>Cat ipsum dolor sit amet, throw down all the stuff in the kitchen. Stand in "
                 "front of the computer screen leave dead animals as gifts, or in the middle of "
                 "the night i crawl onto your chest and purr gently to help you sleep or scratch "
                 "at the door then walk away howl uncontrollably for no reason catty ipsum for "
                 "leave buried treasure in the sandbox for the toddlers.</p>")
