#!/usr/bin/python3
"""Module Class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""