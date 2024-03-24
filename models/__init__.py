#!/usr/bin/python3
"""__init__ the magic method for packages"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
