Login Activity
================

### Overview

This project is a proof of concept, used to generate a report of login activities. Using a provided json file, typically stored in the [`/data/`](https://github.com/jeff1evesque/login-activity/blob/master/data/) subdirectory, a login-activity report is generated as a webpage.

**Metrics:** Web Report

- A: the count of users that have ever logged-in
- B: the count, each, of users that have logged-in the last 30, 60, 90 days (three distinct metrics)
- C: the %, each, of users that have logged-in the last 30, 60, 90 days (calculated as B over A, as three distinct metrics)

In addition to the web log-activity report, a downloadable csv link will be provided in the `/static/csv/` directory.  Each row in the file, corresponds to a user within the system.

**Metrics:** CSV Report

- email address
- date & time of the last successful log-in
- date & time of the first successful log-in
- count of successful log-ins
- count of failed log-ins

**Note:** the csv file will also contain a header row, labeling each of the above metric.

**Note:** this project may later implement the python [`requests.get()`](http://docs.python-requests.org/en/latest/user/quickstart/#json-response-content) method, instead of directly parsing a json-file within the web-application [`/data/`](https://github.com/jeff1evesque/login-activity/blob/master/data/) subdirectory.

## Installation

###Linux Packages

The following packages are needed to be installed:

```
# General Packages:
sudo apt-get install python-pip
sudo pip install Flask
sudo pip install requests
sudo pip install jsonschema
```

**Note:** This project assumes [Ubuntu Server 14.04](http://www.ubuntu.com/download/server) as the operating system. If another system is preferred, simply download the above requirements, with respect to the systems *package manager* equivalent.

## Configuration

###GIT

Fork this project in your GitHub account, then clone your repository:

```
cd /var/www/html/
sudo git clone https://[YOUR-USERNAME]@github.com/[YOUR-USERNAME]/login-activity.git
```

Then, change the *file permissions* for the entire project by issuing the command:

```
cd /var/www/html/
sudo chown -R jeffrey:www-data login-activity
```

**Note:** change 'jeffrey' to the user account YOU use.

Then, add the *Remote Upstream*, this way we can pull any merged pull-requests:

```
cd /var/www/html/login-activty/
git remote add upstream https://github.com/[YOUR-USERNAME]/login-activity.git
```

###Flask

Python's [Flask](http://flask.pocoo.org/), is a microframework based on [Werkzeug](http://werkzeug.pocoo.org/).  Specifically, it is a [web framework](http://en.wikipedia.org/wiki/Web_application_framework), which includes, a development server, integrated support for [unit testing](http://en.wikipedia.org/wiki/Unit_testing), [RESTful](http://en.wikipedia.org/wiki/Representational_state_transfer) API, and [Jinja2](http://jinja.pocoo.org/) templating.

This project implements flask, by requiring [`app.py`](https://github.com/jeff1evesque/login-activity/blob/master/app.py) to be running:

```
cd /var/www/html/login-activity/
python app.py
```

**Note:** the [`run()`](http://flask.pocoo.org/docs/0.10/api/#flask.Flask.run) method within `app.py`, runs the local developement server, and has the ability of defining the host, port, debug feature, and several other options. If none of these attributes are passed into the method, the server will default to running `localhost` on port `5000`, with no [`debug`](http://flask.pocoo.org/docs/0.10/quickstart/#debug-mode) features enabled.

**Note:** when running the above `app.py`, ensure that the terminal window is not used for any other processes, while the web application is available to others.

###JSON Schema

[JSON Schema](https://pypi.python.org/pypi/jsonschema) provides an implementation to validate [JSON](http://en.wikipedia.org/wiki/JSON) data structures. When a specific element within the JSON structure fails validation, an [exception](https://wiki.python.org/moin/HandlingExceptions) is raised indicating the corresponding *error message*.

Additional documentation:

- [Understanding JSON Schema](http://spacetelescope.github.io/understanding-json-schema/)
- [jsonschema](http://python-jsonschema.readthedocs.org/en/latest/)

This project implements *JSON Schema* validation, as a backend-validation tool. Specifically, [`jsonschema_metrics.py`](https://github.com/jeff1evesque/login-activity/blob/master/package/schema/jsonschema_metrics.py) defines acceptable *schemas* to validate against, while [`validator_data.py`](https://github.com/jeff1evesque/login-activity/blob/master/package/validator/validator_data.py) implements the validation schema(s).

###Dataset

This project requires a structured JSON file (user-activity dataset), to be stored relative to the project directory.  Specifically, [`settings.py`](https://github.com/jeff1evesque/login-activity/blob/master/settings.py#L10) contains the file path to this json file, in the `LOG_ACTIVITY` constant.

**Note:** [`load_data.py`](https://github.com/jeff1evesque/login-activity/blob/master/package/load_data.py#L13) implements the `LOG_ACTIVITY` constant, in order to open the json file as a file-object, which allows the file to be parsed, and the user-activity report to be generated, respectively.

##Execution

Once `app.py` is running on a dedicated terminal window, this application can be accessed via any web-browser:

```
http://localhost:5000/
```
