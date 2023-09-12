from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Owner, Pet, Handler, Job)

if __name__ == '__main__':

    engine = create_engine('sqlite:///pet_app.db')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    #3✅ One to Many
    #Getting an owners pets
    #Use session.query and first to grab the first owner
    def get_first_owner():
        return session.query(Owner).first()

    #use session.query and filter_by to get the owners pets from Pet
    def pets_by_owner(owner): 
        # return session.query(Pet).filter(owner.id == Pet.id).all()
        return owner.pets
    
    #print out your owners pets
    # print(pets_by_owner(owner))
    
    #Getting a pets owner
    def owner_by_pet(pet):
        # with filter
        # return session.query(Owner).filter(pet.owner_id == Owner.id).first()
        return session.query(Owner).filter_by(id = pet.owner_id).first()


    #Use session.query and first to grab the first pet
    def get_first_pet():
        return session.query(Pet).first()
    
    #Use session.query and filter_by to get the owner associated with this pet
    # done above

    #4✅ Head back to models to build out a Many to Many 
#--------------------------------------------

#6.✅ Many to Many 
    #Use session.query and .first to get the first handler
    def get_first_handler():
        return session.query(Handler).first()
    
    #Use session.query and the .filter_by to grab the jobs
    def get_jobs_for_handler(handler):
        return session.query(Job).filter_by(handler_id=handler.id).all()
    
    #Print the jobs
    first_handler = get_first_handler()
    first_handlers_jobs = get_jobs_for_handler(first_handler)
    for job in first_handlers_jobs:
        print(job.pet)

    #Use the handler_jobs to query pets for the associated pet to each job.
    # job.pet
    

    #Optional breakpoint for debugging
    import ipdb; ipdb.set_trace()