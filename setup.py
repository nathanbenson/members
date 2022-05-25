#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
import versioneer
import os

with open('README.md') as readme_file:
    readme = readme_file.read()

HERE = os.path.dirname(os.path.abspath(__file__))

setup_requirements = [
    'sphinx',
    'pytest-runner',
]

test_requirements = [
    'pytest'
]


def extract_requires():
    """Get pinned requirements from requirements.txt."""
    with open(os.path.join(HERE, 'requirements/main.txt'), 'r') as reqs:
        return [line.split(' ')[0] for line in reqs if not line[0] in ('-', '#')]


setup(
    name='members',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Member and provider api/data handler",
    long_description=readme,
    author="Nathan Benson",
    author_email='nathanbenson33@gmail.com',
    url='',
    packages=find_packages(),
    include_package_data=True,
    install_requires=extract_requires(),
    zip_safe=False,
    keywords='members',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)

