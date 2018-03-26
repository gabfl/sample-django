# sample-django

Django basic example

## Installation

```bash
virtualenv venv
source venv/bin/activate
pip3 install django

# Start project
django-admin startproject myproject

# Start App
cd myproject
mkdir -p myproject/apps/sample
python manage.py startapp sample myproject/apps/sample
```

## Run the app

```bash
python manage.py runserver
```

## Usage

### App

Visit http://127.0.0.1:8000/sample/
