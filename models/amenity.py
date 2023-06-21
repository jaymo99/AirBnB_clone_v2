#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel

from models.base_model import BaseModel, Base
from models.place import place_amenity


class Amenity(BaseModel, Base):
    '''represents an amenity for a place.'''
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    place_amenities = relationship(
            "Place",
            secondary=place_amenity
            )
