from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Unicode, BigInteger
from sqlalchemy import exc

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


db_engine = create_engine('mysql+mysqldb://root:pass@localhost/DB', echo=False)

Base.metadata.create_all(db_engine)
Session = sessionmaker(bind=db_engine)
session = Session()


findHold = session.query(Order).filter(Order.state == 0).yield_per(100)

#for result in findHold:
#    print result

try:
    session.commit()
except exc.SQLAlchemyError, e:
    session.rollback()

