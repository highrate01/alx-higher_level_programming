#!/usr/bin/python3
"""
contains the class definition of a State and an
instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from relationship_city import Base, City

Base = declarative_base()


class State(Base):
    """
    Defines a state and an instance Base
    """
    __tablename__ = 'states'
    id = Column(
                Integer, primary_key=True, nullable=False,
                autoincrement=True
                )
    name = Column(String(128), nullable=False)

    cities = relationship(
            "City", backref="state", cascade="all, delete"
            )
