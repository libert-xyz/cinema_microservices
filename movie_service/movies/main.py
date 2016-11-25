from settings import app, db, manager
from models import Movies
from movies import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
    #app.run()
    #manager.run()
