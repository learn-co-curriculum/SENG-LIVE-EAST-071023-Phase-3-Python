class Pet ( ) :

    all = []

    def __init__ ( self, name, type, breed, owner ) :
        self.name = name
        self.type = type
        self.breed = breed
        self._owner = owner
        Pet.all.append( self )

    @property
    def owner ( self ) :
        return self._owner
    
    @owner.setter
    def owner ( self, owner ) :
        if type( owner ) is Owner :
            self._owner = owner
        else :
            raise TypeError( 'Owner must be an instance of the Owner class.' )


    pass
    
from .owner import *