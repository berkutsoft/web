#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Unicode, BigInteger

Base = declarative_base()


class Order(Base):

    __tablename__ = 'orders'

    id = Column(BigInteger, nullable=False, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    # accepted = 1, hold = 0
    state = Column(Integer, nullable=False, index=True)

    def __init__(self, name, state):
        self.name = name
        self.state = state

    def __repr__(self):
        return "Name: '%s'" % (self.name)


db_engine = create_engine('mysql+mysqldb://root:pass@localhost/DB', echo=False)
Base.metadata.create_all(db_engine)
Session = sessionmaker(bind=db_engine)
session = Session()


def mark_random_orders_accepted(num):
    c = 0
    while c < num:
        q = session.query(Order).filter(Order.state == 0).yield_per(100)
        for order in q:
            order.state = 1
            c += 1
    session.commit()

if __name__ == "__main__":
    mark_random_orders_accepted(20000)
