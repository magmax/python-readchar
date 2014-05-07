# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from readchar import __version__


def read_description():
    with open('README.rst') as fd:
        return fd.read()


setup(name='readchar',
      version=__version__,
      description="Utilities to read single characters and key-strokes",
      long_description=read_description(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Topic :: Software Development',
          'Topic :: Software Development :: User Interfaces',
      ],
      keywords='stdin,command line',
      author='Miguel Ángel García',
      author_email='miguelangel.garcia@gmail.com',
      url='https://github.com/magmax/python-readchar',
      license='MIT',
      packages=find_packages(exclude=['tests', 'venv']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        ],
      )
