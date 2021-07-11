from .base import *  # noqa


DEBUG = True

INSTALLED_APPS += ["debug_toolbar"]  # noqa

# django-debug-toolbar middleware should be high on the list of middleware
# (but after anything that encodes the response content such as GZipMiddleware)
MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE  # noqa

# needed for django-debug-toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "0g^9kov4soj^q^7_o^+orwl&%w9w%kvw@k*yczi1^+c%my5)2u"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DJANGO_DENMARK_INVITE_CODES = ["test"]
