from settings import app,db,nice_json
from models import User
import json
from flask import jsonify, request,make_response,abort
from werkzeug.exceptions import NotFound, ServiceUnavailable
import requests

@app.route('/user',methods=['GET'])
def movies():
    if request.method == 'GET':
        users = User.query.all()
        #return jsonify(Movies = [i.serialize for i in movies])
        return jsonify(Users = [i.serialize for i in users])

@app.route('/user/<int:id>', methods=['GET'])
def get_movie(id):

    try:
         user = User.query.filter_by(id=id).one()
         return jsonify(User = user.serialize)
    except:
        abort(404)

@app.route('/user/<int:id>/booking',methods=['GET'])
def get_booking(id):
    try:
        users_bookings = requests.get("http://localhost:5005/booking/{}".format(id))
    except:
        raise ServiceUnavailable("The bookings service is unavailable")

    if users_bookings.status_code == 404:
        raise NotFound("No bookings were found for ".format(id))

    #just a dictionary
    users_bookings = users_bookings.json()

    # For each booking, get the rating and the movie title
    result = {}
    for date, movies in users_bookings['User'].items():
        result[date] = []
        for movieid in movies:
            print(movieid)
            try:
                movies_resp = requests.get("http://localhost:5000/movies/{}".format(movieid))

            except:
                raise ServiceUnavailable("The Movie service is unavailable.")

            movies_resp = movies_resp.json()
            print(movies_resp['Movie']['Title'])
            result[date].append({
                    'Title': movies_resp['Movie']['Title'],
                    'rating': movies_resp['Movie']['Raiting']
            })

                #     return {
                #  self.date_id :
                #   [i.id for i in self.movie_booking]
                 #
                #   }



    #return nice_json(users_bookings)
    return nice_json(result)
    #print (users_bookings)
    #print (users_bookings.json())
    #return 'ok'



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
