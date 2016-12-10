# Vitola API

## Setup

### virtualenv

It is recommended to use virtualenv and virtualenvwrapper to set up the environment, as there are many moving pieces. Follow the instructions [here](http://virtualenvwrapper.readthedocs.org/en/latest/install.html), specifically under Basic Installation and Shell Startup File.

### Database

To run the app for development, you need to set up PostgreSQL locally.

If you are on a Mac then [Postgres.app](http://postgresapp.com/) is an easy way to get it set up. If you use this, make sure to set up the [command line tools](http://postgresapp.com/documentation/cli-tools.html) as well.

You can verify that your local PostgreSQL server is running via the `psql` command-line tool.

You may run into `psql: FATAL:  database "{your username}" does not exist`. In which case, just issue the command `createdb` and you'll be set up.

Create the database to use for development:
```
psql -c 'create database vitola_api_dev;'
```

Also the database for unit testing:
```
psql -c 'create database vitola_api_test;'
```

### Vitola API Set-up

```
git clone https://github.com/statham/vitola-api.git
cd vitola-api
virtualenv vitola-api
source vitola-api/bin/activate
pip install -r requirements.txt
```

## Start the Vitola API server

run the server locally with this command (using the `config/dev.py` default config file):

```
python manage.py runserver
```

By default that runs on port 5000. Use -p 8001 to change to port 8001, for example.

## Tests

To actually run the tests, first install nose:
```
pip install nose
```

Then run the tests:

```
nosetests -sv tests/
```
