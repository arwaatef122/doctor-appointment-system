class BookingSystem:
    def __init__(self):
        self.doctors = {"Dr. Ahmed": ["2026-11-01 10:00 AM", "2026-11-01 11:00 AM"]}
        self.appointments = []  # List of dicts
        self.MAX_UPCOMING = 3   # N = 3 (R4)

    def view_availability(self, doctor_name):
        return self.doctors.get(doctor_name, [])

    def book_appointment(self, patient_id, doctor_name, slot):
        # Count active upcoming (Pending + Accepted) for this patient
        active_count = sum(
            1 for a in self.appointments 
            if a["patient_id"] == patient_id and a["status"] in ["Pending", "Accepted"]
        )
        
        if active_count >= self.MAX_UPCOMING:
            return f"Booking failed: Reached the maximum limit of {self.MAX_UPCOMING} upcoming appointments (R4)."
        
        if slot in self.doctors.get(doctor_name, []):
            self.appointments.append({
                "patient_id": patient_id,
                "doctor": doctor_name,
                "slot": slot,
                "status": "Pending"
            })
            return "Appointment requested successfully! Status: Pending."
        return "Selected slot is not available."

    def manage_appointment(self, patient_id, slot, action):
        for appt in self.appointments:
            if appt["patient_id"] == patient_id and appt["slot"] == slot:
                if action.lower() in ["accept", "decline"]:
                    appt["status"] = "Accepted" if action.lower() == "accept" else "Declined"
                    return f"Appointment status updated to: {appt['status']} (R3)."
        return "Appointment not found."

if __name__ == "__main__":
    system = BookingSystem()
    print("Available times for Dr. Ahmed (R1):", system.view_availability("Dr. Ahmed"))
    print(system.book_appointment(101, "Dr. Ahmed", "2026-11-01 10:00 AM")) # R2 & R4
    print(system.manage_appointment(101, "2026-11-01 10:00 AM", "Accept")) # R3