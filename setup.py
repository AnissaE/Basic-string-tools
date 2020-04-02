#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:50:34 2020

@author: clemonnier
"""
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bstools", # Replace with your own username
    version="0.0.3",
    author="Claire Lemonnier",
    author_email="claire.lemonnier@insa-lyon.fr",
    description="A small and simple module to perform simple manipulations on strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AnissaE/Software_deployement",
    packages=setuptools.find_packages(),
    license= "MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

print("packages:",setuptools.find_packages())
