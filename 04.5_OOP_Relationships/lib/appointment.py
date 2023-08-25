class Appointment :

    all = []

    def __init__( self, patient, doctor, date, time ) :
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.time = time
        Appointment.all.append( self )

    pass
