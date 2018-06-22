from pymavlink.generator import mavgen
from pymavlink.generator import mavparse

import re 


def format_error_message(message):

  reObj = re.compile(r'^(ERROR):\s+',re.M);
  matches = re.findall(reObj, message);
  prefix = ("An error occurred in mavgen:" if len(matches) == 1 else "Errors occurred in mavgen:\n")
  message = re.sub(reObj, '\n', message);

  return prefix + message


def generate_headers(xml_value, lang, out_value):

  # Verify settings
  rex = re.compile(".*\\.xml$", re.IGNORECASE)

  if not xml_value:
    print('Error Generating Headers: An XML message definition file must be specified.')
    return

  if not out_value:
    print('Error Generating Headers: An output directory must be specified.')
    return

  if not lang:
    print('Error Generating Headers: No language selected.')

  # Generate headers
  opts = mavgen.Opts(out_value, wire_protocol=mavparse.PROTOCOL_2_0, language=lang, validate=mavgen.DEFAULT_VALIDATE, error_limit=5, strict_units=mavgen.DEFAULT_STRICT_UNITS);
  args = [xml_value]

  try:

    print opts
    print args
    mavgen.mavgen(opts, args)
    print('Successfully Generated Headers', 'Headers generated successfully.')

  except Exception as ex:

    exStr = format_error_message(str(ex));
    print('Error Generating Headers','{0!s}'.format(exStr))
    return



import sys
 
# Get the total number of args passed to the demo.py
total = len(sys.argv)
 
generate_headers(sys.argv[1], sys.argv[2], sys.argv[3])

