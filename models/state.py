#!/usr/bin/python3
"""the Defination of the state class of the user"""
from models.base_model import BaseModel


class State(BaseModel):
    """the whole Rep a state class

    Attributes:
        name (str): the state neme of the user
    """

    name = ""
