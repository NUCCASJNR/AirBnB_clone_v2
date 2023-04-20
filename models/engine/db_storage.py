#!/usr/bin/python3
"""creating a new engine"""

from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("OHBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, passwd, host, db), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls is None:
            lists = [list for cls in classes.values() for list in self.__session.quer    y(cls).all()]
       else:
            lists = self.__session.query(cls).all()

        obj_dict = {}
        for list in lists:
            key = f"{list.__class__.__name__}.{list.id}"
            obj_dict[key] = list


