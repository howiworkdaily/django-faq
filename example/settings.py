#
# A minimal settings file that ought to work out of the box for just about
# anyone trying this project. It's deliberately missing most settings to keep
# everything simple.
#
# A real app would have a lot more settings. The only important bit as far as
# django-FAQ is concerned is to have `faq` in INSTALLED_APPS.
#

import os

PROJECT_DIR = os.path.dirname(__file__)
DEBUG = TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'faq.db'),
    }
}

SITE_ID = 1
SECRET_KEY = 'c#zi(mv^n+4te_sy$hpb*zdo7#f7ccmp9ro84yz9bmmfqj9y*c'
ROOT_URLCONF = 'urls'
TEMPLATE_DIRS = (
    [os.path.join(PROJECT_DIR, "templates")]
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',

    # Database migration helpers
    'south',

    'faq',
)