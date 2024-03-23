#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.file_storage import FileStorage
from models.engine import db_storage


if os.environ.get("HBNB_TYPE_STORAGE") == 'db':
    storage = db_storage.DBStorage()
else:
    storage = FileStorage()

storage.reload()
