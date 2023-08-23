from typing import Any
import ipdb

    # Demonstrate classes 
    # 1. ✅ Create a Person class
    # 2. ✅ Instantiate a few person instances 
        # Compare the person instances to demonstrate they are not the same object

class Person :
    pass

    # 3. ✅ Demonstrate __init__
    def __init__ ( self, first_name, last_name, date_of_birth, ssn ):
        pass
        # ✅ Add arguments to instances  
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.set_ssn( ssn )

        # ✅ use dot notation to access their attributes 
        # ✅ update attributes with new values 


        # ✅ Demonstrate the self keyword 



        
    # 4.✅ Demonstrate instance methods by creating a greeting function that will print a message
        #     Review the self keyword 
        #     Invoke the greeting on an instance 
    def greeting ( self ):
        print( f"Hello there! I'm { self.first_name }." )


    # Demonstrate getters and setters
    def get_first_name ( self ):
        return self._first_name

    def set_first_name ( self, first_name ) :
        if type( first_name ) is str and len( first_name ) > 0 :
            self._first_name = first_name
        else :
            raise Exception( 'Name must be a string and more than 0 characters long.' )
    
    # Demonstrate object properties
    first_name = property( get_first_name, set_first_name )


    # Demonstrate decorators ( stretch goal! )