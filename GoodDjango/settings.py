#coding:utf-8
"""
Django settings for GoodDjango project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7by!@@7!ifzef$ys(mt9+)32)8_&*%xxdovvt1uwnaiy=40w^+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'blog',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'suit',
    'django.contrib.admin',

    'south',
    'django_select2',
    'suit_redactor',
    'suit_ckeditor',
    'import_export',
    'reversion',
    'django_extensions',


)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
'django.core.context_processors.request',
)

# In settings.py
TEMPLATE_DIRS = {
    os.path.join(BASE_DIR, "templates"),
}


# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': '信息管理系统',
    # 'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_DATE_FORMAT': 'Y%sm%sd%s l' %('年','月','日'),
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/blog/Author/',
    'MENU_ICONS': {
       'sites': 'icon-leaf',
       'auth': 'icon-lock',
    },
    'MENU_OPEN_FIRST_CHILD': True, # Default True
    'MENU_EXCLUDE': ('auth.group',),

    'MENU':(
        # Rename app and set icon
        # 'sites',

        # '-',
        {'app': 'auth', 'label':u'权限组','model': ('user','group'), 'icon': 'icon-lock'},

        # {'app':'blog','label':u'作者相关','model':(
        #   'Qualification','Mark','Author','Myobject','Adress'),'icon': 'icon-leaf'},

        {'label': u'基础数据', 'icon':'icon-cog', 'models': (
            {'label': "物品归属(含物品编辑)", 'url': '/admin/blog/objectattribution'},
             {'label': '相关标签', 'url': '/admin/blog/mark'},
             {'label': '资质说明', 'url': '/admin/blog/qualification'},
             {'label': '物品材料构成', 'url': '/admin/blog/material'},
        )},

   		{'label': u'作者相关', 'icon':'icon-cog', 'models': (
            {'label': "个人博客", 'url': '/admin/blog/author'},
             {'label': '物品列表', 'url': '/admin/blog/myobject'},
             {'label': '地址', 'url': '/admin/blog/adress'},
        )},

        {'label': u'自定义连接', 'icon':'icon-cog', 'models': (
            {'label': "AllenLee's Blog", 'url': '/admin/custom'},
             {'label': '404 error page', 'url': '/admin/nonexist'}
        )},
    ),

    # misc
    'LIST_PER_PAGE': 15
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'GoodDjango.urls'

WSGI_APPLICATION = 'GoodDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_DIRS = {
    os.path.join(BASE_DIR, "static"),
}

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = '/media/'