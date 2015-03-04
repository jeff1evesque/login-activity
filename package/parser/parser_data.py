#!/usr/bin/python

## @parser_data.py
#  This file parses the supplied file-object into a python dictionary.
#
#  Note: during each iteration of parsing the supplied file-object, the
#        sub-dataset is validated against an imported jsonschema, then
#        appended to an overall restructured data.
import json

## Class: Parse_Data, explicitly inherit 'new-style' class
#
#  @self.fp, a json file-object, representing the supplied dataset
class Parse_Data(object):

  ## constructor:
  #
  #  @self.dataset, is the either the dataset as a file-object, or python dict
  #
  #  @self.dict, the indicator whether the supplied dataset is a python dict
  def __init__(self, dataset, dict=False):
    self.dataset = dataset
    self.dict    = dict

  ## restructure: iterate over json file-object, and build a dict representation
  def restructure(self):
    if self.dict: dataset_dict = self.dataset
    else: dataset_dict = json.loads(self.fp.read())
