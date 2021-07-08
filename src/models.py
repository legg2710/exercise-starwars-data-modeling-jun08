import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    frist_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email= Column(String(250), unique=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    planet = Column(String(250), nullable=False)
    character = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Characters(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    frist_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    planet_name= Column(String(250), nullable=False)
    vehicles= Column(String(250), nullable=False)
    weapons= Column(String(250), nullable=False)
    character_race= Column(String(250), nullable=False)
    character_skill= Column(String(250), nullable=False)
    favorite_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship(Favorites)
    

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    autor_favorites = relationship(Favorites)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    autor_favorites = relationship(Favorites)

class Weapons(Base):
    __tablename__ = 'weapons'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    autor_favorites = relationship(Favorites)

class Character_race(Base):
    __tablename__ = 'Character_race'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    autor_favorites = relationship(Favorites)

class Character_skill(Base):
    __tablename__ = 'Character_skill'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    autor_favorites = relationship(Favorites)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')