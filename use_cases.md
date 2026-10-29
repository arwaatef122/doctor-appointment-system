# Use Cases - Doctor Appointment Booking System

## Actors
1. **Patient**: Uses the system to view doctor availability, book appointments, and manage requests.
2. **Doctor**: Views incoming appointment requests and accepts or declines them.

## Use Cases
- **UC1: View Doctor Availability (R1)**
  - **Actor**: Patient
  - **Description**: The patient browses the system to see available days and time slots for specific doctors.
- **UC2: Book Appointment (R2, R4)**
  - **Actor**: Patient
  - **Description**: The patient selects an available time slot to book an appointment, provided their active upcoming appointments (Pending + Accepted) do not exceed the limit ($N = 3$).
- **UC3: Manage Appointment Requests (R3)**
  - **Actor**: Doctor
  - **Description**: The doctor views pending appointment requests and chooses either to accept or decline them.