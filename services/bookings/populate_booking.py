from models import Movies,Dates,showtime, User
from settings import db
from datetime import date



##########User##############

m = User(name='Rodrigo Schmidt')
m.email='rschmidt@nuvops.com'
db.session.add(m)
db.session.commit()

m1 = User(name='Reeses Peche')
m1.email='reeses@nsa.gov'
db.session.add(m1)
db.session.commit()


m2 = User(name='Zarya Decker')
m2.email='zd@aol.com'
db.session.add(m2)
db.session.commit()


######Movies###################

m = Movies(title='Titanic')
m.rating=9
db.session.add(m)
db.session.commit()

m2 = Movies(title='Dragon Ball')
m2.rating=2
db.session.add(m2)
db.session.commit()


m3 = Movies(title='FightClub')
m3.rating=10
db.session.add(m3)
db.session.commit()

m4 = Movies(title='Batman')
m4.rating=5
db.session.add(m4)
db.session.commit()

###############DATES#######################

d = Dates(date=date(2016, 11, 7))
d.user_id=1
d.showtime.append(m)
d.showtime.append(m4)
db.session.add(d)
db.session.commit()

d1 = Dates(date=date(2016, 11, 8))
d1.user_id=1
d1.showtime.append(m)
d1.showtime.append(m4)
d1.showtime.append(m3)
db.session.add(d1)
db.session.commit()


d2 = Dates(date=date(2016, 11, 9))
d2.user_id=3
d2.showtime.append(m)
d2.showtime.append(m2)
d2.showtime.append(m3)
d2.showtime.append(m4)
db.session.add(d2)
db.session.commit()



d3 = Dates(date=date(2016, 11, 10))
d3.user_id=2
d3.showtime.append(m2)
d3.showtime.append(m3)
db.session.add(d3)
db.session.commit()


d4 = Dates(date=date(2016, 11, 11))
d4.user_id=3
d4.showtime.append(m2)
d4.showtime.append(m4)
d4.showtime.append(m3)
db.session.add(d4)
db.session.commit()

d5 = Dates(date=date(2016, 11, 15))
d5.user_id=3
d5.showtime.append(m2)
d5.showtime.append(m4)
d5.showtime.append(m3)
db.session.add(d4)
db.session.commit()

d6 = Dates(date=date(2016, 11, 15))
d6.user_id=1
d6.showtime.append(m4)
db.session.add(d4)
db.session.commit()



print ('Done creation..')
