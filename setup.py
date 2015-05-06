#!/usr/bin/env python

from setuptools import setup
import sys
import os


if sys.argv == ["setup.py", "test"]:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test.settings_test")
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__))+'/')


def get_requirements():
    return open('requirements.txt').read().split('\n')

setup(
    name='Mezzanine REST API',
    version='0.0.1',
    description='Dynamic REST API for Mezzanine pages',
    author='Jesus Anaya',
    author_email='jesus.anaya.dev@gmail.com',
    url='https://github.com/JesusAnaya/mezzanine-rest-api',
    packages=['mezzanine_rest'],
    license="BSD",
    zip_safe=False,
    install_requires=get_requirements(),
    test_suite='setuptest.setuptest.SetupTestSuite',
    tests_require=(
        'django==1.6',
        'django-setuptest',
        'argparse',
        'mock==1.0.1'
    ),
)
