Title: Settings
Date: 2019-12-08 21:30
Status: published
Author: Ivanhercaz
Category: Documentation
Tags: settings, variables, pelicanconf
Slug: settings
Extract: Available setting for Buruma.

Buruma is being developed to be easy to configure and to use. One of its goals is to be able to adapt itself easily. This can be possible with a good structure that makes possible to configure everything with small changes or additions. Surely, **Buruma doesn't accomplish with this**, but I hope Buruma grows fastly.

## `pelicanconf.py`

In this section you can check the available variables to configure Buruma with your Pelican configuration file (`pelicanconf.py`).

| Variable | Description | Type | Example |
|----------|-------------|------|---------|
|`MENUITEMS_NAVBAR`|Set of items (text to show and url) in the left part of the menu of the navigation bar|Tuple|`(("Docs", "/p/docs.html"), ("Info", "/p/info.html"))`|
|`MENUITEMS_NAVBAR_FEATURED`|Set of items with an different style in the right part of the menu of the navigation bar|Tuple|`(("Docs", "/p/docs.html", "is-link"), ("Info", "/p/info", "is-info"))`|
|`NAVBAR_STYLE`|CSS class for the navigation bar (see section *Buruma SCSS/CSS*|String|`is-info`, `is-warning`|
|`CATS_STYLE`|Allow to apply a CSS class to elements (e.g., entries) of the specified categories|Dictionary|`{"Example cat 1": "is-info", "Example cat 2": "is-link"}`|
|`FOOTER`|Customized HTML snippet to replace the default text in the footer|Tuple (multiline string)||
|`LICENSE`|If it is `True`, show the customized `LICENSE_NOTICE`, if it is `False` or it isn't declared, show a copyright notice|Boolean||
|`LICENSE_NOTICE`|Allow to add a HTML snippet to add a license|Tuple (multiline string)||
|`ABOUT_EXTRACT_STATUS`|If it is `True`, show the customized `ABOUT_EXTRACT`|Boolean||
|`ABOUT_EXTRACT`|Allow to add a HTML snippet to add an extract about the site (or whatever) between the navigation bar and the content. It is only shown in the home page|Tuple (multiline string)||
