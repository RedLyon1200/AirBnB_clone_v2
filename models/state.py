#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if models.storage_type == 'db':
        name = Column(
            String(128),
            nullable=False
        )
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if models.storage_type == 'fs':
        @property
        def cities(self):
            """return the list of City objects from storage
            linked to the current State """
            city_list = []
            cities = models.storage.all(City)

            for city in cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
