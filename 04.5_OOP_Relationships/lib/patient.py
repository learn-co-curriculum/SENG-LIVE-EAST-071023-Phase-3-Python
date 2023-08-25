class Patient :

    all = []

    def __init__ ( self, name, insurance, dob ) :
        self.name = name
        self.insurance = insurance
        self.dob = dob
        Patient.all.append( self )

    def appointments ( self ) :
        return [ app for app in Appointment.all if app.patient is self ]
    
    def doctors ( self ) :
        return [ app.doctor.name for app in self.appointments() ]
    
    def make_appointment ( self, doctor, time, date ) :
        Appointment(
            patient = self,
            doctor = doctor,
            time = time,
            date = date
        )

    pass

from .appointment import Appointment
from .doctor import Doctor