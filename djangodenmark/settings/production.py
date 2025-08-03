"""
This is the shared, PUBLIC production settings.

Do NOT put secrets here.
"""
import os
from .base import *  # noqa


DEBUG = False

ALLOWED_HOSTS = ["django-denmark.org", "www.django-denmark.org"]

STATIC_ROOT = os.path.join(BASE_DIR, "static")
