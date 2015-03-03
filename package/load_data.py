#!/usr/bin/python

## @load_data.py
#  This file delegates parser, validator, report generator logic, and
#      returns the correspond login-activity report.
from settings import APP_ROOT

## Class: Load_Data, explicitly inherit 'new-style' class
class Load_Data(object):

  ## constructor:
  def __init__(self):
