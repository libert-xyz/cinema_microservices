from settings import app,db
from models import User
import json
from flask import jsonify, request,make_response,abort


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

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
