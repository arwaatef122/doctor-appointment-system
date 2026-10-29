graph TD
    Patient([Patient]) --> UC1[R1: View Doctor Availability]
    Patient --> UC2[R2 & R4: Book Appointment (Limit N=3)]
    Doctor([Doctor]) --> UC3[R3: Accept/Decline Appointment]
    
    subgraph Doctor Appointment Booking System
        UC1
        UC2
        UC3
    end