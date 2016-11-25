from settings import app, db, manager
from models import User
from user import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
    #app.run()
    #manager.run()
