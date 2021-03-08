#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Sam Lewis'
SITENAME = u'Sam Lewis'
SITEURL = 'https://www.samlewis.me'
TIMEZONE = 'Australia/Brisbane'
THEME = './theme/notebook-simpler'
SUMMARY_MAX_LENGTH = 50
AVATAR = '/theme/images/avatar.jpg'
TITLE = "Sam Lewis"
DESCRIPTION = "Sam Lewis is a Melbourne based geek who develops cool bits of code. He likes data, embedded stuff and AFL."

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'


# DEFAULTS
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'misc'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d %b %Y'
DEFAULT_PAGINATION = False


# FEEDS
FEED_ALL_ATOM = "feeds/all.atom.xml"
TAG_FEED_ATOM = "feeds/tag/%s.atom.xml"


# PLUGINS
PLUGIN_PATH = './plugins/'
PLUGINS = []

CODE_DIR = 'code'
NOTEBOOK_DIR = 'notebooks'
#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

STATIC_PATHS = ['images']
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},}


# Additional
DISQUS_SITENAME = "sam-lewis"
#GOOGLE_ANALYTICS = "UA-50600593-1"
DOMAIN = "samlewis.me"

# Twitter Cards
TWITTER_CARDS = False