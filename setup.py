from distutils.core import setup
from setuptools import find_packages
setup(name='fibonacci',
      version='1.0',
      package_dir={'fibonacci': 'fibonacci'}, #optional
      packages=['fibonacci'],
      scripts=['bin/main']
      )

