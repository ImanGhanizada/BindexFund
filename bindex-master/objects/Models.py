from sqlalchemy import Column, Integer, String
from sqlalchemy.inspection import inspect

from Database import db_session, Base

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=False)
    email = Column(String(255), unique=False)

    def __init__(self, username=None, email=None):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.username)

class Price(Base):
    __tablename__ = 'Price'
    id = Column(Integer, primary_key=True)
    date = Column(String(255), unique=False)
    symbol = Column(String(255), unique=False)
    name = Column(String(255), unique=False)
    price = Column(String(255), unique=False)
    change = Column(String(255), unique=False)
    market_cap = Column(String(255), unique=False)

    def __init__(self, date=None, symbol=None, name=None, price=None, change=None, market_cap=None):
        self.date = date
        self.symbol = symbol
        self.name = name
        self.price = price
        self.change = change
        self.market_cap = market_cap

    def serialize(self):
        d = Serializer.serialize(self)
        return d

    def __repr__(self):
        return '<Name %r>' % (self.name)

class Funds(Base):
    __tablename__ = 'Funds'
    id = Column(Integer, primary_key=True)
    symbol = Column(String(255), unique=False)
    percent = Column(String(11), unique=False)
    fund = Column(String(255), unique=False)
    description = Column(String(6000), unique=False)
    selection = Column(String(6000), unique=False)

    def __init__(self, symbol=None, percent=None, fund=None, description=None, selection=None):
        self.symbol = symbol
        self.percent = percent
        self.fund = fund
        self.description = description
        self.selection = selection

    def __repr__(self):
        return '<Symbol %r>' % (self.symbol)
