from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Unicode, BigInteger
from sqlalchemy import exc
import random

Base = declarative_base()

class Order(Base):

    __tablename__ = 'orders'

    id = Column(BigInteger, nullable=False, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    state = Column(Integer, nullable=False, index=True)   # accepted = 1, hold = 0

    def __init__(self, name, state):
        self.name  = name
        self.state = state

    def __repr__(self):
        return "Name: '%s'" % (self.name)

def mark_random_orders_accepted(orders):
    count = orders.query(Order).count()
    rnd = random.randrange(0,count)
    print rnd
    for i, order in enumerate(orders.query(Order).yield_per(100)):
        if rnd==0:break

        order.state = 1
        if not i % 1000:
            print i
            orders.commit()
            #orders.close()
        #print "id", i, "name", order.name
        rnd-=1
    print rnd
    orders.commit()

db_engine = create_engine('mysql+mysqldb://root:1011@localhost/DB', echo=False)

Base.metadata.create_all(db_engine)
Session = sessionmaker(bind=db_engine)
session = Session()


#findHold = session.query(Order).filter(Order.state == 0).yield_per(100)
findHold = session.query(Order).yield_per(100)
mark_random_orders_accepted(session)
#for result in findHold:
#    print result

try:
    session.commit()
except exc.SQLAlchemyError, e:
    session.rollback()

