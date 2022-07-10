TYPE_JSON = '.json'
TYPE_YML_OR_YAML = ('.yml', '.yaml')
UNSUPPORTED_TYPE = '''Extension "{}" is not supported.
Use JSON or YML/YAML format'''

FORMAT_STYLISH = 'stylish'
FORMAT_PLAIN = 'plain'
FORMAT_JSON = 'json'
FILEREAD_ERR = '''Failed to open file '{}'.
Please, check that the file path is entered correctly.'''
INVALID_FILE = '''This file is not valid.
Please, make sure the file is filled in correctly.'''
UNSUPPORTED_FORMAT = '''Format is not supported.
Use STYLISH, PLAIN or JSON format'''
DEFAULT_FORMAT = FORMAT_STYLISH
FORMATS = (FORMAT_STYLISH, FORMAT_JSON, FORMAT_PLAIN)

ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
NESTED = 'nested'
CHILD = 'child'

DIFFLINE_TEMPLATE_STYLISH = '{}  {} {}: {}'
ENDLINE_TEMPLATE_STYLISH = '{}    {}'
NESTING_INDENTATION = 4

ADDED_TEMPLATE_PLAIN = "Property '{}' was added with value: {}"
REMOVED_TEMPLATE_PLAIN = "Property '{}' was removed"
UPDATED_TEMPLATE_PLAIN = "Property '{}' was updated. From {} to {}"
COMPLEX_VALUE = "[complex value]"
