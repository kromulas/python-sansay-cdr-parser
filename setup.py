from __future__ import with_statement
from setuptools import setup, find_packages

__version__ = None
with open('sansaycdr/version.py') as f:
    exec(f.read())

# To install python-sansay-cdr-parser Module, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed. Try reading the setuptools
# documentation: http://pypi.python.org/pypi/setuptools

setup (
    name = "sansaycdr",
    version = __version__,
    description = "Quick Sansay SBC CDR file parser that returns a list of records"
    author = "Ken Ryon"
    author_email = "ken.ryon@shift8networks.net"
    url = "https://github.com/kromulas/python-sansay-cdr-parser"
    keywords = ["sansay","cdr","parser"],
    packages = find_packages(),
    include_package_data=True,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Pythin :: 3.3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
        ],
    long_description = """\
    Sansay SBC CDR File Parser Module
    ---------------------------------

    USAGE
        records_list = sansaycdrparser.ParseFile(file, ver)
    Where file is the name of a Sansay SBC CDR file and ver is the version of the Sansay SBC CDR file format.
    Current support for version 1.18 is provided and is the default passed at this time.
    Earlier versions and newly released versions will be updated as needed.

    LICENSE This helper module is distributed under the MIT License """ )
