#1.✅ Update our models to include a One to Many association
# Pet >- Owner

#Import ForeignKey
from sqlalchemy import (Column, String, Integer, Float,  DateTime, ForeignKey)

# import relationship and backref from sqlalchemy.orm
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    species = Column(String())
    breed = Column(String())
    temperament = Column(String())
    
    #1.a✅ Add  ForeignKey('owners.id') to owner.id
    owner_id = Column(Integer(), ForeignKey('owners.id'))
    # owner = relationship
    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Name:{self.name}, " \
            + f"Species {self.species}, "\
            + f"Breed {self.breed}, "\
            + f"Temperament {self.temperament}"

#1.b✅ Add an Owners table 
class Owner(Base):
    __tablename__ = 'owners'

    #Create the following columns
    # id -> type integer -> primary key = True
    # name -> type string
    # email -> type string
    # phone -> type int
    # address -> type string
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String(), unique=True)
    phone = Column(Integer())
    address = Column(String())

    #1.c✅ Associate the Pet model with the owner Model
    pets = relationship('Pet', backref=backref('pet'))

    #def pets(self):
        # query the pets class, for all pets that belong to me based upon my owner id

    #add a __repr__ method that returns a string containing the id, name, email, phone and address of our class
    def __repr__ (self):
        return f"{{Id: {self.id}"\
            + f"Name: {self.name},"\
            + f"Email: {self.email},"\
            + f"Phone: {self.phone},"\
            + f"Address: {self.address}}}"\

#2.✅ Update your migrations by running `alembic revision --autogenerate -m` and `alembic upgrade head` 

    # Note: If you still have your database from the previous lecture, you'll need to create a migration to update the pets table 
    # After running your migrations, go build out some seeds and test your one-to-many with debug.py
# -------------------------------

#4.✅ Update our Model to have a Many to Many association
# Pet-< Jobs >- Handlers

# Create a Handlers table
class Handler(Base):
    __tablename__ = "handlers"
    #Create the following columns
    # id -> type integer
    # name -> type string
    # email -> type string
    # phone -> type int
    # hourly_rate -> type float
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String(), unique=True)
    phone = Column(Integer())
    hourly_rate = Column(Float())
    


    #add a __repr__ method that returns a string containing the id, name, email, phone and hourly_rate of our class
    def __repr__ (self):
        return f"{{Id: {self.id}"\
            + f"Name: {self.name},"\
            + f"Email: {self.email},"\
            + f"Phone: {self.phone},"\
            + f"Hourly Rate: {self.hourly_rate}}}"\
    
#Create a "jobs" table to serve as our join
class Job(Base):
    __tablename__ = "jobs"

    #Create the following columns
    # id -> type integer
    # request -> type string
    # date -> type datetime
    # fee -> type float
    # pet_id -> type int with a ForeignKey('pet.id')
    # handler_id -> type int with a ForeignKey('handlers.id')
    id = Column(Integer(), primary_key=True)
    request = Column(String())
    date = Column(DateTime())
    fee = Column(Float())
    pet_id = Column(Integer(), ForeignKey('pets.id'))
    handler_id = Column(Integer(), ForeignKey('handlers.id'))

    #Associate the models with relationship(<ModelNameHere>, backref=backref(<TableNameHere>))
    pet = relationship('Pet', backref=backref('pets'))
    handler = relationship('Handler', backref=backref('handlers'))

    #Add a __repr__ method that returns a string containing the id, request, date, notes, fee, pet_id and handler_id of our class
    def __repr__(self):
        return f"{{Id: {self.id}"\
            + f"Request: {self.request},"\
            + f"Date: {self.date},"\
            + f"Fee: {self.fee},"\
            + f"pet_id: {self.pet_id},"\
            + f"handler_id: {self.handler_id}}}"\
#5.✅ Update your migrations by running `alembic revision --autogenerate -m` and `alembic upgrade head` 

#After running your migrations, go build out some seeds and test your many to many with debug.py