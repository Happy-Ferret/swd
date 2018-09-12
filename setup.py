# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='swd',
    version='1.0',
    py_modules=['swd'],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    entry_points={
        'console_scripts': ['swd = swd:main'],
    },
)
