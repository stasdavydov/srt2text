from distutils.core import setup

from setuptools import find_packages

setup(name='srt2text',
      version='1.0',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'click',
          'pysrt',
      ],
      entry_points={
          'console_scripts': [
              'srt2text = srt2text.group:main',
          ]
      },
      )
