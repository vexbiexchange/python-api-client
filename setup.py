import setuptools

try:
  long_description = open('README.txt').read()
except(IOError, ImportError):
  long_description = open('README.md').read()

setuptools.setup(
  name='vexbi-python-api-client',
  version='0.0.1',
  description='Python API Client library for Vexbi.com',
  long_description=long_description,
  url='http://bitbucket.org/volabit/vexbi-python-api-client',
  download_url='https://github.com/Mifiel/python-api-client/tarball/v0.0.6',
  author='Jaime Victoria',
  author_email='jaime@michelada.io',
  license='MIT',
  test_suite='nose2.collector.collector',
  packages=setuptools.find_packages()
)
