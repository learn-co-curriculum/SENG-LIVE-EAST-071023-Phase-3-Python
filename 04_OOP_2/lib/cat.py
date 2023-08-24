#6✅. Create a subclass of Pet called Cat
    # import Pet from lib.pet
from lib.pet import Pet

    # Update the instance in debug.py to rose = Cat('rose', 11, 'domestic longhair', 'sweet', 'rose.jpg', True)


class Cat ( Pet ) :

# ✅. Create __init__ that takes all the parameters from Pet and a parameter called indoor 
    # Use super to pass the Pet parameters to the super class
    # Add an indoor attribute
    
    def __init__ ( self, name, age, temperament, image_url, breed, indoor ) :
        super().__init__( name, age, temperament, image_url )
        self.breed = breed
        self.indoor = indoor

#7✅. Create a method unique to the Cat subclass called talk which returns the string "Meowwwwwww"
    def talk ( self ) :
        return 'Meowwwwwww 🐈'

#9✅. Stretch: Create a method called print_pet_details, to match the print_pet_details in Pet    
        #Add super().print_pet_details() and print the indoor attribute
    def print_pet_details( self ):
        super().print_pet_details()
        print(f'''
            breed: { self.breed }
            indoor: { self.indoor }
        ''')