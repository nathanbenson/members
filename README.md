Members application
====================

This is a test application that is designed to store member information.


Local Deployment for Development
--------------------------------

Checkout the codebase from our Git repository server.

```
git clone git@github.com:nathanbenson/members.git
```

A Python virtual environment needs to be created to isolate your member application.
membes is a Django based python3.6 application. If python version 3.6 is not
available in your workstation, it needs to installed before setting up the virtual environment. For instructions on how
to set up virtualenv and virtualenv-wrapper, go to the following page.

```
https://docs.python.org/3/library/venv.html
http://virtualenvwrapper.readthedocs.io/en/latest/
```

MySQL and Celery with RabbitMq (Broker) are used in this project and it needs to be setup in your local workstation.
Instructions to setup them are provided in the following pages.

```
https://www.servermania.com/kb/articles/install-sqlite/
http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html#rabbitmq

```
To run celery use the following command:

```
celery -A members worker -l info

```

All third-party packages for development are included in the *requirements/main.txt* file.

```
pip install -r requirements/main.txt
```

Before running the application you should create a **local.py** in the *members/ package directory.
The changes contained in this file will override the default settings necessary for local development.
*Note - You should never commit a local.py file to the repository.*
Setting up a local mysql database in your local.py file is recommended.
Local file should include configurations of Celery and MySQL.

```
touch members/local.py
```

Before actually running the django server, follow these django instructions:

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver (Port of your choice)
```

Curl commands to create a user.

```

curl --header "Content-Type: application/json" -d '{"first_name": "john", "last_name": "Doe", "phone_number":"93","client_member_id": "91", "provider_info": ["16"]}' http://localhost:8000/api/create_member/

```

api endpoints:
```
http://localhost:8000/api/get_members_by_acc_id/12/
http://localhost:8000/api/get_member_by_phone/6670161365/
http://localhost:8000/api/get_member_by_id/1/
http://localhost:8000/api/get_member_by_client_id/3865044/
http://localhost:8000/api/generate_sub_batch/   Upload a csv and hit upload.

local admin
http://localhost:8000/admin/
```