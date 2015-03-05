#!/usr/bin/python

## @load_data.py
#  This file delegates parser, validator, report generator logic, and
#      returns the correspond login-activity report.
from settings import LOG_ACTIVITY
from package.parser.parser_data import Parse_Data
from package.generator.generator_data import Generate_Data

## process_report:
def process_report():
  try:
    with open(LOG_ACTIVITY) as fp:
      # parse data
      sent_file         = Parse_Data(fp)
      restructured_data = sent_file.restructure()
      user_metrics      = sent_file.user_metrics(restructured_data)

      # generate report
      if user_metrics['data']:
        sent_data  = Generate_Data(user_metrics['data'])
        report     = sent_data.generate_report()
        report_csv = sent_data.generate_csv()
      else:
        print user_metrics['error']
        return False

      # return report
      return report
  except Exception, error:
    print error
    return False
