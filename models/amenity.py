#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.place import association_table

class Amenity(BaseModel, Base):
    """ Amenity: Class"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=association_table, viewonly=False)

    def __init__(self, *args, **kwargs):
        """
            Init for inherited
        """
        super().__init__(*args, **kwargs)
