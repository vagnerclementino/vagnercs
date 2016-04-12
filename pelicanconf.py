#!/usr/bin/env python
# -*- coding: utf-8 -*- #
TYPOGRIFY = True
GOOGLE_ANALYTICS_CODE = 'UA-844985-1'

AUTHOR = u'Vagner Clementino'
SITENAME = u'Vagner Clementino'
SITETAGLINE = u'Simple is better than complex.'
#SITEURL = 'http://homepages.dcc.ufmg.br/~vagnercs'
SITEURL = 'http://localhost:8000'
SITELOGO = 'images/me.png'
SITEDESCR = u'Candidato a mestre em Engenharia de Software. Analista de Sistema na PRODABEL. E estou apenas começando...'

GITHUB_URL = 'https://github.com/vagnerclementino'
LINKEDIN_URL = 'https://br.linkedin.com/pub/vagner-clementino/68/95/b20'
TWITTER_URL = 'https://twitter.com/vclementino'
GOOGLE_URL = 'https://plus.google.com/+VagnerClementino'
#FLICKR_URL = 'http://flickr.com/photos/siovene'

LICENSE_NAME = 'CC BY-SA 3.0'
LICENSE_URL  = 'http://creativecommons.org/licenses/by-sa/3.0/'

TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = u'pt'
SUMMARY_MAX_LENGTH = 75

DEFAULT_PAGINATION = 10
THEME = '.theme'
STATIC_PATHS = [
    'files',
    'images',
    'cv'
]

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = ARCHIVES_URL + 'index.html'

CONTACT_URL = 'pages/contact/'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['photos']


PHOTO_LIBRARY = "pictures"