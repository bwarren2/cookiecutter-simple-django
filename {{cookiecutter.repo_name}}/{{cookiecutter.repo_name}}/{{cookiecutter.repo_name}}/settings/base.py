import sys
from os.path import join, abspath, dirname, normpath, basename
from os import getenv
import dj_database_url
from sys import path

# PATH vars


BASE_DIR = dirname(dirname(abspath(__file__)))

# PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(dirname(abspath(__file__))))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

path.append(DJANGO_ROOT)

sys.path.insert(
    0,
    normpath(join(SITE_ROOT, 'apps')),
)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
)

THIRD_PARTY_APPS = (
    'corsheaders',
    # 'social.apps.django_app.default',
    # 'storages',
    # 'bootstrapform',
    # 'corsheaders',
    # 'payments',
    # 'django_forms_bootstrap',
    # 'tagging',
    # 'mptt',
    # 'rest_framework',
)


# Apps specific for this project go here.
LOCAL_APPS = (
)

PROJECT_APPS = ()

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

ROOT_URLCONF = '{{cookiecutter.repo_name}}.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{cookiecutter.repo_name}}.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {}
DATABASES['default'] = dj_database_url.config(
    default="postgres://localhost/{{cookiecutter.repo_name}}"
)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'  # 'Europe/London'

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# MEDIA CONFIGURATION
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
MEDIA_URL = '/media/'
# END MEDIA CONFIGURATION


# STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATIC_ROOT = normpath(join(DJANGO_ROOT, 'assets'))
STATIC_URL = '/assets/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/
#      #std:setting-STATICFILES_DIRS
# Note: There is a presumption that the first entry here is 'static' so that
# trash dirs work.
STATICFILES_DIRS = (
    normpath(join(DJANGO_ROOT, 'static')),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [normpath(join(DJANGO_ROOT, 'templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]
