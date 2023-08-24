#!/usr/bin/env python3
# Class Attributes and Methods 

class Pet:

    # ✅. Create a class variable that will track all of our instances of Pet
    all = []
    


    def __init__(self , name, age, temperament, image_url):
        self.set_name( name )
        self.age = age
        self.temperament = temperament
        self.image_url = image_url
        self.all.append( self )

    # ✅. Create some decorators for some of the attributes

    @property
    def age ( self ) :
        return self._age
    
    @age.setter
    def age ( self, age ) :
        if type( age ) is int and age > 0 :
            self._age = age
        else :
            raise Exception( 'Age must be a number greater than 0.' )


    # ✅. Show the difference between properties and decorators

    def get_name ( self ) :
        return self._name
    
    def set_name ( self, name ) :
        if type( name ) is str and len( name ) > 0 :
            self._name = name
        else :
            raise Exception( 'Name must be a string and greater than 0 characters.' )

    name = property( get_name, set_name )


    def print_pet_details(self):
        print(f'''
            name: {self.name}
            age: {self.age}
            temperament: {self.temperament}
            image_url: {self.image_url}
        ''')

    # ✅. Show off a class method
    @classmethod
    def total_number_of_pets ( cls ) :
        return f"The total number of pets is { len( cls.all ) }."

