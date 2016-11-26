from models import Movies,Dates,showtime
from settings import db
from datetime import date,datetime
import pytz



######Movies###################

# m = Movies(title='Titanic')
# m.rating=9
# db.session.add(m)
# db.session.commit()
#
# m2 = Movies(title='Dragon Ball')
# m2.rating=2
# db.session.add(m2)
# db.session.commit()
#
#
# m3 = Movies(title='FightClub')
# m3.rating=10
# db.session.add(m3)
# db.session.commit()
#
# m4 = Movies(title='Batman')
# m4.rating=5
# db.session.add(m4)
# db.session.commit()


######Movies###################

m = Movies(id=1)
db.session.add(m)
db.session.commit()

m2 = Movies(id=3)
db.session.add(m2)
db.session.commit()


m3 = Movies(id=4)
db.session.add(m3)
db.session.commit()

m4 = Movies(id=5)
db.session.add(m4)
db.session.commit()


###############DATES#######################

d = Dates(date=datetime(2016, 11, 7,12,30,tzinfo=pytz.timezone('US/Eastern')))
d.showtime.append(m)
d.showtime.append(m4)
db.session.add(d)
db.session.commit()

d1 = Dates(date=datetime(2016, 11, 8,12,30,tzinfo=pytz.timezone('US/Eastern')))
d1.showtime.append(m)
d1.showtime.append(m4)
d1.showtime.append(m3)
db.session.add(d1)
db.session.commit()


d2 = Dates(date=datetime(2016, 11, 9,13,45,tzinfo=pytz.timezone('US/Eastern')))
d2.showtime.append(m)
d2.showtime.append(m2)
d2.showtime.append(m3)
d2.showtime.append(m4)
db.session.add(d2)
db.session.commit()



d3 = Dates(date=datetime(2016, 11, 10,9,tzinfo=pytz.timezone('US/Eastern')))
d3.showtime.append(m2)
d3.showtime.append(m3)
db.session.add(d3)
db.session.commit()

d5 = Dates(date=datetime(2016, 11, 10,16,30,tzinfo=pytz.timezone('US/Eastern')))
d5.showtime.append(m)
d5.showtime.append(m3)
db.session.add(d5)
db.session.commit()


d4 = Dates(date=datetime(2016, 11, 11,12,tzinfo=pytz.timezone('US/Eastern')))
d4.showtime.append(m2)
d4.showtime.append(m4)
d4.showtime.append(m3)
db.session.add(d4)
db.session.commit()



print ('Done creation..')
