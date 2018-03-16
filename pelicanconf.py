#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


SITENAME = 'Badgerbones'
SITEURL = ''
THEME = "badgerbones-theme"

PATH = 'content'

TIMEZONE = 'GB'

DEFAULT_LANG = 'English'


ARTICLE_PATHS = ['articles']
ARTICLE_URL = 'articles/{date:%Y}-{date:%b}-{date:%d}-{author}-{slug}.html'
ARTICLE_SAVE_AS = 'articles/{date:%Y}-{date:%b}-{date:%d}-{author}-{slug}.html'
AUTHOR_URL = 'authors/{slug}.html'
AUTHOR_SAVE_AS = 'authors/{slug}.html'
AUTHORS_SAVE_AS = 'authors/index.html'
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
INDEX_SAVE_AS = 'articles/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
