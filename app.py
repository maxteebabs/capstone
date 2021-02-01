import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor
from flask_migrate import Migrate, MigrateCommand
from auth.auth import requires_auth, AuthError

def create_app(test_config=None):
	# create and configure the app
	app = Flask(__name__)
	app.config.from_object('config')
	CORS(app)
	
	setup_db(app)
	db = SQLAlchemy(app)
	Migrate(app, db)

	@app.route('/')
	def index():
		return ("hello word")

	@app.route('/actors', methods=["GET"])
	@requires_auth('get:actors')
	def get_actors(payload):
		actors = Actor.query.all()
		return jsonify({
			"actors": [actor.format() for actor in actors],
			"success": True
		})

	@app.route('/actors', methods=["POST"])
	@requires_auth('post:actors')
	def create_actor(payload):
		body = request.get_json()
		name = body.get("name")
		age = body.get("age")
		gender = body.get("gender")

		if not name or not age or not gender:
			abort(400)

		actor = Actor(name=name, age=age, gender=gender)
		actor.insert()
		return jsonify({
			"actor": actor.format(),
			"success": True
		})
	
	@app.route('/actors/<actor_id>', methods=["PATCH"])
	@requires_auth('patch:actors')
	def update_actor(payload, actor_id):
		body = request.get_json()
		name = body.get("name", None)
		age = body.get("age", None)
		gender = body.get("gender", None)
		actor = Actor.query.filter_by(id=actor_id).first_or_404()
		if name:
			actor.name = name
		if age:
			actor.age = age
		if gender:
			actor.gender = gender

		actor.update()
		return jsonify({
			"actor": actor.format(),
			"success": True
		})

	@app.route('/actors/<actor_id>', methods=["DELETE"])
	@requires_auth('delete:actors')
	def delete_actor(payload, actor_id):
		actor = Actor.query.filter_by(id=actor_id).first_or_404()
		actor.delete()
		return jsonify({
			"success": True
		})

	@app.route('/movies', methods=["GET"])
	@requires_auth('get:movies')
	def get_movies(payload):
		movies = Movie.query.all()
		return jsonify({
			"movies": [movie.format() for movie in movies],
			"success": True
		})

	@app.route('/movies', methods=["POST"])
	@requires_auth('post:movies')
	def create_movie(payload):
		body = request.get_json()
		title = body.get("title")
		release_date = body.get("release_date")
		
		if not title or not release_date:
			abort(400)
		movie = Movie(title=title, release_date=release_date)
		movie.insert()
		return jsonify({
			"movie": movie.format(),
			"success": True
		})

	@app.route('/movies/<movie_id>', methods=["PATCH"])
	@requires_auth('patch:movies')
	def update_movie(payload, movie_id):
		body = request.get_json()
		movie = Movie.query.filter_by(id=movie_id).first_or_404()
		movie.title = body.get("title")
		movie.release_date = body.get("release_date")

		movie.update()
		return jsonify({
			"movie": movie.format(),
			"success": True
		})

	@app.route('/movies/<movie_id>', methods=["DELETE"])
	@requires_auth('delete:movies')
	def delete_movie(payload, movie_id):
		movie = Movie.query.filter_by(id=movie_id).first_or_404()
		movie.delete()
		return jsonify({
			"success": True
		})

	@app.errorhandler(404)
	def not_found(error):
		return jsonify({
			'success': False,
			'error': 404,
			'message': "Not found"
		}), 404

	@app.errorhandler(422)
	def unprocessible(error):
		return jsonify({
			'success': False,
			'error': 422,
			'message': "Unprocessible"
		}), 422

	@app.errorhandler(400)
	def bad_request(error):
		return jsonify({
			'success': False,
			'error': 400,
			'message': "Bad Request"
		}), 400
	
	@app.errorhandler(405)
	def bad_request(error):
		return jsonify({
			'success': False,
			'error': 405,
			'message': "Method not found"
		}), 405
	
	@app.errorhandler(401)
	def unauthenticated(error):
		return jsonify({
			"success": False,
			"error": 401,
			"message": "unauthenticated"
		}), 401
	
	@app.errorhandler(AuthError)
	def auth_error(ex):
		return jsonify({
			"success": False,
			"error": ex.status_code,
			"message": ex.error['description']
		}), ex.status_code
  
	return app

app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
