#!/usr/bin/python3
'''this module creates amenity class'''
from models.base_model immport BaseModel


class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kargs):
        '''initialize attributes for amenity clss'''
        super().__init__(*args, **kwargs)
