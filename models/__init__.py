#!/usr/bin/python3
"""this is the __init__ method for models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
