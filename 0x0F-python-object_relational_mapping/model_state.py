#!/usr/bin/python3
"""
Defines the City model for the cities table in the database.

This script defines a SQLAlchemy model for the City class, which represents
the cities table in the database. It has columns for id, name, and state_id
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Represents a city in the database.

    Attributes:
        id (int): The unique identifier for the city.
        name (str): The name of the city.
        state_id (int): The foreign key referencing the id of the state
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
