#!/usr/bin/python3
'''module cetes Review class'''
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    usser_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
