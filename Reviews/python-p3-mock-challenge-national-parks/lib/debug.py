#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    v1 = Visitor( "Princeton" )
    v2 = Visitor( "Thomas" )
    v3 = Visitor( "Curtis" )
    v4 = Visitor( "Farhan" )

    n1 = NationalPark( "Yellowstone" )
    n2 = NationalPark( "Thomas Town" )
    n3 = NationalPark( "Stone Mountain" )
    n4 = NationalPark( "Grand Canyon" )

    t1 = Trip ( v2, n2, '8/30/23', '8/30/23' )
    t2 = Trip ( v3, n1, '10/21/23', '10/27/23' )
    t3 = Trip ( v4, n4, '8/31/23', '9/1/23' )
    t4 = Trip ( v4, n2, '11/1/23', '11/25/23' )
    t5 = Trip ( v3, n2, '11/1/23', '11/25/23' )
    t6 = Trip ( v1, n4, '2/5/24', '2/10/24' )
    t7 = Trip ( v1, n3, '7/4/24', '7/4/24' )
    t8 = Trip ( v1, n1, '10/30/23', '11/4/23' )
    t9 = Trip ( v1, n1, '9/2/23', '9/5/23' )
    t10 = Trip ( v1, n2, '3/11/24', '3/23/24' )


    ipdb.set_trace()
