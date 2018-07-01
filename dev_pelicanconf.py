#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Laura Santamaria'
SITENAME = 'Personal Site'
SITEURL = './'

PATH = 'content'
OUTPUT_PATH = 'docs'

TIMEZONE = 'America/Chicago'

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

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme info
THEME = './theme'
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']

# static files
STATIC_PATHS = [
    'favicon.ico'
]

# Plugins
PLUGIN_PATHS = ['hidden/pelican-plugins']
PLUGINS = [
    'assets'
]

# Pages
PAGE_SAVE_AS = '{slug}.html'

# webassets
# JINJA_ENVIRONMENT = {'webassets.ext.jinja2AssetsExtension': True}
# WEBASSETS = True
# ASSET_SOURCE_PATHS = ['static/css']
# ASSET_URL = 'theme'
# ASSET_DEBUG = True
