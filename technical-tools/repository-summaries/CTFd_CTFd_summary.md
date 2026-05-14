# CTFd/CTFd

## Repository overview

| Field | Details |
|-------|--------|
| **Source** | https://github.com/CTFd/CTFd |
| **Description** | No description provided. |
| **Topics** | `education`, `flask`, `security`, `ctf`, `ctfd` |

---

## Repository health

| Metric | Value |
|--------|-------|
| **Stars** | 6.7k |
| **Forks** | 2.7k |
| **Open issues** | 314 |
| **License** | Apache-2.0 license |
| **Last commit** | 2026-05-12T05:52:38.000Z |

---

## Language breakdown

| Language | Percentage |
|----------|-----------|
| Python | 57.8% |
| JavaScript | 19.9% |
| HTML | 15.6% |
| Vue | 4.4% |
| SCSS | 2.0% |
| Shell | 0.1% |

---

## Dependencies

### Python (pip)

- `alembic`
- `aniso8601`
- `attrs`
- `babel`
- `banal`
- `bcrypt`
- `boto3`
- `botocore`
- `cachelib`
- `certifi`
- `cffi`
- `charset-normalizer`
- `click`
- `cmarkgfm`
- `cryptography`
- `dataset`
- `flask`
- `flask-babel`
- `flask-caching`
- `flask-marshmallow`
- `flask-migrate`
- `flask-restx`
- `flask-script`
- `flask-sqlalchemy`
- `freezegun`
- `gevent`
- `greenlet`
- `gunicorn`
- `idna`
- `importlib-resources`
- `itsdangerous`
- `jinja2`
- `jmespath`
- `jsonschema`
- `jsonschema-specifications`
- `mako`
- `markupsafe`
- `marshmallow`
- `marshmallow-sqlalchemy`
- `maxminddb`
- `nh3`
- `packaging`
- `passlib`
- `pillow`
- `pycparser`
- `pydantic`
- `pymysql`
- `python-dateutil`
- `python-dotenv`
- `python-geoacumen-city`
- `pytz`
- `redis`
- `referencing`
- `requests`
- `rpds-py`
- `s3transfer`
- `six`
- `sqlalchemy`
- `sqlalchemy-utils`
- `tenacity`
- `typing-extensions`
- `urllib3`
- `werkzeug`
- `wtforms`
- `zope-event`
- `zope-interface`

---

## README contents

> The following content was extracted from the repository's README file.

#

[![CTFd MySQL CI](https://github.com/CTFd/CTFd/workflows/CTFd%20MySQL%20CI/badge.svg?branch=master)](https://github.com/CTFd/CTFd/workflows/CTFd%20MySQL%20CI/badge.svg?branch=master)
[![Linting](https://github.com/CTFd/CTFd/workflows/Linting/badge.svg?branch=master)](https://github.com/CTFd/CTFd/workflows/Linting/badge.svg?branch=master)
[![MajorLeagueCyber Discourse](https://camo.githubusercontent.com/eefe402152f62f7d68e15f8f0b19388b85dfd257c3b8682791f173d5d8aef993/68747470733a2f2f696d672e736869656c64732e696f2f646973636f757273652f7374617475733f7365727665723d6874747073253341253246253246636f6d6d756e6974792e6d616a6f726c656167756563796265722e6f7267253246)](https://community.majorleaguecyber.org/)
[![Documentation Status](https://camo.githubusercontent.com/be884a8c1218021fe747ecc148368ab3880d86e67fdd713b1c8935dd2045106a/68747470733a2f2f6170692e6e65746c6966792e636f6d2f6170692f76312f6261646765732f36643130383833612d373762622d343563312d613030332d3232636531323834313930652f6465706c6f792d737461747573)](https://docs.ctfd.io)

## What is CTFd?

CTFd is a Capture The Flag framework focusing on ease of use and customizability. It comes with everything you need to run a CTF and it's easy to customize with plugins and themes.

[![CTFd is a CTF in a can.](https://github.com/CTFd/CTFd/raw/master/CTFd/themes/core/static/img/scoreboard.png?raw=true)](https://github.com/CTFd/CTFd/blob/master/CTFd/themes/core/static/img/scoreboard.png?raw=true)

## Features

* Create your own challenges, categories, hints, and flags from the Admin Interface
  + Dynamic Scoring Challenges
  + Unlockable challenge support
  + Challenge plugin architecture to create your own custom challenges
  + Static & Regex based flags
    - Custom flag plugins
  + Unlockable hints
  + File uploads to the server or an Amazon S3-compatible backend
  + Limit challenge attempts & hide challenges
  + Automatic bruteforce protection
* Individual and Team based competitions
  + Have users play on their own or form teams to play together
* Scoreboard with automatic tie resolution
  + Hide Scores from the public
  + Freeze Scores at a specific time
* Scoregraphs comparing the top 10 teams and team progress graphs
* Markdown content management system
* SMTP + Mailgun email support
  + Email confirmation support
  + Forgot password support
* Automatic competition starting and ending
* Team management, hiding, and banning
* Customize everything using the [plugin](https://docs.ctfd.io/docs/plugins/overview) and [theme](https://docs.ctfd.io/docs/themes/overview) interfaces
* Importing and Exporting of CTF data for archival
* And a lot more...

## Install

1. Install dependencies: `pip install -r requirements.txt`
   1. You can also use the `prepare.sh` script to install system dependencies using apt.
2. Modify [CTFd/config.ini](https://github.com/CTFd/CTFd/blob/master/CTFd/config.ini) to your liking.
3. Use `python serve.py` or `flask run` in a terminal to drop into debug mode.

You can use the auto-generated Docker images with the following command:

`docker run -p 8000:8000 -it ctfd/ctfd`

Or you can use Docker Compose with the following command from the source repository:

`docker compose up`

Check out the [CTFd docs](https://docs.ctfd.io/) for [deployment options](https://docs.ctfd.io/docs/deployment/installation) and the [Getting Started](https://docs.ctfd.io/tutorials/getting-started/) guide

## Live Demo

<https://demo.ctfd.io/>

## Support

To get basic support, you can join the [MajorLeagueCyber Community](https://community.majorleaguecyber.org/): [![MajorLeagueCyber Discourse](https://camo.githubusercontent.com/eefe402152f62f7d68e15f8f0b19388b85dfd257c3b8682791f173d5d8aef993/68747470733a2f2f696d672e736869656c64732e696f2f646973636f757273652f7374617475733f7365727665723d6874747073253341253246253246636f6d6d756e6974792e6d616a6f726c656167756563796265722e6f7267253246)](https://community.majorleaguecyber.org/)

If you prefer commercial support or have a special project, feel free to [contact us](https://ctfd.io/contact/).

## Managed Hosting

Looking to use CTFd but don't want to deal with managing infrastructure? Check out [the CTFd website](https://ctfd.io/) for managed CTFd deployments.

## MajorLeagueCyber

CTFd is heavily integrated with [MajorLeagueCyber](https://majorleaguecyber.org/). MajorLeagueCyber (MLC) is a CTF stats tracker that provides event scheduling, team tracking, and single sign on for events.

By registering your CTF event with MajorLeagueCyber users can automatically login, track their individual and team scores, submit writeups, and get notifications of important events.

To integrate with MajorLeagueCyber, simply register an account, create an event, and install the client ID and client secret in the relevant portion in `CTFd/config.py` or in the admin panel:

```
OAUTH_CLIENT_ID = None
OAUTH_CLIENT_SECRET = None
```

## Credits

* Logo by [Laura Barbera](http://www.laurabb.com/)
* Theme by [Christopher Thompson](https://github.com/breadchris)
* Notification Sound by [Terrence Martin](https://soundcloud.com/tj-martin-composer)

---

*This summary was auto-generated by [GitHub Repository Scraper](https://github.com/) from `https://github.com/CTFd/CTFd`.*
