#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

association_table = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False)


                          class Amenity(BaseModel, Base):
                          """Represents an Amenity for a MySQL database.

                          Attributes:
                          __tablename__ (str): Name of MySQL table
                          name (string): The amenity name.
                          place_amenities : Place-Amenity relationship.
                          """
                          __tablename__="amenities"
                          name=Column(String(128), nullable=False)
                          sec_table="place_amenity"
                          place_amenities=relationship("Place",
                                                       secondary=sec_table,
                                                       viewonly=False)
