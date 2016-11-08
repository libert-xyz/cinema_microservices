from settings import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100),unique=True)
    booking = db.relationship('Dates', backref='user',lazy='dynamic')

    def __init__(self,name):
        self.name = name


    def __repr__(self):
        return '<Name: %r>' %self.name


    @property
    def serialize(self):
        return {
      'Name': self.name,
      'email': self.email,
      'id' : self.id
      }


class Movies(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200))
    rating = db.Column(db.Integer)


    def __init__(self,title):
        self.title = title

    def __repr__(self):
        return '<Title %r>' %self.title

    @property
    def serialize(self):
        return {
      'Title': self.title,
      }

showtime = db.Table('showtime',
            db.Column('movie_id',db.Integer, db.ForeignKey('movies.id')),
            db.Column('date_id',db.Integer, db.ForeignKey('dates.id'))
                )

class Dates(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.DateTime)
    showtime = db.relationship('Movies', secondary=showtime,
        backref=db.backref('dates', lazy='dynamic'))


    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __init__(self,date):
        self.date = date


    def __repr__(self):
        return '<Date: %r>' %self.date

    @property
    def serialize(self):
        #d = Dates.query.filter_by(id=i.id).first().showtime
        return {
      str(self.date) :
      [i.title for i in self.showtime]
      }
