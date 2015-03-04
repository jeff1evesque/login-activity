#!/usr/bin/python

## @parser_data.py
#  This file parses the supplied file-object into a python dictionary.
#
#  Note: during each iteration of parsing the supplied file-object, the
#        sub-dataset is validated against an imported jsonschema, then
#        appended to an overall restructured data.
import json
from datetime import datetime, timedelta

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

    list_days30  = []
    list_days60  = []
    list_days90  = []

    datetime_back30 = datetime.now() - timedelta(days=30)
    datetime_back60 = datetime.now() - timedelta(days=60)
    datetime_back90 = datetime.now() - timedelta(days=90)

    # iterate supplied data, generate metrics
    for index, item in enumerate(data):
      login_success     = []
      login_failure     = []
      logout_success    = []

      back30days = False
      back60days = False
      back90day  = False

      datetime_instance = datetime.strptime(item['_source']['timestamp'], '%d-%m-%Y %H:%M:%S.%f')

      # base case: first time activity
      if item['_id'] not in unique_users:
        email = item['_id']

        # record system, not client timestamp
        if item['_source']['clientLog']['action'] == 'LoginSuccess':
          login_success = [item['_source']['timestamp']]

          # determine if user has logged in the last 30, 60, 90 days
          if datetime_instance > datetime_back30:
            list_days30.append(item['_id'])
            back30days = True
          if datetime_instance > datetime_back60:
            list_days60.append(item['_id'])
            back60days = True
          if datetime_instance > datetime_back90:
            back90days = True
            list_days90.append(item['_id'])

        elif item['_source']['clientLog']['action'] == 'LoginFailure':
          login_failure = [item['_source']['timestamp']]
        elif item['_source']['clientLog']['action'] == 'Logout':
          logout_success = [item['_source']['timestamp']]

        # append user
        unique_users[item['_id']] = {'email': email, 'login_success': login_success, 'login_failure': login_failure, 'logout_success': logout_success, 'back30days': back30days, 'back60days': back60days, 'back90days': back90days }

        # validate with jsonschema

      # step case: successive time activity
      elif item['_id'] in unique_users:
      
        # record system, not client timestamp
        if item['_source']['clientLog']['action'] == 'LoginSuccess':
          login_success = [item['_source']['timestamp']]
          unique_users[item['_id']]['login_success'].append(login_success)

          # determine if user has logged in the last 30, 60, 90 days
          if not unique_users[item['id']]['back30days']: list_days30.append(item['_id'])
          if not unique_users[item['id']]['back60days']: list_days60.append(item['_id'])
          if not unique_users[item['id']]['back90days']: list_days90.append(item['_id'])

        elif item['_source']['clientLog']['action'] == 'LoginFailure':
          login_failure = [item['_source']['timestamp']]
          unique_users[item['_id']]['login_failure'].append(login_failure)
        elif item['_source']['clientLog']['action'] == 'Logout':
          logout_success = [item['_source']['timestamp']]
          unique_users[item['_id']]['logout_success'].append(logout_success)

        # validate with jsonschema

    # return unique users login-activity metrics
    return unique_users
