from settings import app,db
from models import Movies,Dates
import json
from flask import jsonify, request,make_response,abort


@app.route('/showtimes',methods=['GET'])
def showtimes_list():
    if request.method == 'GET':
        #d = Dates.query.filter_by(id=3).first().showtime
        show = Dates.query.all()
        #return jsonify(Movies = [i.serialize for i in movies])
        #d = Dates.query.filter_by(id=i.id).first().showtime
        return jsonify(Showtimes = [i.serialize for i in show])
        #return ([Dates.query.filter_by(id=i.id).first().showtime for i in Dates.query.all()])


@app.route('/showtimes/<int:id>',methods=['GET'])
def showtimes_get(id):
    if request.method == 'GET':
        try:
            show = Dates.query.filter_by(id=id).one()
            return jsonify(show.serialize)
        except:
            abort(404)
        #return jsonify(Showtimes = [i.serialize for i in show])

# @app.route('/showtimes/<int:id>', methods=['GET'])
# def get_movie(id):
#
#     try:
#          showtime = Showtimes.query.filter_by(id=id).one()
#          return jsonify(User = user.serialize)
#     except:
#         abort(404)

@app.route('/mv/add',methods=['POST'])
def add_movie():
    id = request.args.get('id','')
    if id == '':
        abort(400)
    if Movies.query.filter_by(id=id).first() is not None:

        return jsonify({"message":"movie alaredy exists in showtime Database"}), 200

    movie = Movies(id=id)
    db.session.add(movie)
    db.session.commit()
    return 'Movie added in the showtime service'
    #return jsonify({'Title': movie.title,'Raiting': movie.rating, 'id': movie.id})

@app.route('/show',methods=['GET'])
def show_movies():
    movies = Movies.query.all()
    m = []
    for i in movies:
        m.append(i.id)

    print(m)
    return 'watch console'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
