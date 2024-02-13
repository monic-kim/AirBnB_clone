#!/usr/bin/python3'''creates a User class'''
from models.base_model import BaseModel


class City(BaseModel):
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        '''initializes attributes for th city class'''
        super().__init__(*args, **kwargs)
