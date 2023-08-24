#!/usr/bin/env python3
# 📚 Review With Students:
    # Introduction to Object Oriented programming, classes, instances, methods

# Importing the pet class 
from lib.pet import *
from lib.cat import *

# Instances of the pet classes
cookie = Pet('cookie', 1, 'hyper', 'cookie.jpg')
princess = Pet( 'Princess', 2, 'docile', 'princess.jpg' )

# ✅. Show how to do mass assignment when making a new instance
Pet(
    name = 'K',
    image_url = 'k.jpg',
    temperament = 'Calm',
    age = 5
)

rose = Cat(
    name = 'Rose',
    image_url = 'rose.jpg',
    indoor = True,
    breed = 'Sphinx',
    temperament = 'independent',
    age = 6
)
# princess_grace = Cat('princess grace', 7, 'domestic longhair', 'affectionate', 'gracy.png')




import ipdb; ipdb.set_trace()