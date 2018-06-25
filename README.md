# To-do list app

This is a simple webapp for making to-do lists. 
It is live on http://todolist.pythonanywhere.com

## About project
- made upon python Django framework.
- uses Bootstrap3 with jQuery on the frontend.
- Database used is MySQL, managed by django ORM.

## Prerequisites for setup
Python3 with virtualenv


## Build / Run 
-> create and activate a python virtualenv

-> `$ pip install -r requirements.txt`

-> `$ cd todo/`

-> `$ nano database.cnf`

-> paste the following contents in database.cnf (replaced with your db credentials) :
```
[client]
database = DATABASE_NAME
host = DATABASE_HOST
port = 3306 
user = DATABASE_USER
password = DATABASE_PASSWORD
default-character-set=utf8
```
-> Note that you need to create an empty database (for DATABASE_NAME ) on your DB server.

-> `python manage.py migrate`

-> `python manage.py runserver`

-> app will be live on `127.0.0.1:8000`


#### Developer contact
 - [ github ](https://github.com/sanskarsharma)
 - [ linkedin ](https://linkedin.com/in/sanskarssh)
 - [angel](https://angel.co/sanskarsharma)

     
