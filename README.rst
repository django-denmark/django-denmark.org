django-denmark.org
==================

Local development bootstrapping:

#. ``pip install -r requirements.txt``
#. Run ``python manage.py migrate``.
   * If you don't have Postgis, run it and then accept that it fails when migrating ``map`` and then get the remaining apps migrated running ``python manage.py migrate <app-label>``.
#. Run ``python manage.py runserver``.
#. Run ``python manage.py runserver`` again if this was the first time. In the future, you can add local settings to ``djangodenmark/settings/local.py``.

In order to contribute, please create a Pull Request and we will get back 💖
