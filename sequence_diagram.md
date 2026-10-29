sequenceDiagram
    autonumber
    actor Patient
    participant System
    actor Doctor

    Patient->>System: Request doctor availability (R1)
    System-->>Patient: Display available days & times (R6)
    
    Patient->>System: Select slot & request booking (R2)
    Note over System: Check if active appointments < N (R4)
    System-->>Patient: Booking confirmation (Pending)
    
    Doctor->>System: View pending appointment requests
    System-->>Doctor: Show appointment details
    Doctor->>System: Accept or Decline request (R3)
    System-->>Patient: Notify appointment status update