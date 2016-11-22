import unittest
import requests
import main
#import db,app
from settings import app, db
import sqlalchemy
from models import Movies


class TestMoviesService(unittest.TestCase):


    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        db.create_all()
        self.app = app.test_client()
        self.url = 'http://localhost://127.0.0.1/movies'


    def tearDown(self):
        #db.session.remove()
        db.drop_all()

    def test_MoviesAll(self):

        tester = app.test_client(self)

        m2 = Movies(title='Dragon Ball')
        m2.rating=2
        db.session.add(m2)
        db.session.commit()


        m3 = Movies(title='FightClub')
        m3.rating=10
        db.session.add(m3)
        db.session.commit()

        #response = tester.get('http://localhost://127.0.0.1/movies')
        response = tester.get('/movies')

        print(response.data)
        self.assertIn(b'FightClub',response.data)



GOOD_RESPONSES = {
  "Movies": [
    {
      "Raiting": 10,
      "Title": "Titanic",
      "id": 1
    },
    {
      "Raiting": 6,
      "Title": "American Pie",
      "id": 2
    },
    {
      "Raiting": 2,
      "Title": "Dragon Ball",
      "id": 3
    },
    {
      "Raiting": 10,
      "Title": "FightClub",
      "id": 4
    },
    {
      "Raiting": 5,
      "Title": "Batman",
      "id": 5
    }
  ]
}

if __name__ == '__main__':
    unittest.main()
