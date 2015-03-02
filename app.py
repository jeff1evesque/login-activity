## @app.py
#  This file loads corresponding logic, and html template file(s), which
#      allows the presentation of (asynchronous) content.
import json
from flask import Flask, render_template, request

# Initialize: create flask instance
app = Flask(__name__)

# Define Route: assign corresponding template, or logic to given path
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login_report/', methods=['POST', 'GET'])
def login_report():
  if request.method == 'POST':
  # local variables
  files = None

  # get POST data
  if request.files:
    files = request.files
  settings = request.form

  # process data
  sender = Process_Report(settings, files)
  report = sender.get_report()

  # return report
  return json.loads(report)
