#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    cu1 = Customer( 'Princeton' )
    cu2 = Customer( 'Thomas' )
    cu3 = Customer( 'BreElle' )
    cu4 = Customer( 'John' )

    co1 = Coffee( 'Mocha' )
    co2 = Coffee( 'Latte' )
    co3 = Coffee( 'Americano' )
    co4 = Coffee( 'Cappuccino' )
    co5 = Coffee( 'Espresso' )

    o1 = Order( customer = cu1, coffee = co5, price = 10 )
    o2 = Order( customer = cu4, coffee = co1, price = 5 )
    o3 = Order( customer = cu3, coffee = co2, price = 2 )
    o4 = Order( customer = cu1, coffee = co3, price = 7 )
    o5 = Order( customer = cu1, coffee = co5, price = 4 )
    o6 = Order( cu1, co1, 5 )
    o7 = Order( cu1, co1, 6 )

    ipdb.set_trace()
