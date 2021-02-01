## CAPSTONE APP
----

## INTRODUCTION
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

### HEROKU URL 
This application is hosted on heroku and a link is provided here. 
https://remmy-capstone-app.herokuapp.com

## Getting Started
### Installing Dependencies
#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


```bash
pip install -r requirements.txt
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM. I made use of POSTGRESql database.
Details is found in models.py 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension I used for cross origin request


## Starting the App
###  Setting up the environment variables
```bash
source setup.sh
```
### To start the application, run 
```bash
python app.py
```

### How to run test
```bash
python -m unittest discover
```

#### ROLES

#####  CASTING ASSISTANT
* The casting assistant can only view actors and movies

##### CASTING DIRECTOR
* This role has all the permissions that the CASTING ASSISTANT has
* It also has permissions to add or delete an actor from the database
* It has permissions to modify actors or movies

##### EXECUTIVE PRODUCER
* This role has all the permissions that the CASTING DIRECTOR has
* It can also add or delete a movie from the database

#### Permissions
The permissions for this application includes the following:
* get:actors - access to retrieve all actors
* post:actor - access to create an actor
* patch:actor - access to update an actor
* delete:actor - access to delete an actor
* get:movies - access to retrieve all movies
* post:movie - access to create a movie
* patch:movie - access to update a movie
* delete:movie - access to delete a movie


## DATA MODELLING
The data model of the project is provided in models.py file in the root of the project. The 
following schema for the database and helper methods are used for API behaviour:
Two tables are created: actors and movies
* The Actor model contains id as primary key
* Attributes of the Actor model also include name, age and gender
* The Movie model contains id as primary key
* Attributes of the Movie Model also include title and release_date

## API Endpoints
### GET '/actors'
* fetches a collection of all actors in the database
```
Sample curl request: curl -X GET https://remmy-capstone-app.herokuapp.com/actors
```
Sample Response:
```

```
