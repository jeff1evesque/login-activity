#!/usr/bin/python

## @generator_data.py
#  This file generates a report of user login-activity using the supplied
#      dataset.

## Class: Generate_Data, explicitly inherit 'new-style' class
class Generate_Data(object):

  ## constructor:
  def __init__(self, user_metrics):
    self.user_metrics = user_metrics

  ## generate_report: generate the login-activity report displayed on a webpage.
  def generate_report(self):

  ## generate_csv: generate the login-activity report contained within a csv.
  def generate_csv(self):
