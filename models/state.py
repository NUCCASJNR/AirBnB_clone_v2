#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship
from models import storage


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state', cascade='all, delete')

    @property
    def cities(self):
        """
        Getter attribute that returns the list of City
        instances with state_id equals to the current State.id.
        """

        city_objs = storage.all(City)
        return [city_obj for city_obj in city_objs.values() if 
        city_obj.state_id == self.id]
