
from setuptools import setup
import sys

setup(
  name = 'memcached-utils',
  packages = ['memcached-utils'], 
  version = '0.1.0',
  description = 'Python utility to get / set (read/write) values from memcached',
  author = 'ipapi',
  license="MIT License",
  author_email = 'pweb@ipapi.co',
  url = 'https://github.com/ipapi-co/memcached-utils', 
  download_url = 'https://github.com/ipapi-co/memcached-utils/archive/0.1.0.tar.gz',
  keywords = ['memcached', 'memcached-utils', 'python-memcached', 'memcached-reader', 'memcached-writer'], 
  classifiers = [],
  install_requires = 'python-memcached',
)
