#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, Integer, Float, ForeignKey, String, Table
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
import models

#place_amenity = Table(
#    'place_amenity',
#    Base.metadata,
#    Column(
#        'place_id',
#        String(60),
#        ForeignKey('places.id'),
#        primary_key=True,
#        nullable=False,
#    ),
#    Column(
#        'amenity_id',
#        ForeignKey('amenities.id'),
#        primary_key=True,
#        nullable=False,
#    ),
#    mysql_charset="latin1",
#)


class Place(BaseModel, Base):
    """ A place to stay """
    if models.storage_t == 'db':
        __tablename__ = 'places'

        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer(), nullable=False, default=0)
        number_bathrooms = Column(Integer(), nullable=False, default=0)
        max_guest = Column(Integer(), nullable=False, default=0)
        price_by_night = Column(Integer(), nullable=False, default=0)
        latitude = Column(Float(), nullable=True)
        longitude = Column(Float(), nullable=True)
        amenity_ids = []

        reviews = relationship(
                "Review",
                cascade="all, delete, delete-orphan",
                backref="place"
                )

        #amenities = relationship(
        #        "Amenity",
        #        secondary=place_amenity,
        #        viewonly=False,
        #        cascade="all, delete, delete-orphan",
        #        backref="place_amenities"
        #        )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            '''returns list of review instances for the current place.'''
            revs = []
            for key, val in models.storage.all(Review).items():
                if val.place_id == self.id:
                    revs.append(val)
            return revs
                    
        @property
        def amenities(self):
            '''returns list of amenity instances for the current place.'''
            return self.amenity_ids
        
        @amenities.setter
        def amenities(self, value=None):
            """appends amenity id to the attribute 'amenity_ids'"""
            if type(value).__name__ == 'Amenity' and value.id not in self.amenity_ids:
                self.amenity_ids.append(value.id)
