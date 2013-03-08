# coding: utf-8

from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='coorder',
      version=version,
      description="Coörder unfuddles coordinate ordering",
      long_description="""\
The ordering of geospatial coordinates varies depending on the coordinate system used. Coörder is here to help!""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='gis coordinates unfuddling',
      author='Sean Gillies',
      author_email='sean.gillies@gmail.com',
      url='http://github.com/sgillies/coorder',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
