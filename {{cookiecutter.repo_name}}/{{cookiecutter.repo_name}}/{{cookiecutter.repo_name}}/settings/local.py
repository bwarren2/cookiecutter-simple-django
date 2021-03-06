from .base import *


ADMINS = (
    ('{{cookiecutter.author_name}}', '{{cookiecutter.email}}'),
)

MANAGERS = ADMINS

#   DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
#   END DEBUG CONFIGURATION


#   EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#   END EMAIL CONFIGURATION


#   CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
#   END CACHE CONFIGURATION


#   TOOLBAR CONFIGURATION
# See: https://github.com/django-debug-toolbar/django-debug-toolbar/
#      #installation
INSTALLED_APPS += (
    'debug_toolbar',
    'template_timings_panel',
    'debug_toolbar_line_profiler',
    'template_profiler_panel',
)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar/
#      #installation
INTERNAL_IPS = ('127.0.0.1',)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar/
#      #installation
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
#   END TOOLBAR CONFIGURATION

# STATIC CONFIGURATION
STATIC_URL = '/assets/'
STATIC_ROOT = normpath(join(DJANGO_ROOT, 'assets'))

MEDIA_URL = '/media/'
MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'media'))

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False
}

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar_line_profiler.panel.ProfilingPanel',
    'template_timings_panel.panels.TemplateTimings.TemplateTimings',
    'template_profiler_panel.panels.template.TemplateProfilerPanel',
)

ALLOWED_HOSTS = (
    '127.0.0.1',
)
