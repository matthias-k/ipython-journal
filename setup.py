# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='ipython-journal',
      version=version,
      description="IPython Journal",
      long_description=""" """,
      install_requires=["matplotlib",
                        ],
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Matthias Kümmerer',
      author_email='matthias@matthias-k.org',
      url='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
#      package_data={'':'LICENSE'},
      include_package_data=True,
      zip_safe=True,
      entry_points="""
      # -*- Entry points: -*-
      """,
      use_2to3 = True,
      )
