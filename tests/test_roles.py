import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie
import config


class CapstoneRolesCase(unittest.TestCase):
    """This test represent the capstone project"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        # self.config = self.app.config
        database_name = "capstone_test"
        database_path = "postgresql://postgres:admin@{}/{}".format(
            'localhost:5432', database_name)
        setup_db(self.app, database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        pass

    # def tearDownClass(self):
    #     print(self)

    def test_casting_assistant_can_view_actors(self):
        token = config.CASTING_ASSISTANT_TOKEN
        headers = {"Authorization": f"Bearer {token}"}
        resp = self.client().get('/actors', headers=headers)
        result = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(result['success'])

    def test_casting_assistant_can_view_movies(self):
        token = config.CASTING_ASSISTANT_TOKEN
        headers = {"Authorization": f"Bearer {token}"}
        resp = self.client().get('/movies', headers=headers)
        result = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(result['success'])

    def test_casting_assistant_cannot_delete_an_actor(self):
        token = config.CASTING_ASSISTANT_TOKEN
        headers = {"Authorization": f"Bearer {token}"}
        model = Actor(name="Badmus Ope", age=25, gender="male")
        model.insert()
        resp = self.client().delete(
            f'/actors/{model.id}', headers=headers)
        result = json.loads(resp.data)
        self.assertEqual(resp.status_code, 401)
        self.assertFalse(result['success'])

    def test_casting_director_can_add_an_actor(self):
        token = config.CASTING_DIRECTOR_TOKEN
        headers = {"Authorization": f"Bearer {token}"}
        resp = self.client().post('/actors', json={
            "name": "Celine Dion",
            "age": 30,
            "gender": "male"
        }, headers=headers)
        result = json.loads(resp.data)
        # lets get the actor
        actor = Actor.query.get(result['actor']['id'])

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(result['success'])
        self.assertTrue(actor)

    def test_casting_director_cant_delete_a_movie(self):
        token = config.CASTING_DIRECTOR_TOKEN
        headers = {"Authorization": f"Bearer {token}"}
        model = Movie(title="Pursuit of happyness", release_date="2021-01-06")
        model.insert()
        resp = self.client().delete(
            f'/movies/{model.id}', headers=headers)
        result = json.loads(resp.data)
        self.assertEqual(resp.status_code, 401)
        self.assertFalse(result['success'])

    def test_executive_director_can_update_a_movie(self):
        token = config.EXECUTIVE_DIRECTOR_TOKEN
        headers = {"Authorization": f"Bearer {token}"}
        model = Movie(title="Alita the battle angel",
                      release_date="2018-05-22")
        model.insert()
        movie_title = model.title
        resp = self.client().patch(f'/movies/{model.id}', json={
            "title": "Bulletproof",
            "release_date": "2019-03-15"
        }, headers=headers)
        result = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(result['success'])
        self.assertEqual(model.id, result['movie']['id'])
        self.assertNotEqual(movie_title, result['movie']['title'])

    def test_executive_director_can_delete_a_movie(self):
        token = config.EXECUTIVE_DIRECTOR_TOKEN
        headers = {"Authorization": f"Bearer {token}"}
        model = Movie(title="Pursuit of happyness", release_date="2021-01-06")
        model.insert()
        resp = self.client().delete(
            f'/movies/{model.id}', headers=headers)
        result = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(result['success'])
        # check that record was deleted successfully
        deleted_movie = Movie.query.get(model.id)
        self.assertFalse(deleted_movie)
