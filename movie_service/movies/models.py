from settings import db

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
      'Raiting': self.rating,
      'id' : self.id
      }
