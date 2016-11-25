from settings import app, db, manager
from models import Dates,Movies
from showtimes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5002)

    #app.run()
    #manager.run()
