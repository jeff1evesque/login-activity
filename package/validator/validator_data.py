#!/usr/bin/python

## @validator_data.py
#  This file performs various validations on login data.

## Class: Validate_Data, explicitly inherit 'new-style' class
class Validate_Data(object):

  ## constructor:
  def __init__(self, data):
    self.data        = data
    self.list_errors = []

  ## validate_data: validate user metric sub-dataset
  def validate_data(self):
    try:
      validate(self.data, jsonschema_metric())
      return True
    except Exception, error
      return False

  ## get_errors: returns appended errors
  def get_errors(self):
    return self.list_errors
