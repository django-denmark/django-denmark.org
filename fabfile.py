"""
ATTENTION!!! This file has not been tested at all!
"""
import os
from contextlib import contextmanager as _contextmanager
from fabric.api import run, env
from fabric import api
from fabric.context_managers import cd, prefix

api.env.hosts = ['djangodenmark@django-denmark']

# NB! No trailing slashes
ENV_DIR = '/var/vhosts/djangodenmark/.virtualenvs/venv'
PROJECT_DIR = '/var/vhosts/djangodenmark/git'


def dirjoin(x):
    return os.path.join(PROJECT_DIR, x)

# Use the local .ssh/config
env.use_ssh_config = True

# Define a set of SSH hosts per roledef
# afterwars, use fab --roles ROLEDEF task
env.roledefs = {
    'production': ['fair@fair'],
    # 'local': ['letsgo-vagrant']
}

env.virtualenv = ENV_DIR
env.activate = 'source %(virtualenv)s/bin/activate' % env
env.code_dir = PROJECT_DIR


@_contextmanager
def virtualenv():
    with cd(env.virtualenv), prefix(env.activate), cd(env.code_dir):
        yield


def git_pull():

    with cd(PROJECT_DIR):
        run('git pull --ff origin master')


def clean_pyc():

    with cd(PROJECT_DIR):
        run("find -name '*.pyc' -exec rm {} \\;")


def syncdb():
    with virtualenv():
        run('python manage.py syncdb')


def migrate():
    with virtualenv():
        run('python manage.py migrate')


def collectstatic():
    with virtualenv():
        run('python manage.py collectstatic --noinput')


def install():
    with virtualenv():
        run('pip install -r requirements.txt --upgrade')


def reload():
    api.run('touch /var/vhosts/djangodenmark/reload')


def deploy():
    git_pull()
    install()
    migrate()
    collectstatic()
    reload()
