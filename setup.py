# coding=utf-8
import sys
from setuptools import setup, find_packages

NAME = 'plotnow'
VERSION = '0.1.0'

def read(filename):
    import os
    BASE_DIR = os.path.dirname(__file__)
    filename = os.path.join(BASE_DIR, filename)
    with open(filename, 'r') as fi:
        return fi.read()

def readlist(filename):
    rows = read(filename).split("\n")
    rows = [x.strip() for x in rows if x.strip()]
    return list(rows)

# if we are running on python 3, enable 2to3 and
# let it use the custom fixers from the custom_fixers
# package.
extra = {}
if sys.version_info >= (3, 0):
    extra.update(
        use_2to3=True,
    )

setup(
    name = NAME,
    version = VERSION,
    description = ('A terminal application which plot 2D data and generate '
                   'a graph.'),
    long_description = read('README.rst'),
    classifiers = (
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ),
    keywords = 'matplotlib numpy scipy plot graph',
    author = 'Alisue',
    author_email = 'lambdalisue@hashnote.net',
    url = 'https://github.com/lambdalisue/%s' % NAME,
    download_url = 'https://github.com/lambdalisue/%s/tarball/master' % NAME,
    license = 'MIT',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data = True,
    package_data = {
        '': ['LICENSE', 'README.rst',
             'requirements.txt'],
    },
    zip_safe=True,
    install_requires=readlist('requirements.txt'),
    #test_suite='runtests.runtests',
    #tests_require=readlist('requirements-test.txt'),
    entry_points={
        'console_scripts': [
            'plotnow = plotnow.console:main',
        ],
    },
    **extra
)
