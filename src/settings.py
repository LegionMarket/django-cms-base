from django.utils.translations import ugettext_lazy as _

"""
Django settings for this project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y&+f+)tw5sqkcy$@vwh8cy%y^9lwytqtn*y=lv7f9t39b(cufx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    # djangocms_admin_style needs to be before django.contrib.admin!
    # https://django-cms.readthedocs.org/en/develop/how_to/install.html#configuring-your-project-for-django-cms
    'djangocms_admin_style',
    # django defaults
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # django CMS additions
    'django.contrib.sites',
    'cms',
    'treebeard',
    'menus',
    'sekizai',
    'reversion',
    # django CMS addons
    'djangocms_text_ckeditor',
    # > prerequisites for aldryn-bootstrap3
    'filer',
    'mptt',
    'easy_thumbnails',
    # > prerequisites for aldryn-newsblog
    'aldryn_apphooks_config',
    'aldryn_boilerplates',
    'aldryn_categories',
    'aldryn_people',
    'aldryn_reversion',
    'parler',
    'sortedm2m',
    'taggit',
    # > addons
    'aldryn_bootstrap3',
    'aldryn_newsblog',
    'aldryn_style',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # django CMS additions
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangocms_demo_local',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PASSWORD': '',
        'PORT': '',
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static_collected')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Templates
# https://docs.djangoproject.com/en/1.7/ref/settings/#template-context-processors

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    # django CMS additions
    'django.core.context_processors.request',
    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings',
    # aldryn-newsblog
    'aldryn_boilerplates.context_processors.boilerplate',
)

# https://docs.djangoproject.com/en/1.7/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    # aldryn-bpolerplates needs the following line to be placed exactly there
    'aldryn_boilerplates.template_loaders.AppDirectoriesLoader',
    'django.template.loaders.app_directories.Loader',
    # django CMS additions
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# django CMS settings
# http://docs.django-cms.org/en/latest/

SITE_ID = 1

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

CMS_TOOLBAR_SIMPLE_STRUCTURE_MODE = True

# django CMS internationalization
# http://docs.django-cms.org/en/latest/topics/i18n.html

LANGUAGES = (
    ('en', _('English')),
    ('de', _('Deutsch')),
)

CMS_LANGUAGES = {
    # Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': _('English'),
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': 'de',
            'hide_untranslated': False,
            'name': _('German'),
            'redirect_on_fallback': True,
        },
    ],
}

# django CMS templates
# http://docs.django-cms.org/en/latest/how_to/templates.html

CMS_TEMPLATES = (
    # Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right'),
    ('tpl_home.html', 'Home Template'),
)

# django CMS migrations for django 1.7
# https://docs.djangoproject.com/en/1.7/topics/migrations/#dependencies

# MIGRATION_MODULES = {}

# aldryn-newsblog required configurations
# DOCS: https://pypi.python.org/pypi/aldryn-boilerplates/
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # aldryn-bpolerplates needs the following line to be placed exactly there
    'aldryn_boilerplates.staticfile_finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # aldryn-newsblog neews to override the default scale_and_crop
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    'easy_thumbnails.processors.background',
)

ALDRYN_BOILERPLATE_NAME = 'bootstrap3'

# aldryn-style required configurations
# DOCS: https://github.com/aldryn/aldryn-style
ALDRYN_STYLE_CLASS_NAMES = (
    ('container', _('bootstrap container')),
)
