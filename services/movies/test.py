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
        self.url = 'http://localhost:5000/movies'


    def tearDown(self):
        db.session.remove()
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

        response = tester.get('/movies')

        #response = requests.get("{}".format(self.url))
        #response = response.json()


        print(response.data)
        #self.assertIn(b'FightClub',response.data)
        self.assertEqual(b'{\n  "Movies": [\n    {\n      "Raiting": 2, \n      "Title": "Dragon Ball", \n      "id": 1\n    }, \n    {\n      "Raiting": 10, \n      "Title": "FightClub", \n      "id": 2\n    }\n  ]\n}\n',
        response.data)
        #self.asserEqual(b"{'id': 4, 'Raiting': 10, 'Title': 'FightClub'}",response['Movies'][3])

    def test_movies_id(self):
        tester = app.test_client(self)

        m2 = Movies(title='Dragon Ball')
        m2.rating=2
        db.session.add(m2)
        db.session.commit()

        response = tester.get('/movies/1')
        print(response.data)
        self.assertIn(b'Dragon Ball',response.data)

    def test_movies_post(self):
        tester = app.test_client(self)

        response = tester.post('/movies?title=DragonBall&rating=4')
        print (response.data)
        self.assertIn(b'DragonBall',response.data)


    def test_movies_put(self):
        tester = app.test_client(self)
        m = Movies(title='Dragon Ball')
        m.rating = 5
        db.session.add(m)
        db.session.commit()

        response = tester.put('/movies/1?title=Pokemon')
        print (response.data)
        self.assertIn(b'Pokemon',response.data)


    def test_movies_delete(self):
        tester = app.test_client(self)
        m = Movies(title='Dragon Ball')
        m.rating = 2
        db.session.add(m)
        db.session.commit()

        response = tester.delete('/movies/1')
        print(response.data)
        self.assertIn(b'Movie Deleted',response.data)



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
