from settings import app,db
from models import Movies
import json
from flask import jsonify, request,make_response,abort


@app.route('/movies',methods=['GET'])
def movies():
    if request.method == 'GET':
        movies = Movies.query.all()
        #return jsonify(Movies = [i.serialize for i in movies])
        return jsonify(Movies = [i.serialize for i in movies])

@app.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):

    try:
         movie = Movies.query.filter_by(id=id).one()
         return jsonify(Movie = movie.serialize)
    except:
        abort(404)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
