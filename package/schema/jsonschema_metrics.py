#!/usr/bin/python

## @jsonschema_metrics.py
#  This file contains various required schemas used to validate components of user
#      login activity.

## jsonschema_timestamp: returns the schema used to validate login timestamps.
def jsonschema_timestamp():
  schema = {
    'type': 'object',
    'properties': {
      'timestamp': {
        'type': ['string', 'null'],
        'format': 'date-time',
        'minLength': 1
      },
    },
  }
  return schema

## jsonschema_metrics: returns the schema used to validate the login metric for
#                      each user within the provided dataset.
def jsonschema_metrics():
  schema = {
    'type': 'object',
    'properties': {
      'email': {
        'type': 'string',
        #'format': 'email',
        'minLength': 1
      },
      'login30days': {
        'enum': [True, False]
      },
      'login60days': {
        'enum': [True, False]
      },
      'login90days': {
        'enum': [True, False]
      },
      'count_success': {
        'type': 'integer',
        'minLength': 1
      },
      'count_failure': {
        'type': 'integer',
        'minLength': 1
      },
      'login_first': {
        'type': ['string', 'null'],
        'format': 'date-time',
        'minLength': 1
      },
      'login_last': {
        'type': ['string', 'null'],
        'format': 'date-time',
        'minLength': 1
      },
    },
  }
  return schema
