import datetime
from flask import abort
from flask_sqlalchemy import SQLAlchemy
import sys
db = SQLAlchemy()


def setup_db(app, database_path=None):
    if(database_path):
        app.config["SQLALCHEMY_DATABASE_URI"] = database_path
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class DBModel(db.Model):
    """base model to inherit from """
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            print(sys.exc_info())
            db.session.rollback()
            abort(400)

    def update(self):
        try:
            db.session.commit()
        except:
            print(sys.exc_info())
            db.session.rollback()
            abort(400)

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            print(sys.exc_info())
            db.session.rollback()
            abort(400)


class Movie(DBModel):
    __tablename__ = 'movies'

    def __repr__(self):
        return f'<Movie> id:{self.id}, title: {self.title}'

    title = db.Column(db.String(120))
    release_date = db.Column(db.DateTime)

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }


class Actor(DBModel):
    __tablename__ = 'actors'

    def __repr__(self):
        return f'<Actor> id:{self.id}, name: {self.name}'

    name = db.Column(db.String(120))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }
