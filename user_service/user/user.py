from settings import app,db,nice_json
from models import User
import json
from flask import jsonify, request,make_response,abort
from werkzeug.exceptions import NotFound, ServiceUnavailable
import requests

@app.route('/user',methods=['GET'])
def users():
    if request.method == 'GET':
        users = User.query.all()
        return jsonify(Users = [i.serialize for i in users])

@app.route('/user',methods=['POST'])
def add_user():
    name = request.args.get('name','')
    email = request.args.get('email','')
    if name == '' or email == '':
        abort(400)

    if User.query.filter_by(email=email).first() is not None:
        return jsonify({"message":"user alaredy exists"}), 200

    user = User(name=name)
    user.email = email
    db.session.add(user)
    db.session.commit()

    return jsonify({'User': user.name,'Email': user.email, 'id': user.id})



@app.route('/user/<int:id>', methods=['GET','PUT','DELETE'])
def get_user(id):


    try:
         user = User.query.filter_by(id=id).one()
         if request.method == 'GET':
             return jsonify(User = user.serialize)
         elif request.method == 'PUT':
            name = request.args.get('name','')
            email = request.args.get('email','')
            if name:
                user.name = name
            if email:
                user.email = email

            db.session.add(user)
            db.session.commit()
            return jsonify({'User': user.name,'Email': user.email, 'id': user.id})

         elif request.method == 'DELETE':
            db.session.delete(user)
            db.session.commit()
            return 'User Deleted'
    except:
        abort(404)



@app.route('/user/<int:id>/booking',methods=['GET'])
def get_booking(id):
    try:
        users_bookings = requests.get("http://localhost:5003/booking/{}".format(id))
    except:
        raise ServiceUnavailable("The bookings service is unavailable")

    if users_bookings.status_code == 404:
        raise NotFound("No bookings were found for ".format(id))

    #just a dictionary
    users_bookings = users_bookings.json()

    # For each booking, get the rating and the movie title
    result = {}
    print (users_bookings)
    for l in users_bookings['User']:
        for date,movies in l.items():
            date_resp = requests.get("http://localhost:5002/showtimes/{}".format(date))
            date_resp = date_resp.json()
            date_resp = date_resp.popitem()[0]
            #print (date_resp.popitem()[0])
            result[date_resp] = []
            for movieid in movies:
                print(movieid)
                try:
                    movies_resp = requests.get("http://localhost:5000/movies/{}".format(movieid))

                except:
                    raise ServiceUnavailable("The Movie service is unavailable.")

                movies_resp = movies_resp.json()
                print(movies_resp['Movie']['Title'])
                result[date_resp].append({
                        'Title': movies_resp['Movie']['Title'],
                        'rating': movies_resp['Movie']['Raiting']
                })

    return nice_json(result)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
