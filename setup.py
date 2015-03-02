# -*- coding: utf-8 -*-
"""Setup file for easy installation"""
from os.path import join, dirname
from setuptools import setup


LONG_DESCRIPTION = """
"""


def long_description():
    """Return long description from README.rst if it's present
    because it doesn't get installed."""
    try:
        return open(join(dirname(__file__), 'README.rst')).read()
    except IOError:
        return LONG_DESCRIPTION


setup(name='django-whitelist',
      version='',
      author='Martin Prunell',
      author_email='martin.prunell@gmail.com',
      description='Whitelist access to protected resources',
      license='BSD',
      keywords='django',
      url='https://github.com/martinprunell/django-whitelist',
      packages=[],
      long_description=long_description(),
      install_requires=[],
      classifiers=[],
      tests_require=[],
      test_suite='',
      zip_safe=False)