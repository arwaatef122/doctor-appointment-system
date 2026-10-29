classDiagram
    class Patient {
        +int patient_id
        +string name
        +string email
        +view_availability()
        +book_appointment()
    }

    class Doctor {
        +int doctor_id
        +string name
        +string specialization
        +manage_appointment()
    }

    class Appointment {
        +int appointment_id
        +string date_time
        +string status
        +create()
        +update_status()
    }

    Patient "1" --> "*" Appointment : books
    Doctor "1" --> "*" Appointment : manages