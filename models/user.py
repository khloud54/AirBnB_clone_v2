#!/usr/bin/python3
"""
Module for user class

"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    base model class

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
