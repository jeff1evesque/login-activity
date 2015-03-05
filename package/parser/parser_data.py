#!/usr/bin/python

## @parser_data.py
#  This file parses the supplied file-object into a python dictionary.
#
#  Note: during each iteration of parsing the supplied file-object, the
#        sub-dataset is validated against an imported jsonschema, then
#        appended to an overall restructured data.
import json
from datetime import datetime, timedelta
from package.validator.validator_data import Validate_Data

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

  ## user_metrics: generate a dict of users, and their corresponding login
  #                activity metrics.
  def user_metrics(self, data):
    # local variables
    unique_users = {}

    list_days30  = [None]
    list_days60  = [None]
    list_days90  = [None]

    datetime_back30 = datetime.now() - timedelta(days=30)
    datetime_back60 = datetime.now() - timedelta(days=60)
    datetime_back90 = datetime.now() - timedelta(days=90)

    # iterate supplied data, generate metrics
    for index, item in enumerate(data):
      login_success  = [None]
      login_failure  = [None]
      logout_success = [None]

      login30days = False
      login60days = False
      login90days = False

      # convert datetime-string to datetime
      datetime_instance = datetime.strptime(item['_source']['timestamp'], '%d-%m-%Y %H:%M:%S.%f')

      # base case: first time login (system time, not client time)
      if item['_id'] not in unique_users:
        count_success = 0
        count_failure = 0
        email = item['_id']

        # add successful login timestamp, increment counter
        if item['_source']['clientLog']['action'] == 'LoginSuccess':
          login_success = [item['_source']['timestamp']]
          count_success = 1

          # determine if user has logged in the last 30, 60, 90 days
          if datetime_instance > datetime_back30:
            if list_days30[0] == None: list_days30.remove(None)
            list_days30.append(item['_source']['timestamp'])
            login30days = True
          if datetime_instance > datetime_back60:
            if list_days60[0] == None: list_days60.remove(None)
            list_days60.append(item['_source']['timestamp'])
            login60days = True
          if datetime_instance > datetime_back90:
            if list_days90[0] == None: list_days90.remove(None)
            login90days = True
            list_days90.append(item['_source']['timestamp'])

        # add unsuccessful login timestamp, increment counter
        elif item['_source']['clientLog']['action'] == 'LoginFailure':
          login_failure = [item['_source']['timestamp']]
          count_failure = 1

        # add successful logout timestamp
        elif item['_source']['clientLog']['action'] == 'Logout':
          logout_success = [item['_source']['timestamp']]

        # append user
        unique_users[item['_id']] = {'email': email, 'login_success': login_success, 'login_failure': login_failure, 'logout_success': logout_success, 'login30days': login30days, 'login60days': login60days, 'login90days': login90days, 'count_success': count_success, 'count_failure': count_failure, 'login_first': login_success[0], 'login_last': None}

        # validate with jsonschema, return error
        sender   = Validate_Data(unique_users[item['_id']])
        validate = sender.validate_data()

        if not validate:
          error_validation = sender.get_errors()
          print error_validation
          return {'data': None, 'error': error_validation}

      # step case: successive time login (system time, not client time)
      elif item['_id'] in unique_users:
      
        # add successful login timestamp, increment counter
        if item['_source']['clientLog']['action'] == 'LoginSuccess':
          login_success_item = item['_source']['timestamp']
          unique_users[item['_id']]['login_success'].append(login_success_item)
          unique_users[item['_id']]['success'] += 1

          # record first, and last time login
          if unique_users[item['_id']]['last_login'] == None and login_success_item > unique_users[item['_id']]['first_login']: unique[item['_id']]['last_login'] = login_success_item
          elif login_success_item > unique_users[item['_id']]['last_login']: unique_users[item['_id']]['last_login'] = login_success_item
          elif login_success_item < unique_users[item['_id']]['first_login']: unique_users[item['_id']]['login'] = login_success_item

          # determine if user has logged in the last 30, 60, 90 days
          if not unique_users[item['_id']]['login30days']:
            if len(unique_users[item['_id']]['login30days']) == 1 and unique_users[item['_id']]['login30days'][0] == None: unique_users[item['_id']]['login30days'].remove(None)
            list_days30.append(item['_source']['timestamp'])
          if not unique_users[item['_id']]['login60days']:
            if len(unique_users[item['_id']]['login60days']) == 1 and unique_users[item['_id']]['login60days'][0] == None: unique_users[item['_id']]['login60days'].remove(None)
            list_days60.append(item['_source']['timestamp'])
          if not unique_users[item['_id']]['login90days']:
            if len(unique_users[item['_id']]['login90days']) == 1 and unique_users[item['_id']]['login90days'][0] == None: unique_users[item['_id']]['login90days'].remove(None)
            list_days90.append(item['_source']['timestamp'])

        # add unsuccessful login timestamp, increment counter
        elif item['_source']['clientLog']['action'] == 'LoginFailure':
          if len(unique_users[item['_id']]['login_failure']) == 1 and unique_users[item['_id']]['login_failure'][0] == None: unique_users[item['_id']]['login_failure'].remove(None)
          login_failure_item = item['_source']['timestamp']
          unique_users[item['_id']]['login_failure'].append(login_failure_item)
          unique_users[item['_id']]['failure'] += 1

        # add successful logout timestamp
        elif item['_source']['clientLog']['action'] == 'Logout':
          logout_success_item = item['_source']['timestamp']
          unique_users[item['_id']]['logout_success'].append(logout_success_item)

        # validate with jsonschema, return error
        sender   = Validate_Data(unique_users[item['_id']])
        validate = sender.validate_data()

        if not validate:
          error_validation = sender.get_errors()
          print error_validation
          return {'data': None, 'error': error_validation}

    # return unique users login-activity metrics
    return {'data': unique_users, 'error': None}
