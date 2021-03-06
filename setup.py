#!/usr/bin/env python3
"""Setup flask app."""
from setuptools import find_packages, setup

setup(
    name='youdownload',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'youtube_dl',
    ],
)
