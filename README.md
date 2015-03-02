Login Activity
================

### Overview

This project is a proof of concept, used to generate a report of login activities. Using a provided json file, typically stored in the [`/data/`](https://github.com/jeff1evesque/login-activity/blob/master/data/) subdirectory, a login-activity report is generated as a webpage.

Specifically, the web log-activity report will contain the following metrics:

- A: the count of users that have ever logged-in
- B: the count, of users that have logged-in the last 30 days
- B: the count, of users that have logged-in the last 60 days
- B: the count, of users that have logged-in the last 90 days
- C: the percentage of users that have logged-in the last 30 days (A/B)
- C: the percentage of users that have logged-in the last 60 days (A/B)
- C: the percentage of users that have logged-in the last 90 days (A/B)

In addition to the web log-activity report, a downloadable csv link will be provided.  Specifically, each row in the csv will correspond to a user within the system, and will contain the following metrics:

- email address
- date & time of the last successful log-in
- date & time of the first successful log-in
- count of successful log-ins
- count of failed log-ins

**Note:** the csv file will also contain a header row, labeling each of the above metric.

**Note:** this project may later implement the python `request.get()` method, instead of directly parsing a json-file within the web-application `/data/` subdirectory.

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

##Execution

Once `app.py` is running on a dedicated terminal window, this application can be accessed via any web-browser:

```
http://localhost:5000/
```
