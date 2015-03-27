#!/usr/bin/python

## @settings.py
#  This file contains various setting variables
#
#  Note:  __file__ refers to the current file (settings.py)
import os

APP_ROOT     = os.path.dirname(os.path.abspath(__file__))
LOG_ACTIVITY = os.path.realpath(os.path.join(APP_ROOT, 'data/large_dataset.json'))
#LOG_ACTIVITY = os.path.realpath(os.path.join(APP_ROOT, 'data/medium_dataset.json'))
#LOG_ACTIVITY = os.path.realpath(os.path.join(APP_ROOT, 'data/small_dataset.json'))
