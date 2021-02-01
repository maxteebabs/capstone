import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie
import config


class CapstoneMovieCase(unittest.TestCase):
    """This test represent the capstone Movie module"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client

        # lets use the executive director token because it has all permissions
        token = config.EXECUTIVE_DIRECTOR_TOKEN
        self.headers = {"Authorization": f"Bearer {token}"}

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

    """Test for Movies """
    def test_get_movies(self):
        resp = self.client().get('/movies', headers=self.headers)
        result = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(result['success'])

    def test_create_movie(self):
        resp = self.client().post('/movies', json={
            "title": "The transporter",
            "release_date": '2020-01-20'
        }, headers=self.headers)
        result = json.loads(resp.data)
        # lets get the movie
        movie = Movie.query.get(result['movie']['id'])

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(result['success'])
        self.assertTrue(movie)

    def test_create_movie_bad_request(self):
        resp = self.client().post('/movies', json={
            "title": "Spartacus",
        }, headers=self.headers)
        result = json.loads(resp.data)
        self.assertEqual(resp.status_code, 400)
        self.assertFalse(result['success'])
        self.assertEqual(result['message'], 'Bad Request')

    def test_update_movie(self):
        model = Movie(
            title="Alita the battle angel", release_date="2018-05-22")
        model.insert()
        movie_title = model.title
        resp = self.client().patch(f'/movies/{model.id}', json={
            "title": "Bulletproof",
            "release_date": "2019-03-15"
        }, headers=self.headers)
        result = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(result['success'])
        self.assertEqual(model.id, result['movie']['id'])
        self.assertNotEqual(movie_title, result['movie']['title'])

    def test_update_movie_not_found(self):
        resp = self.client().patch(f'/movies/99999', json={
            "title": "Bulletproof",
            "release_date": "2019-03-15"
        }, headers=self.headers)
        result = json.loads(resp.data)
        self.assertEqual(resp.status_code, 404)
        self.assertFalse(result['success'])
        self.assertEqual(result['message'], "Not found")

    def test_delete_movie(self):
        model = Movie(title="Pursuit of happyness", release_date="2021-01-06")
        model.insert()
        resp = self.client().delete(
            f'/movies/{model.id}', headers=self.headers)
        result = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(result['success'])
        # check that record was deleted successfully
        deleted_movie = Movie.query.get(model.id)
        self.assertFalse(deleted_movie)

    def test_delete_movie_not_found(self):
        resp = self.client().delete(f'/movies/99999', headers=self.headers)
        result = json.loads(resp.data)
        self.assertEqual(resp.status_code, 404)
        self.assertFalse(result['success'])
        self.assertEqual(result['message'], "Not found")
