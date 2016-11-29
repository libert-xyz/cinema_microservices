from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moviesdb.db'
db = SQLAlchemy(app)


user_service = 'http://0.0.0.0:5001/user'
booking_service = 'http://0.0.0.0:5003/booking'
showtime_service = 'http://0.0.0.0:5002/mv/add'

server = Server(host="0.0.0.0", port=5000)

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('run', server)
