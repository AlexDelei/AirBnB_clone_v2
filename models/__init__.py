#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.file_storage import FileStorage
from models.engine import db_storage


storage = FileStorage()
storage.reload()
