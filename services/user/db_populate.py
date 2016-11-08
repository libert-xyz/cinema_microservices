from models import User
from settings import db




# m = User(name='Rodrigo Schmidt')
# m.email='rschmidt@nuvops.com'
# db.session.add(m)
# db.session.commit()

m1 = User(name='Reeses Peche')
m1.email='reeses@nsa.gov'
db.session.add(m1)
db.session.commit()


m2 = User(name='Zarya Decker')
m2.email='zd@aol.com'
db.session.add(m2)
db.session.commit()

print ('Done..')
