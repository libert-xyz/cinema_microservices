from settings import app, db, manager
from models import Dates,Movies
from showtimes import *

if __name__ == '__main__':
    #app.run()
    manager.run()
