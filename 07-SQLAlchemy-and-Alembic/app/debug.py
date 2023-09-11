
# 3.✅ CRUD practice
# To run the file run `python3 console.py` in the app directory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Pet)

if __name__ == '__main__':
    #3.1 ✅ Uncomment bellow to create the engine
    engine = create_engine('sqlite:///pet_app.db')
    Base.metadata.create_all(engine)
    #3.2 ✅ Uncomment bellow to create sessions and bind o the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    #3.3 ✅  -- Creating records
    ashe = Pet(name = "Ashe", species = "Cat", breed = "Chartreux", temperament = "fiesty", owner_id = 1)
    isha = Pet(name = "Isha", species = "Dog", breed = "Mutt", temperament = "loving", owner_id = 2)
    liam = Pet(name = "Liam", species = "Dog", breed = "Golden Doodle", temperament = "wild", owner_id = 2)
    
    def save_pet(pet):
        # Create a pet and save it to the data base with session.add and session.commit
        session.add(pet)
        session.commit()
        
    def save_pets(pets):
        # Create multiple pets and bulk save them with  session.bulk_save_objects and session.commit
        session.bulk_save_objects(pets)
        session.commit()

        #verify by checking the db 
    #3.4 ✅ Read
    def get_all_pets():
        # Get all with session.query
        # Print the pets 
        return session.query(Pet).all()

    def print_all_pets(pets):
        for pet in pets:
            print(pet)
    
    def print_pet_names():
        #Get all of the pet names and print them with session.query
        names = session.query(Pet.name).all()
        print("Printing all pet names:")
        for name in names:
            print(name[0])
        
    
    def print_pet_names_in_reverse_order():
        #Get all the pet names and print them in order with session.query and order_by
        names = session.query(Pet.name).order_by(Pet.name.desc()).all()
        print("Printing all pet names:")
        for name in names:
            print(name[0])

    def get_first_pet():
        #Get the first pet with session.query and first
        return session.query(Pet).first()

    def get_by_temperament(temp):
        #Filter pet by temperament with session.query and filter 
        return session.query(Pet).filter(Pet.temperament.like(f"%{temp}%")).all()


    #3.5 ✅ Update 
    def update_name(new_name, pet):
        # Update the pets name and print the updated pet info
        if isinstance(pet, Pet):
            pet.name = new_name
            session.commit()
        else:
            raise TypeError("Must be of type pet")
    
    
    def update_all_pets_temperament(temp = "cool"):
        # Update all the pets temperament to 'cool' and print the pets
        session.query(Pet).update({Pet.temperament : temp})
        session.commit()
   
    def update_all_pets_temperament_individually(temp = "cool"):
        # Update all the pets temperament to 'cool' and print the pets
        for pet in get_all_pets():
            pet.temperament = temp
        session.commit()

    #3.6 ✅  Delete
        # Delete one item by 
        # querying the first pet
    def delete_pet(pet):
        # pet must be a query object
        session.delete(pet)
        # committing it
        session.commit()

    def delete_all_pets():
        #delete all the pets with session.query and .delete
        session.query(Pet).delete()
        session.commit()
    

    # optional Break point for debugging and testing
    import ipdb; ipdb.set_trace()