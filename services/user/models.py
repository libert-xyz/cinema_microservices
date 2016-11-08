from settings import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100),unique=True)


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
