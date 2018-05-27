# Stream3 project

[![Build Status](https://travis-ci.org/vieiraa360/full_stack_project.svg?branch=master)](https://travis-ci.org/vieiraa360/full_stack_project)



# Kambolife
**Ecommerce Web Application with User Authentication and Stripe Payments**

This Web App was built as a final project for the Code Institute's full stack project. 
It is a **real costumer** Ecommerce site built with Python's *Django* framework.

## Live Demo

**Follow this link to view deployed version of the web app https://full-stack-stream3.herokuapp.com/**

## Technologies used
1. Django
2. Python
2. HTML
3. CSS
4. JavaScript
5. JQuery
4. Bootstrap
5. SQLite/Postgress database
6. Cloud9 IDE
7. Github
7. Heroku

## Added reusable apps and scripts
1. Accounts - obtained from stream3 lessons
2. Avatar - obtained from Django-avatar **https://django-avatar.readthedocs.io/en/latest/**
2. Blog - obtained from stream3 lessons 
3. Caption hover effect - obtained from **https://bootsnipp.com/snippets/featured/caption-hover-effect-text**
4. Cookie consent popup disclaimer - obtained from ClouFlare CDN libraries **https://cdnjs.com/libraries/cookieconsent2**
2. Posts - obtained from stream3 lessons
3. Testimonials - obtained from pinaxproject **https://github.com/pinax/pinax-testimonials**

## Deployment / Hosting

This Project is hosted on Heroku with automatic deployments from GitHub

## Databases / Static Files

When running locally, SQLite database is used & static and media files were stored locally. 
When running from Heroku, Postgres is used as the database server & an Amazon S3 bucket has been set 
up to host the static and media files.

## Installation

This project can be cloned from: **https://github.com/vieiraa360/full_stack_project**.

1. Navigate to desired folder in your terminal & type:
    `$ git clone https://github.com/vieiraa360/full_stack_project`
2. Create & Activate a new Virtual Environment in terminal:
    Create: `$ python3 -m venv ~/virtualenvs/name_of_environment`
    Activate: `$ source ~/virtualenvs/name_of_environment/bin/activate`
3. Install the project dependancies:
    `$ pip3 install -r requirements.txt`
4. Create env.py file at the top level of the project (this will contain all sensitive information)
    **MAKE SURE IT IS IN THE .gitignore FILE**
5. Copy the following into the env.py file, replacing <> contents with the actual keys:
```
import os
os.environ.setdefault("STRIPE_PUBLISHABLE", "<stripe publishable key>")
os.environ.setdefault("STIPE_SECRET", "<stripe secret>")
os.environ.setdefault("DATABASE_URL", "<database url"
os.environ.setdefault("SECRET_key", "<secret key>")
os.environ.setdefault("AWS_ACCESS_KEY_ID", "<aws access key>")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "<aws secret access key>")
os.environ.setdefault("AWS_STORAGE_BUCKET_NAME", "<aws bucket name>")
```

* A new SECRET_KEY can be generated [here](https://www.miniwebtool.com/django-secret-key-generator/)
* Set up an account with Stripe [here](https://stripe.com/gb) & input STRIPE_PUBLISHABLE_KEY & STRIPE_SECRET_KEY 
* Database url can be obtained from Heroku app dashboard > settings > environment variables
* AWS keys are obtained at user or user group creation on the aws console


6. In the terminal:
    `$ python manage.py migrate` - this will apply migrations to the database
    `$ python manage.py createsuperuser` - this will create an administration user
    `$ python manage.py runserver` - this will run the project
7. Go to your browser and type '127.0.0.1:8000' in the address bar
8. The app will run on your browser
9. Log in to the admin panel by going to '127.0.0.1:8000/admin' and log in using the superuser credentials
10. You can manage the site from there

## Running the tests

The tests can be found in the tests.py file within the App folders. 
To run the tests, activate the virtual environment and type:

`$ python manage.py test`