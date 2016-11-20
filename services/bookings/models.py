from settings import db

movie_booking = db.Table('movie_booking',
            db.Column('movie_id',db.Integer, db.ForeignKey('movies.id')),
            db.Column('booking_id',db.Integer, db.ForeignKey('booking.id'))
                )


class Booking(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # date_id = db.Column(db.Integer, db.ForeignKey('dates.id'))
    user_id = db.Column(db.Integer)
    date_id = db.Column(db.Integer)
    movie_booking = db.relationship('Movies', secondary=movie_booking,
        backref=db.backref('booking', lazy='dynamic'))


    @property
    def serialize(self):
        #d = Dates.query.filter_by(id=i.id).first().showtime
        return {
     'id' : self.user_id ,
     'date' : self.date_id ,
      'Movies':
      [i.id for i in self.movie_booking]
      }

    @property
    def serialize_user(self):
        #d = Dates.query.filter_by(id=i.id).first().showtime
        return {
     self.date_id :
      [i.id for i in self.movie_booking]

      }

class Movies(db.Model):
    id = db.Column(db.Integer,primary_key=True)

    def __init__(self,id):
        self.id = id

    # def __repr__(self):
    #     return '<Title %r>' %self.title

    # @property
    # def serialize(self):
    #     return {
    #   'Title': self.title,
    #   }

    # @property
    # def serialize(self):
    #     #d = Dates.query.filter_by(id=i.id).first().showtime
    #     return {
    #   str(self.date) :
    #   [i.title for i in self.showtime]
    #   }
