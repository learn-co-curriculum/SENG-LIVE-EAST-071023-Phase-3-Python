class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append( self )

    def __repr__ ( self ) :
        return "{{ name: {} }}".format( self.name )

    @property
    def name ( self ) :
        return self._name
    
    @name.setter
    def name ( self, name ) :
        if not hasattr( self, 'name' ) :
            if type( name ) is str :
                self._name = name
            else :
                raise TypeError( 'Name must be a string.' )
        else :
            raise Exception( "Name can't be changed after initialization." )

    def trips(self):
        return [ trip for trip in Trip.all if trip.national_park is self ]

    def visitors(self):
        return list( set( [ trip.visitor for trip in self.trips() ] ) )

    def total_visits(self):
        return len( self.trips() )

    def best_visitor(self):
        visitors = [ trip.visitor for trip in self.trips() ]
        return max( visitors, key = visitors.count )

    @classmethod
    def most_visited(cls):
        return max( NationalPark.all, key = lambda national_park: len( national_park.trips() ) )

from classes.visitor import Visitor
from classes.trip import Trip