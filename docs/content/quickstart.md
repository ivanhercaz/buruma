Title: Quickstart
Date: 2019-12-08 20:00
Status: published
Author: Ivanhercaz
Category: Documentation
Tags: quickstart, settings
Slug: quickstart
Extract: Do you want to use Buruma? Follow this quickstart guide.

Hi! If you want to use Buruma, I recommend to you to keep in mind the next things:

  - **Buruma is under development**. Its release 0.1.0 make its able to use but with risks. There are many issue to improve and to solve.
  - **Buruma might grow fast, but might grow slow too**. Everything will depends of the time available to contribute and the users involve. Thus I recommendto anyone to [report anything][buruma-issues] (suggestions, questions, bugs...). If you see something in this site or in the live demo of Buruma, please, report it!
  - **Buruma is built with Bulma**, an easy to use but powerful CSS framework. Buruma uses `node-sass` convert and minify the SCSS into the CSS, but **it isn't necessary** if you just want to use the theme. If you want to contribute to Buruma, you should follow the *Contributing guidelines* (not written yet).
  - **Buruma is to be relaxed and enjoy**. It might be a point that Buruma isn't accomplish yet due it needs more work, but the idea behind Buruma is to work as a modularized theme in which you can change the settings to adapt to your needs, so you can change the appearance of your website (colors, layout...) and its behaviour.
  - **Buruma...** What more? We need to discover!

So if you read this and you still want to test Buruma, you can follow the next instructions:

  1. Clone Buruma's repository wherever you prefer: `git@github.com:ivanhercaz/buruma.git` (with SSH) or `https://github.com/ivanhercaz/buruma.git` with HTTPS.
  2. In `pelicanconf.py` you have to change `THEME` to the theme path (e.g., `THEME = "themes/buruma"`) according to where you cloned it.
  3. In `pelicanconf.py` you have to add the i18n extension for Jinja2. For that you have to set `JINJA_ENVIRONMENT`:
```python
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"],
}
```
  4. Then you need to clone the Pelican plugins repository wherever you prefer: `git clone --recursive https://github.com/getpelican/pelican-plugins` or `git clone --recurse-submodules=i18n_subsites --shallow-submodules https://github.com/getpelican/pelican-plugins.git docs/plugins`, if you want to clone the repository itself and `i18n_subsites`, avoiding the rest of plugins included as submodules in the repository.
  5. Then you have to add `i18n_subsites` to your `pelicanconf.py`:
```python
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["i18n_subsites", ]
```
  6. Now you can generate your website! But I recommend you to read [Settings][docs-settings], after or before your first generation.

At this moment this is the only method available to use Buruma. If you have some suggestion, question or report, you can post it in the [issues][buruma-issues] section of the repository.

[buruma-issues]: <https://github.com/ivanhercaz.com/buruma/issues>
[docs-settings]: </settings>
