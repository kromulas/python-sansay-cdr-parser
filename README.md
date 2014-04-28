# python-sansay-cdr-parser

A module for parsing Sansay VSXi SBC CDR file(s) into a list that can then be used for posting into a SQL or Document based database. Support for Sansay CDR version 1.18 is provided and is the default version passed at this time. Earlier versions and future released versions will be supported as needed. A unique ID is added as the first field to the CDR record since the session ID provided to each CDR record is not unique if pulling CDR's from multiple VSXi's.

## Installation

Install from Pypi using [pip](http://www.pip-installer.org/en/latest/), a package manager for Python.

    pip install sansaycdrparser

Don't have pip installed? Try installing it by running this from the command line:

    $ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

Or you can [download the source code (ZIP)](https://github.com/kromulas/python-sansay-cdr-parser/zipball/master "python-sansay-cdr-parser source code") for `python-sansay-cdr-parser`, and then run:

    python setup.py install

You may need to run the above commands with `sudo`.

## Usage

`sansaycdrparser`.ParseFile(file[, ver])

Where file is a Sansay VSXi produced CDR file and ver is the version of the CDR format. Refer to the Sansay VSXi documentation for understanding the variances between CDR versions.

A short usage example:

```python
import sansaycdrparser

cdr_file = "/raw_cdrs/20140318-0626-85736-85834.cdr"
records_list = sansaycdrparser.ParseFile(cdr_file)

# Do something with the list of call detail records.
```
