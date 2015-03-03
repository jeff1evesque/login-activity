#!/usr/bin/python

## @parser_data.py
#  This file parses the supplied file-object into a python dictionary.
#
#  Note: during each iteration of parsing the supplied file-object, the
#        sub-dataset is validated against an imported jsonschema, then
#        appended to an overall restructured data.

## Class: Parse_Data, explicitly inherit 'new-style' class
class Parse_Data(object):

  ## constructor:
  def __init__(self, fp):
    self.json_fp = fp
