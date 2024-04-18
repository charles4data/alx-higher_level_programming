#!/usr/bin/python3
""" creates state class """
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base


metadata = MetaData()
Base = declarative_base(metadata=metadata)

class State(Base):
    """ state class """
    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
