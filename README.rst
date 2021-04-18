django-denmark.org
==================

Local development bootstrapping:

#. ``pip install -r requirements_dev.txt``
#. Run ``python manage.py migrate``.
   * If you don't have Postgis, run it and then accept that it fails when migrating ``map`` and then get the remaining apps migrated running ``python manage.py migrate <app-label>``.
#. Run ``python manage.py runserver``.
#. Run ``python manage.py runserver`` again if this was the first time. In the future, you can add local settings to ``djangodenmark/settings/local.py``.

In order to contribute, please create a Pull Request and we will get back 💖


Further steps
-------------

We recommend that you use pre-commit for your development::

.. code-block:: bash

  # Install so-called git hooks for checking code when you are committing
  pre-commit install
  # Write some changes
  # ...
  git add
  # See that it runs when you commit stuff
  git commit
  # ..or try it out
  pre-commit run --all-files
