from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///showtimes.db'
db = SQLAlchemy(app)

server = Server(host="localhost", port=5002)


movie_service = 'http://0.0.0.0:5000/movies'
user_service = 'http://0.0.0.0:5001/user'
booking_service = 'http://0.0.0.0:5003/booking'

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('run', server)
