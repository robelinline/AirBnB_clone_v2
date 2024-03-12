#!/usr/bin/python3
"""the defenation of the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """the total Represention a review

    Attributes:
        place_id (str): place id
        user_id (str): user id
        text (str): comment of the review
    """

    place_id = ""
    user_id = ""
    text = ""
