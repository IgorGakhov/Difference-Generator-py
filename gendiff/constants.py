TYPE_JSON = '.json'
TYPE_YML_OR_YAML = ('.yml', '.yaml')
UNSUPPORTED_TYPE = '''Extension "{}" is not supported.
Use JSON or YML/YAML format'''

FORMAT_STYLISH = 'stylish'
FORMAT_JSON = 'json'
FORMAT_PLAIN = 'plain'
UNSUPPORTED_FORMAT = '''Format is not supported.
Use STYLISH, PLAIN or JSON format'''
DEFAULT_FORMAT = FORMAT_STYLISH
FORMATS = (FORMAT_STYLISH, FORMAT_JSON, FORMAT_PLAIN, DEFAULT_FORMAT)

ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
NESTED = 'nested'

DIFFLINE_TEMPLATE_STYLISH = '{}  {} {}: {}'
ENDLINE_TEMPLATE_STYLISH = '{}    {}'
NESTING_INDENTATION = 4
