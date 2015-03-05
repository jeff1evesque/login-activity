#!/usr/bin/python

## @jsonschema_metrics.py
#  This file contains the valid schema for the login metrics.

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
      'login_success': {
        'type': 'array',
        'minItems': 1,
        'items': {
          'type': 'string',
          'format': 'date-time',
          'minLength': 1
        },
      },
      'login_failure': {
        'type': 'array',
        'minItems': 1,
        'items': {
          'type': 'string',
          'format': 'date-time',
          'minLength': 1
        },
      },
      'logout_success': {
        'type': 'array',
        'minItems': 1,
        'items': {
          'type': 'string',
          'format': 'date-time',
          'minLength': 1
        },
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
        'type': 'string',
        'format': 'date-time',
        'minLength': 1
      },
      'login_last': {
        'type': ['string', None],
        'format': 'date-time',
        'minLength': 1
      },
    },
  }
  return schema
