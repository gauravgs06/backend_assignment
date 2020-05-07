# BackendAssignment

A barebones Hotel Listing App based on Django, which can easily be deployed to Heroku.

## Running Locally

Make sure you have Python 3 [installed locally](http://install.python-guide.org).

```sh
$ mkdir backend_assignment_gaurav
$ cd backend_assignment
$ git clone git@github.com:gauravgs06/backend_assignment.git .

$ pipenv install
$ pipenv shell

$ python manage.py migrate
$ python manage.py collectstatic

$ python manage.py runserver 0.0.0.0:5000
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Installing pipenv

```sh
$ python3 -m pip install pipenv
```

## Deploying on Heroku

Make sure [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) is installed.

```sh
$ heroku login
$ heroku create

$ git push heroku master
$ heroku open
```
