django-denmark.org
==================

Local development bootstrapping:

#. ``pip install -r requirements.txt``
#. Edit ``djangodenmark/settings/local.py`` to specify at least ``from .dev import *``.
#. Run ``python manage.py migrate``.
   * If you don't have Postgis, run it and then accept that it fails when migrating ``map`` and then get the remaining apps migrated running ``python manage.py migrate <app-label>``.

To get the ``map`` application working, you need
`Postgis <https://postgis.net>`__ installed.

In order to get Postgres running on your system, consider reading this
`Django Girls tutorial <https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation/index.html>`__
