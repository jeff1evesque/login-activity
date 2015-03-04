#!/usr/bin/python

## @parser_data.py
#  This file parses the supplied file-object into a python dictionary.
#
#  Note: during each iteration of parsing the supplied file-object, the
#        sub-dataset is validated against an imported jsonschema, then
#        appended to an overall restructured data.
import json

## Class: Parse_Data, explicitly inherit 'new-style' class
class Parse_Data(object):

  ## constructor:
  #
  #  @self.dataset, is the dataset as either a file-object, or python dict
  #
  #  @self.dict, the indicator whether the supplied dataset is a python dict
  def __init__(self, dataset, dict=False):
    self.dataset = dataset
    self.dict    = dict

  ## restructure: iterate over json file-object, and build a dict representation
  def restructure(self):
    # load dataset into dict
    if self.dict: dataset_dict = self.dataset['hits']['hits']
    else: dataset_dict = json.loads(self.dataset.read())['hits']['hits']

    # close file, and return restructured dataset
    self.dataset.close()
    return dataset_dict

  ## user_metrics: generate a list of users, and their corresponding login
  #                activity metrics.
  #
  #  The following user-metrics will be generated
  #
  #    - email address
  #    - date & time of the last successful log-in
  #    - date & time of the first successful log-in
  #    - count of successful log-ins
  #    - count of failed log-ins  
  #
  #  The following web-metrics will be generated
  #
  #    - the count of users that have ever logged-in (A)
  #    - the count of users that have logged-in the last 30 days (B)
  #    - the count of users that have logged-in the last 60 days (B)
  #    - the count of users that have logged-in the last 90 days (B)
  #    - the percentage of users that have logged-in the last 30 days (A/B)
  #    - the percentage of users that have logged-in the last 60 days (A/B)
  #    - the percentage of users that have logged-in the last 90 days (A/B)
  def user_metrics(self, data):
    # local variables
    unique_users = {}

    # iterate supplied data, generate metrics
    for index, item in enumerate(data):

      # base case: first time activity
      if item['_id'] not in unique_users:
        email_address = item['_id']

        if item['_source']['clientLog']['action'] == 'LoginSuccess':
          login_success = [item['_source']['timestamp']]
        elif item['_source']['clientLog']['action'] == 'LoginFailure':
          login_failure = [item['_source']['timestamp']]
        elif item['_source']['clientLog']['action'] == 'Logout':
          logout_success = [item['_source']['timestamp']]

      # step case: first time activity
