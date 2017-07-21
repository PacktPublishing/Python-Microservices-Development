from setuptools import setup, find_packages
from dataservice import __version__


setup(name='runnerly-data',
      version=__version__,
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False)
