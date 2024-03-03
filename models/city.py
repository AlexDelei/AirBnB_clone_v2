#!/usr/bin/python3
""" City Module for HBNB project """
import os
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


class City(BaseModel):
    """City class handles all application cities"""
    if STORAGE_TYPE == 'db':
        __tablename__ = 'cities'
        id = Column(String(60), primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)


state = relationship("State", back_populates='cities')
