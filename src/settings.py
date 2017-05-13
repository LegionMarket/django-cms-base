"""
Django settings for this project.

Generated by 'django-admin startproject' using Django 1.10.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

from django.utils.translation import ugettext_lazy as _
from cmsplugin_cascade.utils import format_lazy
from django.core.urlresolvers import reverse_lazy


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y&+f+)tw5sqkcy$@vwh8cy%y^9lwytqtn*y=lv7f9t39b(cufx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Enable this to additionally show the debug toolbar
# INTERNAL_IPS = ['localhost', '127.0.0.1']


# Application definition

DJANGO_APPS = (
    # djangocms_admin_style needs to be before django.contrib.admin!
    # https://django-cms.readthedocs.org/en/develop/how_to/install.html#configuring-your-project-for-django-cms
    'jet',
    'jet.dashboard',
    # 'djangocms_admin_style',

    # django defaults
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',

)
DJANGO_CMS = (
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    # 'reversion',
    # requirements for django-filer
    'filer',
    'easy_thumbnails',
    'mptt',
    # core addons
    'djangocms_text_ckeditor',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_snippet',
    'djangocms_style',
    'djangocms_googlemap',
    'djangocms_video',
    'djangocms_audio',

)
DJANGO_CMS_ADDONS = (
    # Cassaade
    'cmsplugin_cascade',
    'cmsplugin_cascade.clipboard',
    'cmsplugin_cascade.sharable',
    'cmsplugin_cascade.extra_fields',
    'cmsplugin_cascade.icon',
    'cmsplugin_cascade.segmentation',

)

THIRD_PARTY_APPS = (
    'embed_video',
)

LOCAL_APPS = (
    'video_back',

)

INSTALLED_APPS = DJANGO_APPS + DJANGO_CMS + DJANGO_CMS_ADDONS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    # its recommended to place this as high as possible to enable apphooks
    # to reload the page without loading unnecessary middlewares
    'cms.middleware.utils.ApphookReloadMiddleware',
    # django defaults
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # django CMS additions
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = 'src.urls'

WSGI_APPLICATION = 'src.wsgi.application'


# Templates
# https://docs.djangoproject.com/en/1.8/ref/settings/#templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # additional context processors for local development
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                # django CMS additions
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                # django CMS additions
                'django.template.loaders.eggs.Loader',
            ],
            'debug': DEBUG,
        },
    },
]


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# we use os.getenv to be able to override the default database settings for the docker setup

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# we need to add additional configuration for filer etc.
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# django CMS settings
# http://docs.django-cms.org/en/latest/

SITE_ID = 1

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {

}

CMS_PAGE_WIZARD_CONTENT_PLACEHOLDER = 'content'


# django CMS internationalization
# http://docs.django-cms.org/en/latest/topics/i18n.html

LANGUAGES = (
    ('en', _('English')),
)

# django CMS templates
# http://docs.django-cms.org/en/latest/how_to/templates.html

CMS_TEMPLATES = (
    ('content.html', 'Content'),
    ('t458_lavish/index.html', 'TLM-Lavish')
)

# CUSTOM

# Filer
THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

# CKEditor
# DOCS: https://github.com/divio/djangocms-text-ckeditor
# CKEDITOR_SETTINGS = {
#     'stylesSet': 'default:/static/js/addons/ckeditor.wysiwyg.js',
#     'contentsCss': ['/static/css/base.css'],
# }

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'skin': 'moono',
    'toolbar': 'CMS',
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', 'Styles'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        ['HorizontalRule'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table'],
        ['Source']
    ],
    'stylesSet': format_lazy('default:{}', reverse_lazy('admin:cascade_texticon_wysiwig_config')),
}

CKEDITOR_SETTINGS_CAPTION = {
    'language': '{{ language }}',
    'skin': 'moono',
    'height': 70,
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['Format', 'Styles'],
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['Source']
    ],
}

CKEDITOR_SETTINGS_DESCRIPTION = {
    'language': '{{ language }}',
    'skin': 'moono',
    'height': 250,
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', 'Styles'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        ['HorizontalRule'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table'],
        ['Source']
    ],
}
# Embed Video
APPEND_SLASH = True