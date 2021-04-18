django-denmark.org
==================

Local development bootstrapping:

.. code-block:: bash

  # Create a Python3 virtual environment with your favorite tool
  python3 -m venv venv
  # Install the Python requirements for development
  pip install -r requirements_dev.txt
  # Create a database
  python manage.py migrate
  # Start the development web server
  # (you will be prompted start it again if it's the first time)
  python manage.py runserver

After this, you can open a browser on http://localhost:8000

In order to contribute, please create a Pull Request and we will get back 💖

Returning to a development environment
--------------------------------------

When you return to a development environment, you should consider the following:

* Activate your previous virtual environment, for instance: ``source venv/bin/activate``
* Install dependencies in case there are new ones: ``pip install -r requirements_dev.txt``
* Migrate the database, it might have changed: ``python manage.py migrate``


Further steps
-------------

We recommend that you use pre-commit for your development:

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
