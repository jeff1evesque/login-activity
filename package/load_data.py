#!/usr/bin/python

## @load_data.py
#  This file delegates parser, validator, report generator logic, and
#      returns the correspond login-activity report.
import os
from settings import LOG_ACTIVITY
from package.parser.parser_data import Parse_Data
from package.validator.validator_data import Validate_Data
from package.generator.generator_data import Generate_Data

## process_report:
def process_report():
  with open(LOG_ACTIVITY)) as fp:

    # parse data

    # validate data

    # generate report

    # return report
    return report
