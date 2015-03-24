#!/usr/bin/python

## @validator_data.py
#  This file performs various validations on login data.
from jsonschema.validators import Draft4Validator
from package.schema.jsonschema_metrics import jsonschema_metrics, jsonschema_timestamp

## Class: Validate_Data, explicitly inherit 'new-style' class
class Validate_Data(object):

  ## constructor:
  def __init__(self, data):
    self.data        = data
    self.list_errors = []

  ## validate_data: validate user metric sub-dataset
  def validate_data(self):
    try:
      Draft4Validator(jsonschema_metrics()).validate(self.data)
      return True
    except Exception, error:
      self.list_errors.append(error)
      return False

  ## validate_timestamp: validate login timestamps
  def validate_timestamp(self):
    try:
      Draft4Validator(jsonschema_timestamp()).validate(self.data)
      return True
    except Exception, error:
      self.list_errors.append(error)
      return False

  ## get_errors: returns appended errors
  def get_errors(self):
    return self.list_errors
