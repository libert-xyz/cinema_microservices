from settings import app, db, manager
from models import Movies, Booking
from bookings import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5003)
    #app.run()
    manager.run()
