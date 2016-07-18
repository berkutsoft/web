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
    for i, order in enumerate(orders.query(Order).yield_per(100)):
        order.state = 1
        if not i % 1000: #коммит каждые 1000 записей
            orders.commit()
        if rnd==0:break # если мы уже поменяли необходимое количество записей то выходим из цикла
        rnd-=1
    orders.commit()
    return session.query(Order).filter(Order.state == 1).count()

db_engine = create_engine('mysql+mysqldb://root:pass@localhost/DB', echo=False)
Base.metadata.create_all(db_engine)
Session = sessionmaker(bind=db_engine)
session = Session()

# Ищем все заказы со статусом hold = 0
findHold = session.query(Order).filter(Order.state == 0).yield_per(100)

# функция установки рандомного количества записей в accepted 
mark_random_orders_accepted(session)
