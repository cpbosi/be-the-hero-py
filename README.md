# Be the Hero Python

This is a simple CRUD created while studying python.

![betheherobranco](https://user-images.githubusercontent.com/21676380/110052873-1097f700-7d37-11eb-89a9-916c78aa31f2.png)

## About the project
Simple Flask using Flask-SQLAlchemy (ORM) to represent an "organização não governmental" and operate CRUD operations over it.

Used Jinja2 to create the simple templates that are "stored" on SQLITE3 database.


## Heroku

This project was deployed on Heroku and can be used on https://betheheropython.herokuapp.com/.



## How To Run

### Install virtualenv
```bash
pip install virtualenv
```


### Open a terminal in the project root directory and run:
```bash
virtualenv env
```


### Then run the command:
```bash
source env\Scripts\activate
```


### Then install the dependencies:
```bash
pip install -r requirements.txt
```

### Finally start the web server:
```bash
python app.py
```
