#!/usr/bin/python3
""" State Module for HBNB project """
import models
import os
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity model"""
   __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
