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
        id = Column(String(60), primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)


cities = relationship("City", back_populates="state", cascade="delete")
