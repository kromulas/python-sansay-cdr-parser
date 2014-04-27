"""sansaycdrparser.py: Quick Sansay SBC CDR file parser that returns a list of records.

Usage.

Parsing a CDR file:
	records_list = sansaycdrparser.ParseFile(file, ver)
where file is the name of a Sansay SBC CDR file and ver is the version of the Sansay SBC CDR file format.
Current support for version 1.18 is provided and is the default passed at this time. Earlier versions and
newly released versions will be updated as needed.

"""

import datetime, csv
from os.path import isfile
from uuid import uuid4

__version__ = "$Rev: 0.0.2 $"
# exception classes
class Error(Exception):
    """Exception class for this module. Use:

    except xdrlib.Error, var:
        # var has the Error instance for the exception

    Public ivars:
        msg -- contains the message

    """
    def __init__(self, msg=''):
        self.message = msg
        Exception.__init__(self, msg)

    def __repr__(self):
        return self.message

    __str__ = __repr__

class CdrFileError(Error):
	"""Exception raised if the CDR file cannot be located on the system."""
	def __init__(self, cdr_file):
		Error.__init__(self, 'File not found: %r' % (cdr_file, ))
		self.cdr_file = cdr_file
		self.args = (cdr_file, )

class CdrFileFormatError(Error):
	"""Exception raised if the CDR file provided is not the proper format."""
	def __init__(self, cdr_file):
		Error.__init__(self, '%r does not appear to be a CSV file.' % (cdr_file, ))
		self.cdr_file = cdr_file
		self.args = (cdr_file, )


def ParseFile(cdr_file, ver = "1.18"):
	if not isfile(cdr_file):
		raise CdrFileError(cdr_file)
		
	with open(cdr_file, 'rt') as f:
		try:
			dialect = csv.Sniffer().sniff(f.readline(), delimiters=';')
			f.seek(0)
		except csv.Error:
			raise CdrFileFormatError(cdr_file)

		records = list(csv.reader(f, dialect))
		"""CDR version control to support different file formats."""
		if ver == '1.18':
			"""Remove the 18 character padded new line at the end of the raw CDR file"""
			records.pop()
			for line in records:
				"""Add a unique id to each CDR record since the provided session id is not unique if pulling CDR's across multiple Sansay SBC's"""
				record_id = uuid4().hex
				line.insert(0, record_id)
				"""Each record ends with the delimeter before the newline creating a null field in the list - so it's removed."""
				line.pop()
				"""Set the timestamps entries to a standard datetime format for posting to an SQL or Document based DB."""
				d = datetime.datetime.strptime(line[7], '%c')
				line[7] = d.strftime('%Y-%m-%d %H:%M:%S')
				if line[8] != 'NA':
					d = datetime.datetime.strptime(line[8], '%c')
					line[8] = d.strftime('%Y-%m-%d %H:%M:%S')
				d = datetime.datetime.strptime(line[9], '%c')
				line[9] = d.strftime('%Y-%m-%d %H:%M:%S')

	return records
