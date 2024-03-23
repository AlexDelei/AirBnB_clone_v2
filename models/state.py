#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy.orm import relationship
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    if STORAGE_TYPE == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="states", cascade="delete")
    else:
        name = ''

        @property
        def list_cities(self):
            """
            returns a list of Cities which are related
            to this state
            """
            temp = []
            for city in models.storage.all("City").values():
                # only instances with the current state id
                if city.state_id == self.id:
                    temp.append(city)
            return temp
