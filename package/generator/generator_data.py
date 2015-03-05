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
  #
  #  The following web-metrics will be generated:
  #
  #      - the count of users that have ever logged-in (A)
  #      - the count, each, of users that have logged-in the last 30 days (B)
  #      - the count, each, of users that have logged-in the last 60 days (B)
  #      - the count, each  of users that have logged-in the last 90 days (B)
  #      - the percentage, each, of users that have logged-in the last 30 days (A/B)
  #      - the percentage, each, of users that have logged-in the last 60 days (A/B)
  #      - the percentage, each, of users that have logged-in the last 90 days (A/B)
  def generate_report(self):
    # count of users that have logged in
    count_user = len(self.user_metrics)

  ## generate_csv: generate the login-activity report contained within a csv.
  #
  #  The following user-metrics will be generated
  #
  #    - email address
  #    - date & time of the last successful log-in
  #    - date & time of the first successful log-in
  #    - count of successful log-ins
  #    - count of failed log-ins
  #
  #  Note: the csv will have a header row with each column title
  def generate_csv(self):
    pass
