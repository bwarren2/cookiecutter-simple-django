"""Production settings and globals."""
from .base import *
from django.core.exceptions import ImproperlyConfigured
from os import environ

ADMINS = (
    ('{{cookiecutter.author_name}}', '{{cookiecutter.email}}'),
)

MANAGERS = ADMINS

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.

#  DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False
TEMPLATE_DEBUG = DEBUG


def get_env_setting(setting):
    """ Get the environment setting or return exception. """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)

MIDDLEWARE_CLASSES += (
    "{{cookiecutter.repo_name}}.middleware.ForceHttps",
)

# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'bwarren2@gmail.com.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
# END EMAIL CONFIGURATION

# Setting allowed hosts for security.  Only needed when debug = false
ALLOWED_HOSTS = (
    '{{cookiecutter.project_name}}.herokuapp.com',
)

#  CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
#  END CACHE CONFIGURATION
