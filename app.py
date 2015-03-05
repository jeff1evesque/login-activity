## @app.py
#  This file loads corresponding logic, and html template file(s), which
#      allows the presentation of (asynchronous) content.
import json
from flask import Flask, render_template, request
from package.load_data import process_report

# Initialize: create flask instance
app = Flask(__name__)

# Define Route: assign corresponding template, or logic to given path
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/generate-report/', methods=['POST', 'GET'])
def generate_report():
  if request.method == 'POST':
    # process, and return report
    report = process_report()
    return render_template('activity_report.html', data=map(json.dumps, report))

# Execute: run application directly, instead of import
if __name__ == '__main__':
  app.run(
  debug=True
)
