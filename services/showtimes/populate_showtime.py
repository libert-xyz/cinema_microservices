from models import Movies,Dates,showtime
from settings import db
from datetime import date


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
d.showtime.append(m)
d.showtime.append(m4)
db.session.add(d)
db.session.commit()

d1 = Dates(date=date(2016, 11, 8))
d1.showtime.append(m)
d1.showtime.append(m4)
d1.showtime.append(m3)
db.session.add(d1)
db.session.commit()


d2 = Dates(date=date(2016, 11, 9))
d2.showtime.append(m)
d2.showtime.append(m2)
d2.showtime.append(m3)
d2.showtime.append(m4)
db.session.add(d2)
db.session.commit()



d3 = Dates(date=date(2016, 11, 10))
d3.showtime.append(m2)
d3.showtime.append(m3)
db.session.add(d3)
db.session.commit()


d4 = Dates(date=date(2016, 11, 11))
d4.showtime.append(m2)
d4.showtime.append(m4)
d4.showtime.append(m3)
db.session.add(d4)
db.session.commit()



print ('Done creation..')
