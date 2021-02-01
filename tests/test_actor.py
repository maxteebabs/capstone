import unittest
import json
import os
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor


class CapstoneActorCase(unittest.TestCase):
    """This test represent the capstone project"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client

        # lets use the executive director token because it has all permissions
        token = os.environ.get('EXECUTIVE')
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

    # def tearDownClass(self):
    #     print(self)

    def test_get_actors(self):
        resp = self.client().get('/actors', headers=self.headers)
        result = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(result['success'])

    def test_create_actor(self):
        resp = self.client().post('/actors', json={
            "name": "Celine Dion",
            "age": 30,
            "gender": "male"
        }, headers=self.headers)
        result = json.loads(resp.data)
        # lets get the actor
        actor = Actor.query.get(result['actor']['id'])

        self.assertEqual(resp.status_code, 200)
        self.assertTrue(result['success'])
        self.assertTrue(actor)

    def test_create_actor_bad_request(self):
        resp = self.client().post('/actors', json={
            "name": "Celine Dion",
            "age": 30,
            "genderddd": "male"
        }, headers=self.headers)
        result = json.loads(resp.data)
        self.assertEqual(resp.status_code, 400)
        self.assertFalse(result['success'])
        self.assertEqual(result['message'], 'Bad Request')

    def test_update_actor(self):
        model = Actor(name="Badmus Trump", age=25, gender="male")
        model.insert()
        actor_name = model.name
        resp = self.client().patch(f'/actors/{model.id}', json={
            "name": "Felicia Jeffery",
            "age": 30,
            "gender": "female"
        }, headers=self.headers)
        result = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(result['success'])
        self.assertEqual(model.id, result['actor']['id'])
        self.assertNotEqual(actor_name, result['actor']['name'])

    def test_update_actor_not_found(self):
        resp = self.client().patch(f'/actors/99999', json={
            "name": "Celine Dion",
            "age": 30,
            "gender": "male"
        }, headers=self.headers)
        result = json.loads(resp.data)
        self.assertEqual(resp.status_code, 404)
        self.assertFalse(result['success'])
        self.assertEqual(result['message'], "Not found")

    def test_delete_actor(self):
        model = Actor(name="Badmus Ope", age=25, gender="male")
        model.insert()
        resp = self.client().delete(
            f'/actors/{model.id}', headers=self.headers)
        result = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(result['success'])
        # check that record was deleted successfully
        deleted_actor = Actor.query.get(model.id)
        self.assertFalse(deleted_actor)

    def test_delete_actor_not_found(self):
        resp = self.client().delete(f'/actors/99999', headers=self.headers)
        result = json.loads(resp.data)
        self.assertEqual(resp.status_code, 404)
        self.assertFalse(result['success'])
        self.assertEqual(result['message'], "Not found")
