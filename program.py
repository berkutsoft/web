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
        for order in session.query(Order).limit(orders):
            order.state=1
        session.commit()

    else:
        for i, order in enumerate(session.query(Order).yield_per(100)):
            if i >= orders:
                break
            if not i % 50000:
                session.commit()
            if order.state == 1:
                continue
            order.state = 1
        session.commit()


db_engine = create_engine('mysql+mysqldb://root:pass@localhost/DB', echo=False)
Base.metadata.create_all(db_engine)
Session = sessionmaker(bind=db_engine)
session = Session()

count = session.query(Order).count()
rnd = random.randrange(0,count)

mark_random_orders_accepted(rnd)
