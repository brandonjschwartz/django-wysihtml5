from setuptools import setup, find_packages
from setuptools.command.test import test
import os
import sys


def setup_django_settings():
    os.chdir(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, os.getcwd())
    os.environ["DJANGO_SETTINGS_MODULE"] = "wysihtml5.tests.settings"


def run_tests_pkg():
    if not os.environ.get("DJANGO_SETTINGS_MODULE", False):
        setup_django_settings()

    from django.conf import settings
    from django.test.utils import get_runner

    runner = get_runner(settings, "django.test.runner.DiscoverRunner")
    test_suite = runner(verbosity=2, interactive=True, failfast=False)
    test_suite.run_tests(["wysihtml5"])


def run_tests(*args):
    run_tests_pkg()

test.run_tests = run_tests

setup(
    name="django-wysihtml5",
    version="1.2b4",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    description="Simple Django app that provides a Wysihtml5 rich text editor textarea widget. Modified to not do nofollow on all links",
    long_description="Simple Django app that provides a Wysihtml5 rich text editor textarea widget, with a complete command toolbar to give HTML format to your documents. Modified to not do nofollow on all links",
    author="Daniel Rus Morales",
    author_email="inbox@danir.us",
    maintainer="Daniel Rus Morales",
    maintainer_email="inbox@danir.us",
    contributor="Brandon J. Schwartz",
    contributor_email="brandon@boomajoom.com",
    url="https://github.com/brandonjschwartz/django-wysihtml5",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
    test_suite="dummy",
)
