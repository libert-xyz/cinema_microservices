from models import Movies, Booking
from settings import db
from datetime import date



##########User##############

# m = User(id=1)
# db.session.add(m)
# db.session.commit()
#
# m1 = User(id=2)
# db.session.add(m1)
# db.session.commit()
#
#
# m2 = User(id=3)
# db.session.add(m2)
# db.session.commit()


######Movies###################

m = Movies(id=1)
db.session.add(m)
db.session.commit()

m2 = Movies(id=2)
db.session.add(m2)
db.session.commit()


m3 = Movies(id=3)
db.session.add(m3)
db.session.commit()

m4 = Movies(id=4)
db.session.add(m4)
db.session.commit()

###############DATES#######################

# d = Dates(id=1)
# db.session.add(d)
# db.session.commit()
#
# d1 = Dates(id=2)
# db.session.add(d1)
# db.session.commit()
#
#
# d2 = Dates(id=3)
# db.session.add(d2)
# db.session.commit()
#
#
#
# d3 = Dates(id=4)
# db.session.add(d3)
# db.session.commit()
#
#
# d6 = Dates(id=5)
# db.session.add(d4)
# db.session.commit()

###############BOOKING#######################


b = Booking(user_id=1)
b.date_id=1
b.movie_booking.append(m)
db.session.add(b)
db.session.commit()


b1 = Booking(user_id=2)
b1.date_id=1
b1.movie_booking.append(m)
b1.movie_booking.append(m2)
db.session.add(b1)
db.session.commit()


b2 = Booking(user_id=3)
b2.date_id=2
b2.movie_booking.append(m3)
b2.movie_booking.append(m4)
db.session.add(b2)
db.session.commit()



print ('Done creation Booking..')
