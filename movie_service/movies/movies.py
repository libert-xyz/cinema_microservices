from settings import app,db
from models import Movies
import json
from flask import jsonify, request,make_response,abort, abort

@app.route('/movies',methods=['GET'])
def movies():
    if request.method == 'GET':
        movies = Movies.query.all()
        #return jsonify(Movies = [i.serialize for i in movies])
        return jsonify(Movies = [i.serialize for i in movies])

@app.route('/movies/<int:id>', methods=['GET','PUT','DELETE'])
def get_movie(id):

    try:
         movie = Movies.query.filter_by(id=id).one()
         if request.method == 'GET':
             return jsonify(Movie = movie.serialize)

         elif request.method == 'PUT':
            title = request.args.get('title')
            rating = request.args.get('rating')

            if title:
                movie.title = title

            if rating:
                movie.rating = rating

            db.session.add(movie)
            db.session.commit()

            return jsonify(Movie = movie.serialize)

         elif request.method == 'DELETE':
             db.session.delete(movie)
             db.session.commit()
             return 'Movie Deleted'
    except:
        abort(404)

@app.route('/movies',methods=['POST'])
def new_movies():

    title = request.args.get('title','')
    rating = request.args.get('rating','')
    if title == '' or rating == '':
        abort(400)
    if Movies.query.filter_by(title=title).first() is not None:

        return jsonify({"message":"movie alaredy exists"}), 200

    movie = Movies(title=title)
    movie.rating = rating
    db.session.add(movie)
    db.session.commit()

    return jsonify({'Title': movie.title,'Raiting': movie.rating, 'id': movie.id})



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
