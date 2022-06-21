#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="unit-test-for-data-science",
      version="0.1.0",
      packages=find_packages("src"),
      package_dir={"": "src"},
      install_requires=[
                        "matplotlib==3.1.1",
                        "numpy==1.22.0",
                        "pytest==5.2.2",
                        "pytest-mpl==0.10",
                        "pytest-mock==1.11.2",
                        "scipy==1.3.1",
                        ],
      )
