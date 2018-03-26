# sample-django

Django basic example

## Installation

```bash
virtualenv venv
source venv/bin/activate
pip3 install django djangorestframework markdown django-filter

# Start project
django-admin startproject myproject

# Start app
cd myproject
mkdir -p myproject/apps/sample
python manage.py startapp sample myproject/apps/sample

# Start REST API app
mkdir myproject/apps/sample_rest
python manage.py startapp sample_rest myproject/apps/sample_rest

# Migrate
python manage.py makemigrations sample_rest
python manage.py migrate
```

## Add users

```bash
sqlite3 db.sqlite3
```

## Run the app

```bash
python manage.py runserver
```

## Usage

### App

Visit http://127.0.0.1:8000/sample/

## API

```bash
$ curl -s http://127.0.0.1:8000/sample_rest/user/2 | beautify
{
    "name": null,
    "email": "tom@gmail.com"
}

$ curl -s http://127.0.0.1:8000/sample_rest/users | beautify 
[
    {
        "name": null,
        "email": "gab@gmail.com"
    },
    {
        "name": null,
        "email": "bob@gmail.com"
    },
    {
        "name": null,
        "email": "tom@gmail.com"
    }
]
```