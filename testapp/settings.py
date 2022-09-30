import os
from pathlib import Path

from django.urls import reverse_lazy
from django.utils.text import format_lazy


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'secret_key')

DEBUG = bool(os.getenv('DJANGO_DEBUG', True))

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'treebeard',
    'sekizai',
    'django_select2',
    'easy_thumbnails',
    'filer',
    'cms',
    'djangocms_versioning',
    'menus',
    'djangocms_text_ckeditor',
    'cmsplugin_cascade',
    'cmsplugin_cascade.extra_fields',
    'testapp',
]

if True or os.getenv('DATABASE_ENGINE') == 'postgres':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'test_cms',
            'USER': 'djangocms',
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
            'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
            'PORT': os.getenv('POSTGRES_PORT', 5432),
            # 'CONN_MAX_AGE': 900,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': Path(os.getenv('DJANGO_WORKDIR', BASE_DIR / 'workdir')) / 'testapp.sqlite3',
            'TEST': {
                'NAME': Path(__file__).parent / 'test.sqlite3',  # live_server requires a file rather than :memory:
                'OPTIONS': {
                    'timeout': 20,
                },
            },
        }
    }

SITE_ID = 1

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

USE_I18N = True

USE_TZ = True

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', "English"),
    ('de', "Deutsch"),
]

CMS_LANGUAGES = {
    'default': {
        'fallbacks': ['en', 'de'],
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
    1: ({
        'code': 'en',
        'name': "English",
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    }, {
        'code': 'de',
        'name': "Deutsch",
        'public': True,
        'hide_untranslated': True,
        'redirect_on_fallback': True,
    }),
}

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
]

ROOT_URLCONF = 'testapp.urls'

STATIC_ROOT = os.getenv('DJANGO_STATIC_ROOT', BASE_DIR / 'workdir/static')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    ('node_modules', BASE_DIR / 'node_modules'),
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

MEDIA_ROOT = Path(os.getenv('DJANGO_MEDIA_ROOT', BASE_DIR / 'workdir/media'))

MEDIA_URL = '/media/'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'tests/templates'],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'sekizai.context_processors.sekizai',
            'cms.context_processors.cms_settings',
        ],
    },
}]

WSGI_APPLICATION = 'wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'}},
    'formatters': {
        'simple': {
            'format': '[%(asctime)s %(module)s] %(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

CMS_CONFIRM_VERSION4 = True

CMS_TEMPLATES = [
    ('testapp/default.html', "Default"),
]

CMSPLUGIN_CASCADE_PLUGINS = [
    'cmsplugin_cascade.generic',
]

CMSPLUGIN_CASCADE = {
    'register_page_editor': False,
}

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'skin': 'moono-lisa',
    'toolbar_CMS': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        '/',
        ['Bold', 'Italic', 'Underline', 'Strike', '-',
            'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
        ['HorizontalRule'],
        ['NumberedList', 'BulletedList', 'Outdent', 'Indent'],
        ['Table', 'Source']
    ],
    'stylesSet': format_lazy('default:{}', reverse_lazy('admin:cascade_texteditor_config')),
}

SELECT2_CSS = 'node_modules/select2/dist/css/select2.min.css'
SELECT2_JS = 'node_modules/select2/dist/js/select2.min.js'
SELECT2_I18N_PATH = 'node_modules/select2/dist/js/i18n'
