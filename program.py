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
    if orders < 100:
        q =  session.query(Order).filter(Order.state == 0).limit(orders):
    else:
        q = session.query(Order).filter(Order.state == 0).limit(orders).yield_per(100)
    for order in q:
            order.state = 1
    session.commit()


db_engine = create_engine('mysql+mysqldb://root:pass@localhost/DB', echo=False)
Base.metadata.create_all(db_engine)
Session = sessionmaker(bind=db_engine)
session = Session()

count = session.query(Order).count()
rnd = random.randrange(0,count)

mark_random_orders_accepted(rnd)
