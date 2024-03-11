#!/usr/bin/python3
"""Defines the state class of the user"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state class

    Attributes:
        name (str): the state neme of the user
    """

    name = ""
