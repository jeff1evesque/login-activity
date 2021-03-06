#!/usr/bin/python

## @generator_data.py
#  This file generates a report of user login-activity using the supplied
#      dataset.
import os
import csv, json
from settings import APP_ROOT

## Class: Generate_Data, explicitly inherit 'new-style' class
class Generate_Data(object):

  ## constructor:
  def __init__(self, user_metrics):
    self.user_metrics = user_metrics

  ## generate_report: generate the login-activity report displayed on a webpage.
  #
  #  The following web-metrics will be generated:
  #
  #      - A: the count of users that have ever logged-in
  #      - B: the count, each, of users that have logged-in the last 30, 60, 90
  #            days (three distinct metrics)
  #      - C: the %, each, of users that have logged-in the last 30, 60, 90 days
  #            (calculated as B over A, as three distinct metrics)
  def generate_report(self):
    # local variables
    count_30 = 0
    count_60 = 0
    count_90 = 0

    # count of users that have logged in
    count_user = len(self.user_metrics)

    # login count for users in the last 30, 60, 90 days
    for item in self.user_metrics:
      if self.user_metrics[item]['login30days']: count_30 += 1
      if self.user_metrics[item]['login60days']: count_60 += 1
      if self.user_metrics[item]['login90days']: count_90 += 1

    # percentage of users that have logged-in the last 30, 60, 90 days
    percentage_30 = float(count_30) / float(count_user)
    percentage_60 = float(count_60) / float(count_user)
    percentage_90 = float(count_90) / float(count_user)

    # return web-metrics
    return {'total_count': count_user, 'total_30': count_30, 'total_60': count_60, 'total_90': count_90, 'percentage_30': percentage_30, 'percentage_60': percentage_60, 'percentage_90': percentage_90}

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
    # create csv directory
    try:
      path = APP_ROOT + '/static/csv/'
      os.makedirs(path)
    except OSError:
      if not os.path.isdir(path):
        raise

    # create file
    try:
      with open(path + 'login_activity.csv', 'w') as csvfile:
        # create csv object
        csv_report = csv.writer(csvfile)

        # write csv header row
        csv_report.writerow(['email', 'login-last', 'login-first', 'count-success', 'count-failure'])

        # write remaining rows
        for item in self.user_metrics:
          column = self.user_metrics[item]
          csv_report.writerow([column['email'], column['login_last'], column['login_first'], column['count_success'], column['count_failure']])

      return True

    except Exception, error:
      print error
      return False
