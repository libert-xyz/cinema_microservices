from settings import app, db, manager
from models import Movies
from movies import *

if __name__ == '__main__':
    #app.run()
    manager.run()
