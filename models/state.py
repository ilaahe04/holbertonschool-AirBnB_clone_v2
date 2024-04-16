#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models import storage


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            """Get a list of all related City objects."""
            citiess = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    citiess.append(city)
            return citiess
