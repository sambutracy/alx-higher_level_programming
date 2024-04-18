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
    Represents a state in the database.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.
        state_id (int): The foreign key referencing the id of the state
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
