from __future__ import with_statement
from setuptools import setup

# To install python-sansay-cdr-parser Module, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed. Try reading the setuptools
# documentation: http://pypi.python.org/pypi/setuptools

setup (
    name = "sansaycdrparser",
    version = "0.0.2",
    description = "Quick Sansay SBC CDR file parser that returns a list of records",
    author = "Ken Ryon",
    author_email = "ken.ryon@shift8networks.net",
    url = "https://github.com/kromulas/python-sansay-cdr-parser",
    keywords = ["sansay","cdr","parser"],
    py_modules = ["sansaycdrparser"],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
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
