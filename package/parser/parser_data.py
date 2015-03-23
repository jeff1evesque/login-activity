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
  #  @self.dataset, the dataset as either a file-object, or python dict
  #
  #  @self.flag_dict, the indicator whether the supplied dataset is a python dict
  def __init__(self, dataset, flag_dict=False):
    self.dataset     = dataset
    self.flag_dict   = flag_dict
    self.list_errors = []

  ## restructure: iterate over supplied dataset, and build a dict representation
  def restructure(self):
    # load dataset into dict
    if self.flag_dict:
      dataset_dict = self.dataset['hits']['hits']
    else:
      dataset_dict = json.load(self.dataset)['hits']['hits']

    # return restructured dataset
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

      timestamp = item['_source']['timestamp']
      action    = item['_source']['clientLog']['action']
      email     = item['_source']['clientLog']['email']

      # convert datetime-string to datetime
      datetime_instance = datetime.strptime(timestamp, '%d-%m-%Y %H:%M:%S.%f')

      # base case: first time login (system time, not client time)
      if email not in unique_users:
        count_success = 0
        count_failure = 0
        # add successful login timestamp, increment counter
        if action == 'LoginSuccess':
          login_success = [timestamp]
          count_success = 1

          # determine if user has logged in the last 30, 60, 90 days
          if datetime_instance > datetime_back30:
            if list_days30[0] == None: list_days30.remove(None)
            list_days30.append(timestamp)
            login30days = True
          if datetime_instance > datetime_back60:
            if list_days60[0] == None: list_days60.remove(None)
            list_days60.append(timestamp)
            login60days = True
          if datetime_instance > datetime_back90:
            if list_days90[0] == None: list_days90.remove(None)
            login90days = True
            list_days90.append(timestamp)

        # add unsuccessful login timestamp, increment counter
        elif action == 'LoginFailure':
          login_failure = [timestamp]
          count_failure = 1

        # add successful logout timestamp
        elif action == 'Logout':
          logout_success = [timestamp]

        # append user
        unique_users[email] = {'email': email, 'login_success': login_success, 'login_failure': login_failure, 'logout_success': logout_success, 'login30days': login30days, 'login60days': login60days, 'login90days': login90days, 'count_success': count_success, 'count_failure': count_failure, 'login_first': login_success[0], 'login_last': None, 'list_days30': list_days30, 'list_days60': list_days60, 'list_days90': list_days90}

        # validate 'login_xxx' properties for 'unique_users', return error
        sender_timestamp  = Validate_Data(timestamp)
        validate_timstamp = sender_timestamp.validate_data()

        # validate remaining 'unique_users' properties, return error
        sender_properties   = Validate_Data(unique_users[email])
        validate_properties = sender.validate_data()

        # return error(s)
        if not validate_timestamp and not validate_properties:
          self.list_errors.append(sender_timestamp.get_errors())
          self.list_errors.append(sender_properties.get_errors())
          print self.list_errors
          return {'data': None, 'error': self.list_errors}

      # step case: successive time login (system time, not client time)
      elif email in unique_users:
      
        # add successful login timestamp, increment counter
        if action == 'LoginSuccess':
          unique_users[email]['login_success'].append(timestamp)
          unique_users[email]['count_success'] += 1

          # record first, and last time login
          datetime_instance = datetime.strptime(timestamp, '%d-%m-%Y %H:%M:%S.%f')
          datetime_first    = datetime.strptime(unique_users[email]['login_first'], '%d-%m-%Y %H:%M:%S.%f')

          if unique_users[email]['login_last'] != None:
            datetime_last = datetime.strptime(unique_users[email]['login_last'], '%d-%m-%Y %H:%M:%S.%f')
            if datetime_instance > datetime_last:
              unique_users[email]['login_last'] = timestamp
            elif datetime_instance < datetime_first:
              unique_users[email]['login_first'] = timestamp
          elif unique_users[email]['login_last'] == None:
            if datetime_instance > datetime_first:
              unique_users[email]['login_last'] = timestamp
            else:
              unique_users[email]['login_last'] = unique_users[email]['login_first']
              unique_users[email]['login_first'] = timestamp

          # determine if user has logged in the last 30, 60, 90 days
          if not unique_users[email]['login60days']:
            if len(unique_users[email]['list_days30']) == 1 and unique_users[email]['list_days30'][0] == None: unique_users[email]['list_days30'].remove(None)
            list_days30.append(timestamp)
          if not unique_users[email]['login60days']:
            if len(unique_users[email]['list_days60']) == 1 and unique_users[email]['list_days60'][0] == None: unique_users[email]['list_days60'].remove(None)
            list_days60.append(timestamp)
          if not unique_users[email]['login90days']:
            if len(unique_users[email]['list_days90']) == 1 and unique_users[email]['list_days90'][0] == None: unique_users[email]['list_days90'].remove(None)
            list_days90.append(timestamp)

        # add unsuccessful login timestamp, increment counter
        elif action == 'LoginFailure':
          if len(unique_users[email]['login_failure']) == 1 and unique_users[email]['login_failure'][0] == None: unique_users[email]['login_failure'].remove(None)
          login_failure_item = timestamp
          unique_users[email]['login_failure'].append(login_failure_item)
          unique_users[email]['count_failure'] += 1

        # add successful logout timestamp
        elif action == 'Logout':
          logout_success_item = timestamp
          unique_users[email]['logout_success'].append(logout_success_item)

        # validate 'login_xxx' properties for 'unique_users', return error
        sender_timestamp  = Validate_Data(timestamp)
        validate_timstamp = sender_timestamp.validate_data()

        # validate remaining 'unique_users' properties, return error
        sender_properties   = Validate_Data(unique_users[email])
        validate_properties = sender.validate_data()

        # return error(s)
        if not validate_timestamp and not validate_properties:
          self.list_errors.append(sender_timestamp.get_errors())
          self.list_errors.append(sender_properties.get_errors())
          print self.list_errors
          return {'data': None, 'error': self.list_errors}

    # return unique users login-activity metrics
    return {'data': unique_users, 'error': None}
