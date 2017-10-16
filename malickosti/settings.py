"""
Django settings for malickosti project.
"""

import os

from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'vsxmbp&_ch-gv=42=oz*8sqghmqif$)n###*1@+1p6h#t^sep9'
DEBUG = True
ALLOWED_HOSTS = ['localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'markdownify',
    'web',
    'captcha',
    'storages',
    'imagekit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'malickosti.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'web.context_processors.get_cart',
            ],
        },
    },
]


WSGI_APPLICATION = 'malickosti.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGES = [
    ('cs', _('Česky')),
]

LANGUAGE_CODE = 'cs-cz'
LOCALE_PATHS = [
    BASE_DIR + '/web/locale',
]

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DATABASE_BACKUP_FILES_LOCATION = 'dbbackup'
MEDIA_FILES_LOCATION = 'media'
STATIC_FILES_LOCATION = 'static'

MEDIA_URL = '/%s/' % MEDIA_FILES_LOCATION
STATIC_URL = '/%s/' % STATIC_FILES_LOCATION

MARKDOWNIFY_WHITELIST_TAGS = [
    'a',
    'abbr',
    'acronym',
    'b',
    'blockquote',
    'em',
    'i',
    'li',
    'ol',
    'p',
    'strong',
    'ul',
    'h2',
    'h3',
    'h4',
    'h5',
]

RECAPTCHA_PUBLIC_KEY = 'MyRecaptchaKey123'
RECAPTCHA_PRIVATE_KEY = 'MyRecaptchaPrivateKey456'
NOCAPTCHA = True
EMAIL_ORDER_SENDER = 'objednavky@terkyakvarelky.cz'

AWS_ACCESS_KEY_ID = None
AWS_SECRET_ACCESS_KEY = None
AWS_STORAGE_BUCKET_NAME = None
AWS_QUERYSTRING_AUTH = False
AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'

try:
    from local_settings import *  # noqa
except ImportError:
    pass

CORS_ORIGIN_WHITELIST = ALLOWED_HOSTS
EMAIL_ORDER_SENDER = 'objednavky@%s' % ALLOWED_HOSTS[0]
EMAIL_CONTACT_FALLBACK_SENDER = 'kontakt@%s' % ALLOWED_HOSTS[0]
EMAIL_MANAGER = 'test@example.com'

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if AWS_ACCESS_KEY_ID and AWS_STORAGE_BUCKET_NAME:
    DEFAULT_FILE_STORAGE = 'malickosti.storages.MediaStorage'
    STATICFILES_STORAGE = 'malickosti.storages.StaticStorage'
    DBBACKUP_STORAGE = 'malickosti.storages.DatabaseBackupStorage'
    DBBACKUP_STORAGE_OPTIONS = {
        'access_key': AWS_ACCESS_KEY_ID,
        'secret_key': AWS_SECRET_ACCESS_KEY,
        'bucket_name': AWS_STORAGE_BUCKET_NAME,
    }
