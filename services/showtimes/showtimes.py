from settings import app,db
from models import Movies,Dates
import json
from flask import jsonify, request,make_response,abort


@app.route('/showtimes',methods=['GET'])
def showtimes_llist():
    if request.method == 'GET':
        #d = Dates.query.filter_by(id=3).first().showtime
        show = Dates.query.all()
        #return jsonify(Movies = [i.serialize for i in movies])
        #d = Dates.query.filter_by(id=i.id).first().showtime
        return jsonify(Showtimes = [i.serialize for i in show])
        #return ([Dates.query.filter_by(id=i.id).first().showtime for i in Dates.query.all()])



        #return jsonify(Showtimes = [i.serialize for i in show])

# @app.route('/showtimes/<int:id>', methods=['GET'])
# def get_movie(id):
#
#     try:
#          showtime = Showtimes.query.filter_by(id=id).one()
#          return jsonify(User = user.serialize)
#     except:
#         abort(404)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
