#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

import models
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
                'City',
                cascade="all, delete, delete-orphan",
                backref='state'
                )
    else:
        @property
        def cities(self):
            '''returns list of city instances for the current state.'''
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
