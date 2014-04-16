from distutils.core import setup

from sheetmusic import __version__

setup(name='sheetmusic',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Functions to be loaded by the Gnumeric Sheetmusic plugin',
      url='https://github.com/tlevine/sheetmusic',
      packages=['sheetmusic'],
      install_requires = [],
      tests_require = ['nose'],
      version=__version__,
      license='AGPL',
)
