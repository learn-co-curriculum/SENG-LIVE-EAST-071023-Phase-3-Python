#!/usr/bin/env python3

from lib.pet import Pet
from lib.owner import Owner
from lib.doctor import Doctor
from lib.appointment import Appointment
from lib.patient import Patient
import datetime


smith = Doctor(
    name = 'Smith',
    specialty = 'Orthopedics',
    license = True
)

allen = Doctor(
    name = 'Allen',
    specialty = 'Pediatrics',
    license = True
)

john = Patient(
    name = 'John',
    insurance = True,
    dob = ''
)

tess = Patient(
    name = 'Tess',
    insurance =  True,
    dob = ''
)

breElle = Patient(
    name = 'BreElle',
    insurance = True,
    dob = ''
)

app1 = Appointment(
    doctor = allen,
    patient = breElle,
    time = '1:00 pm',
    date = '9/1/23'
)

app2 = Appointment(
    doctor = allen,
    patient = tess,
    time = '11:00 am',
    date = '8/31/23'
)

app3 = Appointment(
    doctor = smith,
    patient = john,
    time = '2:00 pm',
    date = '9/5/23'
)

app4 = Appointment(
    doctor = allen,
    patient = john,
    time = '4:00 pm',
    date = '8/29/23'
)




princeton = Owner( 'Princeton', 'Nike', 987654321 )
curtis = Owner( 'Curtis', 'Birks', 123456789 )



buddy = Pet(
    type = 'Dog',
    breed = 'Golden Retriever',
    name = 'Buddy',
    owner = curtis
)

ziggy = Pet(
    type = 'Dog',
    breed = 'Black Lab',
    name = 'Ziggy',
    owner = princeton 
)


import ipdb; ipdb.set_trace()