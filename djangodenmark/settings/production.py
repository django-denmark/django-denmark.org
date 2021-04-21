"""
This is the shared, PUBLIC production settings.

Do NOT put secrets here.
"""
from .base import *  # noqa
from .base import BASE_DIR  # noqa


DEBUG = False

ALLOWED_HOSTS = ["django-denmark.org", "www.django-denmark.org"]

STATIC_ROOT = str(BASE_DIR / "static")
