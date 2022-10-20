<!-- Please update value in the {}  -->

<h1 align="center">Django DRF Blog Api</h1>


<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Overview](#overview)
- [Stack & Tools](#stack)
- [Project Structure](#project-structure)
- [How to use](#how-to-use)
- [Contact](#contact)

<!-- OVERVIEW -->

## Overview

This is a back-end blog-api project made with Django DRF. To build this project I have used various tools, including drf-yasg, django toolbar, and django rest auth


<h2 id="stack">Stack & Tools</h2>

- Django
- Django Rest Framework
- PostgreSQL
- Django Debug Toolbar
- drf-yasg (Swagger generator)
- dj-rest-auth



## Project Structure

```bash
.──── django-drf-blog-api (repo)
│
├── README.md
├── debug.log
├── main
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── db.sqlite3
│   ├── settings
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

## How To Use 

To clone and run this application, you'll need [Git](https://git-scm.com)

```bash
# Clone this repository
$ git clone https://github.com/MSKose/django-drf-blog-api

# Install dependencies
    $ python -m venv env
    > env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt

# Add the following to your .env file
    SECRET_KEY=<yourSecretKeyHere>
    DEBUG=True # switch to True when in production
    ENV_NAME=dev # switch to prod when in production
    SQL_DATABASE=<yourDatabaseProjectName>
    SQL_USER=<yourDatabaseUsername> 
    SQL_PASSWORD=<yourDatabasePassword>
    SQL_HOST=localhost 
    SQL_PORT=5432

# Run the app
    $ python manage.py runserver
```

## Contact

- [Linkedin](https://www.linkedin.com/in/mustafa-kose-linked/)
- [GitHub](https://github.com/MSKose)