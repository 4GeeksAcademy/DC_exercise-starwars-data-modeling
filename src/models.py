import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    birth_year = Column(Integer, nullable=True)
    gender = Column(String(250), nullable=True)
    height = Column(Integer, nullable=True)
    skin_color = Column(String(250), nullable=True)
    eye_color = Column(String(250), nullable=True)
    favoritos = relationship ('Favoritos', backref= 'characters', lazy=True)

    def to_dict(self):
        return {}

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    climate = Column(String(250), nullable=True)
    population = Column(Integer, nullable=True)
    orbital_period = Column(Integer, nullable=True)
    rotation_period = Column(Integer, nullable=True)
    diameter = Column(Integer, nullable=True)
    favoritos = relationship ('Favoritos', backref= 'planets', lazy=True)
  
    
    def to_dict(self):
        return {}

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    model = Column(String(250), nullable=True)
    cargo_capacity = Column(Integer, nullable=True)
    consumables = Column(String(250), nullable=True)
    passengers = Column(Integer, nullable=True)
    crew = Column(Integer, nullable=True)
    favoritos = relationship ('Favoritos', backref= 'vehicles', lazy=True)
    
    
    def to_dict(self):
        return {}

class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    characters_id= Column(Integer, ForeignKey('characters.id'),nullable=True)
    planets_id= Column(Integer, ForeignKey('planets.id'),nullable=True)
    vehicles_id= Column(Integer, ForeignKey('vehicles.id'),nullable=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'),
                        nullable=False)
    def to_dict(self):
        return {}

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favoritos = relationship ('Favoritos', backref= 'usuario', lazy=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
