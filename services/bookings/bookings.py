from settings import app,db
from models import Movies,Dates,User
import json
from flask import jsonify, request,make_response,abort


@app.route('/booking',methods=['GET'])
def movies():
    if request.method == 'GET':
        return 'OK'
        #return jsonify(Movies = [i.serialize for i in movies])
        #return jsonify(Movies = [i.serialize for i in movies])



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
