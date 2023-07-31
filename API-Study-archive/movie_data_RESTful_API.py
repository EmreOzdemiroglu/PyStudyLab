from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

class Movie(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    budget = db.Column(db.Integer)
    genres = db.Column(db.String(500))
    homepage = db.Column(db.String(500))
    id = db.Column(db.Integer)
    keywords = db.Column(db.String(500))
    original_language = db.Column(db.String(100))
    original_title = db.Column(db.String(500))
    overview = db.Column(db.String(5000))
    popularity = db.Column(db.Float)
    # Add other columns as necessary
    # ...

class MovieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Movie

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

class MovieListResource(Resource):
    def get(self):
        movies = Movie.query.all()
        return movies_schema.dump(movies), 200

    def post(self):
        new_movie = Movie(**request.get_json())
        db.session.add(new_movie)
        db.session.commit()
        return movie_schema.dump(new_movie), 201

api.add_resource(MovieListResource, '/movies')

class MovieResource(Resource):
    def get(self, movie_id):
        movie = Movie.query.get_or_404(movie_id)
        return movie_schema.dump(movie), 200

    def put(self, movie_id):
        movie = Movie.query.get_or_404(movie_id)
        movie.update(request.get_json())
        db.session.commit()
        return movie_schema.dump(movie), 200

    def delete(self, movie_id):
        movie = Movie.query.get_or_404(movie_id)
        db.session.delete(movie)
        db.session.commit()
        return '', 204

api.add_resource(MovieResource, '/movies/<int:movie_id>')

@app.route('/movies/search', methods=['GET'])
def search_movies():
    arg_list = ['genres', 'original_language', 'original_title', 'keywords']
    filters = {arg: request.args[arg] for arg in arg_list if arg in request.args}
    movies = Movie.query.filter_by(**filters).all()
    return movies_schema.dump(movies), 200

@app.route('/movies/popular', methods=['GET'])
def popular_movies():
    limit = request.args.get('limit', default=10, type=int)
    movies = Movie.query.order_by(Movie.popularity.desc()).limit(limit).all()
    return movies_schema.dump(movies), 200

# Load the CSV data into the database
engine = create_engine('sqlite:///movies.db')
df = pd.read_csv('/mnt/data/movie_dataset.csv')
df.to_sql('movies', engine, if_exists='replace')

if __name__ == '__main__':
    app.run(debug=True)

