#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from os import getenv

STO_TYP = getenv('HBNB_TYPE_STORAGE')

class Amenity(BaseModel, Base):
    '''Amenity class'''
    if STO_TYP == "db":
        from models.place import association_table
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=association_table)
    else:
        name = ''
