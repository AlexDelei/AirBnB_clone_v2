#!/usr/bin/python3
"""
Database Storage
"""
import os
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from models.amenity import Amenity


class DBStorage:
    """
      Long-type of storage
      logic implementation of it
    """
    CNC = {
            'Amenity': Amenity,
            'City': City,
            'Place': Place,
            'Review': Review,
            'State': State,
            'User': User
            }
    """
    db storage
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        create the db engine
        and connect to it
        """
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format
                (
                    os.environ.get('HBNB_MYSQL_USER'),
                    os.environ.get('HBNB_MYSQL_PWD'),
                    os.environ.get('HBNB_MYSQL_HOST'),
                    os.environ.get('HBNB_MYSQL_DB')),
                pool_pre_ping=True)

        if os.environ.get("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            returns a dictionary of all
            objects
        """
        obj_d = {}
        if cls:
            all_query = self.__session.query(cls).all()
        else:
            all_query = []
            for cls_name, cls_model in self.CNC.items():
                all_query.extend(self.__session.query(cls_model).all())
        for obj in all_query:
            obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
            obj_d[obj_ref] = obj
        return obj_d

    def new(self, obj):
        """
         adds objects to current db session
        """
        self.__session.add(obj)

    def save(self):
        """
            commis all chenges of db session
        """
        self.__session.commit()

    def rollback_session(self):
        """
            re dos the execution in case of an
            exception
        """
        self.__session.rollback()

    def delete(self, obj=None):
        """
            deletes obj from current db session
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def delete_all(self):
        """
            deletes everything
        """
        for i in DBStorage.CNC.values():
            a_query = self.__session.query(i)
            all_objs = [obj for obj in a_query]
            for j in range(len(all_objs)):
                to_del = all_objs.pop(0)
                to_del.delete()
        self.save()

    def reload(self):
        """
            creates all table in db and session from engine
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
                sessionmaker(
                    bind=self.__engine,
                    expire_on_commit=False))

    def close(self):
        """
            calls remove() on private sessino attribute self.session
        """
        self.__session.remove()

    def get(self, cls, id):
        """
            Retrieves one object based on class name and id
        """
        if cls and id:
            fetch = "{}.{}".format(cls.__name__, id)
            all_objects = self.all(cls)
            for k, v in all_objects.items():
                if k == fetch:
                    return all_objects[k]
        return None

    def count(self, cls=None):
        """
            return the count of all objects in a storage
        """
        return (len(self.all(cls)))
