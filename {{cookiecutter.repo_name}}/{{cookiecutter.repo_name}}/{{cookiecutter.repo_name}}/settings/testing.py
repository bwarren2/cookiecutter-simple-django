from base import *

#   TEST SETTINGS
DEBUG = False
TEMPLATE_DEBUG = False
SOUTH_TESTS_MIGRATE = False

INSTALLED_APPS += (
)


#   IN-MEMORY TEST DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}


#  STORAGE
STATICFILES_STORAGE = 'django.core.files.storage.FileSystemStorage'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
#  END STORAGE
