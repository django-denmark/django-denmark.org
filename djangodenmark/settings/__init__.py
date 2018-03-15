try:
    from .local import *
except:
    print(
        "No settings.local module, create settings/local.py and add something "
        "like `from .dev import *`"
    )
    raise
