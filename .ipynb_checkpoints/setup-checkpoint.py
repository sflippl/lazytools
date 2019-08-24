#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:20:33 2019

@author: sflippl
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lazytools_sflippl",
    version="0.0.0.9000.post1",
    author="Samuel Lippl",
    author_email="sfc.lippl@gmail.com",
    description="A few handy tools for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sflippl/lazytools",
    packages=setuptools.find_packages(),
    include_package_data = True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
)