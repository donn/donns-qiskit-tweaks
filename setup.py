#!/usr/bin/env python3
from setuptools import setup, find_packages

from donns_qiskit_tweaks import __version__

requirements = open("requirements.txt").read().strip().split("\n")

setup(
    name="donns_qiskit_tweaks",
    packages=find_packages(),
    version=__version__,
    description="Some tweaks/useful qiskit functions",
    long_description="# Donn's Qiskit Tweaks",
    long_description_content_type="text/markdown",
    author="Mohamed Gaber",
    author_email="me@donn.website",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">3.8",
)
