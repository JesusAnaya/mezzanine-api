#!/usr/bin/env python
from setuptools import setup


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
        'django-setuptest',
        'argparse'
    ),
)
