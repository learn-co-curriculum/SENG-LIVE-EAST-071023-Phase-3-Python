class Owner ( ) :

    all = []

    def __init__ ( self, name, shoes, ssn ) :
        self.name = name
        self.shoes = shoes
        if type( ssn ) is int and len( str( ssn ) ) == 9 :
            self.__ssn = ssn
        else :
            raise Exception( 'SSN must be a 9-digit number.' )
        Owner.all.append( self )

    @property
    def ssn ( self ) :
        return '***-**-' + str( self.__ssn )[-4:]
    
    @ssn.setter
    def ssn ( self, ssn ) :
        print( "You can't change a SSN once its been assigned!" )


    @property
    def name ( self ) :
        return self._name
    
    @name.setter
    def name ( self, name ) :
        if type( name ) is str and len( name ) > 0 :
            self._name = name
        else :
            raise Exception( 'Name must be a string and more than 0 characters.' )

    @property
    def shoes ( self ) :
        return self._shoes
    
    @shoes.setter
    def shoes ( self, shoes ) :
        self._shoes = shoes

    def pets ( self ) :
        return [ pet for pet in Pet.all if pet.owner is self ]

    pass

from .pet import Pet