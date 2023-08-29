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

CONN = sqlite3.connect('lib/resources.db')
CURSOR = CONN.cursor()

class Pet:
    
    # ✅ 1. Add "__init__" with "name", "species", "breed", "temperament", and "id" (Default: None) Attributes
    def __init__ ( self, name, species, breed, temperament, age, id = None ) :
        self.name = name
        self.species = species
        self.breed = breed
        self.temperament = temperament
        self.age = age
        self.id = id

    def __repr__ ( self ) :
        return f"{{ 'id': { self.id }, 'name': { self.name }, 'species': { self.species }, 'breed': { self.breed }, 'temperament': { self.temperament }, 'age': { self.age } }}"

    # ✅ 2. Add "create_table" Class Method to Create "pets" Table If Doesn't Already Exist
    @classmethod
    def create_table ( cls ) :
        sql = '''
            CREATE TABLE IF NOT EXISTS pets (
                id INTEGER PRIMARY KEY,
                name TEXT,
                species TEXT,
                breed TEXT,
                temperament TEXT,
                age INTEGER
            )
        '''
        CURSOR.execute( sql )
        # CURSOR.execute( '''
        #     CREATE TABLE IF NOT EXISTS pets (
        #         id INTEGER PRIMARY KEY,
        #         name TEXT,
        #         species TEXT,
        #         breed TEXT,
        #         temperament TEXT,
        #         age INTEGER
        #     )
        # '''
        # )

    # ✅ 3. Add "drop_table" Class Method to Drop "pets" Table If Exists
    @classmethod
    def drop_table ( cls ) :
        sql = 'DROP TABLE IF EXISTS pets'
        CURSOR.execute( sql )


    # ✅ 4. Add "save" Instance Method to Persist New "pet" Instances to DB
    def save ( self ) :
        sql = 'INSERT INTO pets ( name, breed, species, age, temperament ) values ( ?, ?, ?, ?, ? )'
        CURSOR.execute( sql, ( self.name, self.breed, self.species, self.age, self.temperament ) )
        # sql = f"INSERT INTO pets ( name, breed, species, age, temperament ) values ( '{ self.name }', '{ self.breed }', '{ self.species }', { self.age }, '{ self.temperament }' )"
        # CURSOR.execute( sql )
        CONN.commit()


    # ✅ 5. Add "create" Class Method to Initialize and Save New "pet" Instances to DB
    @classmethod
    def create ( cls, name, breed, species, temperament, age ) :
        new_pet = Pet(
            name = name,
            breed = breed,
            species = species,
            age = age,
            temperament = temperament
        )
        new_pet.save()
        return cls.new_from_db()


    # ✅ 6. Add "new_from_db" Class Method to Retrieve Newest "pet" Instance w/ Attributes From DB
    @classmethod
    def new_from_db ( cls ) :
        sql = "SELECT * FROM pets ORDER BY id DESC"
        pet = CURSOR.execute( sql ).fetchone()
        return Pet.print_db_record( pet )
    

    @classmethod
    def print_db_record ( cls, record ) :
        return Pet(
            id = record[0],
            name = record[1],
            species = record[2],
            breed = record[3],
            temperament = record[4],
            age = record[5]
        )
    
    @classmethod
    def print_db_records ( cls, records ) :
        return [ Pet.print_db_record( record ) for record in records ]


    # ✅ 7. Add "get_all" Class Method to Retrieve All "pet" Instances From DB
    @classmethod
    def all ( cls ) :
        sql = 'SELECT * FROM pets'
        pets = CURSOR.execute( sql ).fetchall()
        return Pet.print_db_records( pets )


    # ✅ 8. Add "find_by_name" Class Method to Retrieve "pet" Instance by "name" Attribute From DB
    @classmethod
    def find_by_name ( cls, name ) :
        sql = f"SELECT * FROM pets WHERE name LIKE '{ name }'"
        pets = CURSOR.execute( sql ).fetchall()
        if pets :
            return Pet.print_db_records( pets )
        else :
        # If No "pet" Found, return "None"
            raise Exception( 'No pet found with that name.' )


    # ✅ 9. Add "find_by_id" Class Method to Retrieve "pet" Instance by "id" Attribute From DB
    @classmethod
    def find_by_id ( cls, id ) :
        if type( id ) is int and id > 0 :
            sql = f'SELECT * FROM pets WHERE id = { id }'
            pet = CURSOR.execute( sql ).fetchone()
            if pet :
                return Pet.print_db_record( pet )
            else :
                # If No "pet" Found, return "None"
                raise Exception( 'No pet with that id exists.' )
        else :
            raise Exception( 'Id must be a number greater than 0.' )


    # ✅ 10. Add "find_or_create_by" Class Method to:
    @classmethod
    def find_or_create_by ( cls, name, breed, species, age, temperament ) :
        sql = f"SELECT * FROM pets WHERE name LIKE '{ name }' and species LIKE '{ species }' and age = { age } and breed LIKE '{ breed }' and temperament LIKE '{ temperament }'"
        pets = CURSOR.execute( sql ).fetchall()
        if pets :
            #  Find and Retrieve "pet" Instance w/ All Attributes
            return Pet.print_db_records( pets )
        else :
            # If No "pet" Found, Create New "pet" Instance w/ All Attributes
            Pet.create(
                name = name,
                age = age,
                species= species,
                temperament= temperament,
                breed= breed
            )

    # ✅ 11. Add "update" Class Method to Find "pet" Instance by "id" and Update All Attributes

