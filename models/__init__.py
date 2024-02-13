#!/usr/bin/python3
'''intializes the package'''
#from models.base_model import BaseModel
from models.engine import file_sorage

storage = file_storage.FileStorage()
storage.reload()
