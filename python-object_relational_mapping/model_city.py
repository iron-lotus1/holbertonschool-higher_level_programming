#!/usr/bin/python3
"""
Module that defines the City class using SQLAlchemy,
inheriting from Base imported from model_state.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    City class that links to the MySQL table 'cities'.

    Attributes:
        __tablename__ (str): The name of the table in MySQL.
        id (int): The city's unique identifier (Primary Key).
        name (str): The city's name (up to 128 characters).
        state_id (int): The id of the state the city belongs to (Foreign Key).
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
