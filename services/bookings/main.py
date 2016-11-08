from settings import app, db, manager
from models import Movies, User, Dates
from bookings import *

if __name__ == '__main__':
    #app.run()
    manager.run()
