#!/usr/bin/python3
"""This module defines a class User"""

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = "user"
    if getenv("HBTN_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
