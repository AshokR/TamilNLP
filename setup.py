#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (C) 2021 எழில் மொழி அறக்கட்டளை

from setuptools import setup
from codecs import open

long_description = open('README.md','r','UTF-8').read()

setup(name='TamilNLP',
      version='1.0',
      description='TamilNLP tools for Python v3',
      author='Ashok Ramachandran',
      author_email='ashokramach@gmail.com',
      long_description=long_description,
      url='https://github.com/AshokR/TamilNLP.git',
      packages=['tamilnlp'],
      package_dir={'tamilnlp': 'tamilnlp/'},
      package_data={'tamilnlp': ['Resources/*.*','Resources/ParallelText/','Resources/unmunch/']},
      license='APACHE',
      install_requires=[
          'nltk>=3.4.5',
          'tamil>=0.98',
          'wikiapi',
          'requests>=2.23.0'
      ],
      platforms='PC,Linux,Mac',
      classifiers=['Natural Language :: Tamil',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8'],
     download_url='https://github.com/AshokR/TamilNLP/archive/master.zip',
      )
