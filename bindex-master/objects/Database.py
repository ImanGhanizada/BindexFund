from Utilities import Utilities
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

util = Utilities()
db_session = util.SQLSession()

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import Models.User
    import Models.Price
    Base.metadata.create_all(bind=engine)
