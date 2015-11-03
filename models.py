from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgres import JSONB
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

PlaceTagRelation = Table('_rel_place_tag', Base.metadata,
                         Column('place_id', Integer, ForeignKey('places.id')),
                         Column('tag', String, ForeignKey('tags.tag')),
                         UniqueConstraint('place_id', 'tag', name='unique_place_tag')
                         )


class Place(Base):
    __tablename__ = 'places'
    type = 'place'

    id = Column(Integer, primary_key=True, unique=True)
    created = Column(DateTime)
    modified = Column(DateTime, onupdate=datetime.datetime.utcnow)
    name = Column(String, nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    address = Column(String, nullable=False)
    image = Column(String)
    description = Column(String)
    tags = relationship('Tag', secondary=PlaceTagRelation)
    meta = Column(JSONB)


class Tag(Base):
    __tablename__ = 'tags'
    type = 'tag'

    tag = Column(String, nullable=False, primary_key=True, unique=True)
    created = Column(DateTime)
    modified = Column(DateTime, onupdate=datetime.datetime.utcnow)
    synonyms = Column(JSONB)
    places = relationship('Place', secondary=PlaceTagRelation)
    image = Column(String)
    meta = Column(JSONB)
