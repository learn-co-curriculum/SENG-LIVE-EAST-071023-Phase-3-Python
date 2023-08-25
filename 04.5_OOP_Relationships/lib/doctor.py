class Doctor :

    all = []

    def __init__ ( self, name, specialty, license ) :
        self._name = name
        self.specialty = specialty
        self.license = license
        Doctor.all.append( self )

    @property
    def name ( self ) :
        return 'Dr.' + self._name.title()
    
    @name.setter
    def name ( self, name ) :
        self._name = name

    def appointments ( self ) :
        return [ app for app in Appointment.all if app.doctor is self ]
    
    def upcoming_appointments ( self ) :
        for app in self.appointments() :
            print(f'''
            Patient: { app.patient.name }
            Date: { app.date }
            Time: { app.time }

        ''')
            
    def patients ( self ) :
        return [ app.patient.name for app in self.appointments() ]

    pass

from .appointment import Appointment
from .patient import Patient