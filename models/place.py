#!/usr/bin/python3
""" Place Module for HBNB project """
import os
import models
from .base_model import BaseModel
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Float
from sqlalchemy.orm import relationship
from sqlalchemy import Table
from .base_model import Base
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


place_amenity = Table(
     'place_amenity', Base.metadata,
     Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
     Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)
    
    if STORAGE_TYPE != 'db':
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
        review_ids = []

        @property
        def reviews(self):
            """"
            returning a list of reviews to self
            """
            if len(self.review_ids) > 0:
                return review_ids
            else:
                return None

        @reviews.setter
        def reviews(self, review_obj):
            """
                setter for review_ids
            """
            if amenity_obj and amenity_obj not in self.amenity_ids:
                self.amenity_ids.append(amenity_obj.id)

        @property
        def amenities(self):
            """Getter attribute for amenities"""
            amenity_objs = []
            for amenity_id in self.amenity_ids:
                amenity_objs.append(models.storage.all(Amenity).get(amenity_id))
            return amenity_objs

        @amenities.setter
        def amenities(self, obj):
            """Setter attribute for amenities"""
            if isinstance(obj, Amenity):
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)


reviews = relationship("Review", backref="reviewing", cascade="delete")
user = relationship("User", backref="places")
