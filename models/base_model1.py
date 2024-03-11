#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from datetime import datetime, timezone
import uuid


class BaseModel:
    """Base class for all AirBnB objects.

    Provides common attributes (id, created_at, updated_at) and methods
    for serialization, deserialization, and attribute access.
    """

    def __init__(self):
        """
        Initializes the object with a unique ID, creation time, and update time.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(timezone.utc).isoformat()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the object in the format:
        [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now(timezone.utc).isoformat()

    def to_dict(self):
        """
        Returns a dictionary containing all key-value pairs of the object's attributes.

        Includes the class name as a key and converts created_at and updated_at to ISO format.
        Only returns instance attributes (excluding those starting with '_').
        """
        return {
            "__class__": self.__class__.__name__,
            **{key: value.isoformat() if isinstance(value, datetime) else value
               for key, value in self.__dict__.items() if not key.startswith("_")}
        }
