from models import Movies
from settings import db




# m = Movies(title=i)
# m.rating=movies[i]
# db.session.add(m)
# db.session.commit()

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




print ('Done..')
