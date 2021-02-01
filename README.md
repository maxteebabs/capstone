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

### ROLES

####  CASTING ASSISTANT
* The casting assistant can only view actors and movies

#### CASTING DIRECTOR
* This role has all the permissions that the CASTING ASSISTANT has
* It also has permissions to add or delete an actor from the database
* It has permissions to modify actors or movies

#### EXECUTIVE PRODUCER
* This role has all the permissions that the CASTING DIRECTOR has
* It can also add or delete a movie from the database

### Permissions
The permissions for this application includes the following:
* get:actors - access to retrieve all actors
* post:actors - access to create an actor
* patch:actors - access to update an actor
* delete:actors - access to delete an actor
* get:movies - access to retrieve all movies
* post:movies - access to create a movie
* patch:movies - access to update a movie
* delete:movies - access to delete a movie


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
Sample curl request: curl --location --request GET 'https://remmy-capstone-app.herokuapp.com/actors' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFTVkY1OTJ5RS14eGFJcTdLdGJtQyJ9.eyJpc3MiOiJodHRwczovL2Rldi00ZGt4NHVxai51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAxNjMzZThmZmNiZTIwMDZhODkyMTg1IiwiYXVkIjoiaHR0cHM6Ly9jYXBzdG9uZS8iLCJpYXQiOjE2MTIxMzU3OTAsImV4cCI6MTYxMjIyMjE5MCwiYXpwIjoiZEQzaGlZZ1d3WmhXVnBlb3lQRzlYSENtdVNjRmRkbDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.oEjGJXWS8PsygU4rtZQnt_Rkss56fwPHC-1T6ZPorBq_-stkdAuuw_qpQMaXMbpbGYZBTACEX6zoOFvJJie_UFiUB6jNZHWgjQOPgZS149G-FTqusLJQS_fwmYtPwKKOaoGpw8SLNRFUoh4DojLEdCAOqqaJGLDVZ8ZSsCQR4fx9JE8yLnUj0daAzcURscH2H-hRTsD4TyUFJ1qbTlggohKxk9jR3sFcB-UsAUWnTNe5dssQ7V4do3ObnrY8FGe2yI5Y9XU5fC98F7XsE9nOGJwC_qT32eu43zJGgfx0lGvsUKESpiyYQBGyXr1gfCqP5xYGtkbGi6obbhUo_e47PQ' \
--header 'Content-Type: application/json'
```

Sample Response:

```
{
    "actors": [
        {
            "age": 20,
            "gender": "male",
            "id": 2,
            "name": "Smith Russel"
        }
    ],
    "success": true
}
```

### POST '/actors'
* create an actor in the database

```
Sample curl request: curl --location --request POST 'https://remmy-capstone-app.herokuapp.com/actors' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFTVkY1OTJ5RS14eGFJcTdLdGJtQyJ9.eyJpc3MiOiJodHRwczovL2Rldi00ZGt4NHVxai51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAxNjMzZThmZmNiZTIwMDZhODkyMTg1IiwiYXVkIjoiaHR0cHM6Ly9jYXBzdG9uZS8iLCJpYXQiOjE2MTIxMzU3OTAsImV4cCI6MTYxMjIyMjE5MCwiYXpwIjoiZEQzaGlZZ1d3WmhXVnBlb3lQRzlYSENtdVNjRmRkbDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.oEjGJXWS8PsygU4rtZQnt_Rkss56fwPHC-1T6ZPorBq_-stkdAuuw_qpQMaXMbpbGYZBTACEX6zoOFvJJie_UFiUB6jNZHWgjQOPgZS149G-FTqusLJQS_fwmYtPwKKOaoGpw8SLNRFUoh4DojLEdCAOqqaJGLDVZ8ZSsCQR4fx9JE8yLnUj0daAzcURscH2H-hRTsD4TyUFJ1qbTlggohKxk9jR3sFcB-UsAUWnTNe5dssQ7V4do3ObnrY8FGe2yI5Y9XU5fC98F7XsE9nOGJwC_qT32eu43zJGgfx0lGvsUKESpiyYQBGyXr1gfCqP5xYGtkbGi6obbhUo_e47PQ' \
--header 'Content-Type: application/json' \
--data-raw '{
    "age": 20,
    "name": "Smith Russel",
    "gender": "male",
}'
```

Sample Response:

```
{
    "actor": {
        "age": 20,
        "gender": "male",
        "id": 1,
        "name": "Smith Russel"
    },
    "success": true
}
```


### PATCH '/actors/1'
* update an actor

```
Sample curl request: curl --location --request PATCH 'https://remmy-capstone-app.herokuapp.com/actors/1' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFTVkY1OTJ5RS14eGFJcTdLdGJtQyJ9.eyJpc3MiOiJodHRwczovL2Rldi00ZGt4NHVxai51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAxNjMzZThmZmNiZTIwMDZhODkyMTg1IiwiYXVkIjoiaHR0cHM6Ly9jYXBzdG9uZS8iLCJpYXQiOjE2MTIxMzU3OTAsImV4cCI6MTYxMjIyMjE5MCwiYXpwIjoiZEQzaGlZZ1d3WmhXVnBlb3lQRzlYSENtdVNjRmRkbDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.oEjGJXWS8PsygU4rtZQnt_Rkss56fwPHC-1T6ZPorBq_-stkdAuuw_qpQMaXMbpbGYZBTACEX6zoOFvJJie_UFiUB6jNZHWgjQOPgZS149G-FTqusLJQS_fwmYtPwKKOaoGpw8SLNRFUoh4DojLEdCAOqqaJGLDVZ8ZSsCQR4fx9JE8yLnUj0daAzcURscH2H-hRTsD4TyUFJ1qbTlggohKxk9jR3sFcB-UsAUWnTNe5dssQ7V4do3ObnrY8FGe2yI5Y9XU5fC98F7XsE9nOGJwC_qT32eu43zJGgfx0lGvsUKESpiyYQBGyXr1gfCqP5xYGtkbGi6obbhUo_e47PQ' \
--header 'Content-Type: application/json' \
--data-raw '{
    "age": 20,
    "name": "Smith Russel",
    "gender": "male",
}'
```

Sample Response:

```
{
    "actor": {
        "age": 20,
        "gender": "male",
        "id": 1,
        "name": "Smith Russel"
    },
    "success": true
}
```

### Delete '/actors/1'
* Delete an actor

```
curl --location --request DELETE 'https://remmy-capstone-app.herokuapp.com/actors/1' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFTVkY1OTJ5RS14eGFJcTdLdGJtQyJ9.eyJpc3MiOiJodHRwczovL2Rldi00ZGt4NHVxai51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAxNjMzZThmZmNiZTIwMDZhODkyMTg1IiwiYXVkIjoiaHR0cHM6Ly9jYXBzdG9uZS8iLCJpYXQiOjE2MTIxMzU3OTAsImV4cCI6MTYxMjIyMjE5MCwiYXpwIjoiZEQzaGlZZ1d3WmhXVnBlb3lQRzlYSENtdVNjRmRkbDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.oEjGJXWS8PsygU4rtZQnt_Rkss56fwPHC-1T6ZPorBq_-stkdAuuw_qpQMaXMbpbGYZBTACEX6zoOFvJJie_UFiUB6jNZHWgjQOPgZS149G-FTqusLJQS_fwmYtPwKKOaoGpw8SLNRFUoh4DojLEdCAOqqaJGLDVZ8ZSsCQR4fx9JE8yLnUj0daAzcURscH2H-hRTsD4TyUFJ1qbTlggohKxk9jR3sFcB-UsAUWnTNe5dssQ7V4do3ObnrY8FGe2yI5Y9XU5fC98F7XsE9nOGJwC_qT32eu43zJGgfx0lGvsUKESpiyYQBGyXr1gfCqP5xYGtkbGi6obbhUo_e47PQ'
```

Sample Response:

```
{
    "success": true
}
```

### GET '/movies'
* fetches a collection of all movies in the database

```
Sample curl request: curl --location --request GET 'https://remmy-capstone-app.herokuapp.com/movies' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFTVkY1OTJ5RS14eGFJcTdLdGJtQyJ9.eyJpc3MiOiJodHRwczovL2Rldi00ZGt4NHVxai51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAxNjMzZThmZmNiZTIwMDZhODkyMTg1IiwiYXVkIjoiaHR0cHM6Ly9jYXBzdG9uZS8iLCJpYXQiOjE2MTIxMzU3OTAsImV4cCI6MTYxMjIyMjE5MCwiYXpwIjoiZEQzaGlZZ1d3WmhXVnBlb3lQRzlYSENtdVNjRmRkbDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.oEjGJXWS8PsygU4rtZQnt_Rkss56fwPHC-1T6ZPorBq_-stkdAuuw_qpQMaXMbpbGYZBTACEX6zoOFvJJie_UFiUB6jNZHWgjQOPgZS149G-FTqusLJQS_fwmYtPwKKOaoGpw8SLNRFUoh4DojLEdCAOqqaJGLDVZ8ZSsCQR4fx9JE8yLnUj0daAzcURscH2H-hRTsD4TyUFJ1qbTlggohKxk9jR3sFcB-UsAUWnTNe5dssQ7V4do3ObnrY8FGe2yI5Y9XU5fC98F7XsE9nOGJwC_qT32eu43zJGgfx0lGvsUKESpiyYQBGyXr1gfCqP5xYGtkbGi6obbhUo_e47PQ' \
--header 'Content-Type: application/json'
```

Sample Response:

```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Thu, 23 Jan 2020 00:00:00 GMT",
            "title": "Transporter"
        }
    ],
    "success": true
}
```

### POST '/movies'
* create a movie in the database

```
Sample curl request: curl --location --request POST 'https://remmy-capstone-app.herokuapp.com/movies' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFTVkY1OTJ5RS14eGFJcTdLdGJtQyJ9.eyJpc3MiOiJodHRwczovL2Rldi00ZGt4NHVxai51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAxNjMzZThmZmNiZTIwMDZhODkyMTg1IiwiYXVkIjoiaHR0cHM6Ly9jYXBzdG9uZS8iLCJpYXQiOjE2MTIxMzU3OTAsImV4cCI6MTYxMjIyMjE5MCwiYXpwIjoiZEQzaGlZZ1d3WmhXVnBlb3lQRzlYSENtdVNjRmRkbDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.oEjGJXWS8PsygU4rtZQnt_Rkss56fwPHC-1T6ZPorBq_-stkdAuuw_qpQMaXMbpbGYZBTACEX6zoOFvJJie_UFiUB6jNZHWgjQOPgZS149G-FTqusLJQS_fwmYtPwKKOaoGpw8SLNRFUoh4DojLEdCAOqqaJGLDVZ8ZSsCQR4fx9JE8yLnUj0daAzcURscH2H-hRTsD4TyUFJ1qbTlggohKxk9jR3sFcB-UsAUWnTNe5dssQ7V4do3ObnrY8FGe2yI5Y9XU5fC98F7XsE9nOGJwC_qT32eu43zJGgfx0lGvsUKESpiyYQBGyXr1gfCqP5xYGtkbGi6obbhUo_e47PQ' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "Transporter",
    "release_date": "january 23,2020"
}'
```

Sample Response:

```
{
    "movie": {
        "id": 1,
        "release_date": "Thu, 23 Jan 2020 00:00:00 GMT",
        "title": "Transporter"
    },
    "success": true
}
```

### PATCH '/movies/1'
* update a movie

```
Sample curl request: curl --location --request PATCH 'https://remmy-capstone-app.herokuapp.com/movies/1' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFTVkY1OTJ5RS14eGFJcTdLdGJtQyJ9.eyJpc3MiOiJodHRwczovL2Rldi00ZGt4NHVxai51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAxNjMzZThmZmNiZTIwMDZhODkyMTg1IiwiYXVkIjoiaHR0cHM6Ly9jYXBzdG9uZS8iLCJpYXQiOjE2MTIxMzU3OTAsImV4cCI6MTYxMjIyMjE5MCwiYXpwIjoiZEQzaGlZZ1d3WmhXVnBlb3lQRzlYSENtdVNjRmRkbDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.oEjGJXWS8PsygU4rtZQnt_Rkss56fwPHC-1T6ZPorBq_-stkdAuuw_qpQMaXMbpbGYZBTACEX6zoOFvJJie_UFiUB6jNZHWgjQOPgZS149G-FTqusLJQS_fwmYtPwKKOaoGpw8SLNRFUoh4DojLEdCAOqqaJGLDVZ8ZSsCQR4fx9JE8yLnUj0daAzcURscH2H-hRTsD4TyUFJ1qbTlggohKxk9jR3sFcB-UsAUWnTNe5dssQ7V4do3ObnrY8FGe2yI5Y9XU5fC98F7XsE9nOGJwC_qT32eu43zJGgfx0lGvsUKESpiyYQBGyXr1gfCqP5xYGtkbGi6obbhUo_e47PQ' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "Transporter",
    "release_date": "january 23,2020"
}'
```

Sample Response:

```
{
    "movie": {
        "id": 1,
        "release_date": "Thu, 23 Jan 2020 00:00:00 GMT",
        "title": "Transporter"
    },
    "success": true
}
```

### Delete '/movies/1'
* Delete a movie

```
curl --location --request DELETE 'https://remmy-capstone-app.herokuapp.com/movies/1' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFTVkY1OTJ5RS14eGFJcTdLdGJtQyJ9.eyJpc3MiOiJodHRwczovL2Rldi00ZGt4NHVxai51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAxNjMzZThmZmNiZTIwMDZhODkyMTg1IiwiYXVkIjoiaHR0cHM6Ly9jYXBzdG9uZS8iLCJpYXQiOjE2MTIxMzU3OTAsImV4cCI6MTYxMjIyMjE5MCwiYXpwIjoiZEQzaGlZZ1d3WmhXVnBlb3lQRzlYSENtdVNjRmRkbDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.oEjGJXWS8PsygU4rtZQnt_Rkss56fwPHC-1T6ZPorBq_-stkdAuuw_qpQMaXMbpbGYZBTACEX6zoOFvJJie_UFiUB6jNZHWgjQOPgZS149G-FTqusLJQS_fwmYtPwKKOaoGpw8SLNRFUoh4DojLEdCAOqqaJGLDVZ8ZSsCQR4fx9JE8yLnUj0daAzcURscH2H-hRTsD4TyUFJ1qbTlggohKxk9jR3sFcB-UsAUWnTNe5dssQ7V4do3ObnrY8FGe2yI5Y9XU5fC98F7XsE9nOGJwC_qT32eu43zJGgfx0lGvsUKESpiyYQBGyXr1gfCqP5xYGtkbGi6obbhUo_e47PQ'
```

Sample Response:

```
{
    "success": true
}
```