# Stretch Goal: Include Association with Owner

# Pet Attributes: 
# name: TEXT 
# species: TEXT
# breed: TEXT 
# temperament: TEXT
# age: INTEGER

# Stretch Goal
# owner_id: INTEGER

import sqlite3

CONN = sqlite3.connect('lib/dog_walker.db')
CURSOR = CONN.cursor()

class Pet:
    
    def __init__ ( self, owner_id, name, breed, age, id = None ) :
        self.name = name
        self.breed = breed
        self.age = age
        self.owner_id = owner_id
        self.id = id
    
    @property
    def id (self):
        if self._id is None:
            return -1
        else:
            return self._id
    
    @id.setter
    def id (self, id):
        self._id = id


    def __repr__ ( self ) :
        return f"{{ 'id': { self.id }, 'name': { self.name }, 'breed': { self.breed }, 'age': { self.age } }}"


    def save ( self ) :
        sql = 'INSERT INTO pets ( name, breed, age, owner_id ) values ( ?, ?, ?, ?)'
        CURSOR.execute( sql, ( self.name, self.breed, self.age, self.owner_id) )
        CONN.commit()

    @classmethod
    def new_from_db ( cls, record ) :
        return Pet(
            id = record[0],
            name = record[2],
            breed = record[4],
            age = record[3],
            owner_id = record[1]
        )
    
    @classmethod
    def print_db_records ( cls, records ) :
        return [ Pet.new_from_db( record ) for record in records ]

    @classmethod
    def all ( cls ) :
        sql = 'SELECT * FROM pets'
        pets = CURSOR.execute( sql ).fetchall()
        return Pet.print_db_records( pets )
    
    @classmethod
    def find_by_name ( cls, name ) :
        sql = f"SELECT * FROM pets WHERE name LIKE '{ name }'"
        pets = CURSOR.execute( sql ).fetchall()
        if pets :
            return Pet.print_db_records( pets )
        else :
        # If No "pet" Found, return "None"
            raise Exception( 'No pet found with that name.' )


    #
    @classmethod
    def find_by_id ( cls, id ) :
        if type( id ) is int and id > 0 :
            sql = f'SELECT * FROM pets WHERE id = { id }'
            pet = CURSOR.execute( sql ).fetchone()
            if pet :
                return Pet.new_from_db( pet )
            else :
                # If No "pet" Found, return "None"
                raise Exception( 'No pet with that id exists.' )
        else :
            raise Exception( 'Id must be a number greater than 0.' )


