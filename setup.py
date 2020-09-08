#/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup
from scb import __version__

setup(
    # name='SCB: Spider-Container-Builder',
    name='spider-cb',
    version=__version__,
    description="SCB: spider-container builder for different jdk version",
    packages=['scb',],
    license='MIT',
    long_description=open('README.md').read(),
    install_requires = [
        'jinja2==2.*',
        'docker==4.*'
    ],
    tests_require = [
        'pytest'
    ],
    entry_points = {
        'console_scripts': [
            'spider-cb=scb.scb:main'
        ]
    }
)
