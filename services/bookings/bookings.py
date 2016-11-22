from settings import app,db
from models import Movies,Booking
import json
from flask import jsonify, request,make_response,abort


@app.route('/booking',methods=['GET'])
def movies():
    if request.method == 'GET':
        #u = User.query.all()
        b = Booking.query.all()

        return jsonify(Bookings = [i.serialize for i in b])
        #return jsonify(Movies = [i.serialize for i in movies])

@app.route('/booking/<int:id>', methods=['GET'])
def get_user(id):

    try:
         #user = User.query.filter_by(id=id).one()
         user = Booking.query.filter_by(user_id=id)

         #return jsonify(User = user.serialize_user)
         return jsonify(User = [i.serialize_user for i in user])

    except:
        abort(404)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
