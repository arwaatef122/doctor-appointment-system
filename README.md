# Doctor Appointment Booking System

## Team Details
| Student ID | Full name | Assigned task | Branch | PR link |
| :--- | :--- | :--- | :--- | :--- |
| 20240808 | أروى عاطف أحمد | Use Cases & Requirements | `feature/arwa-design` | [[PR Link]](https://github.com/arwaatef122/doctor-appointment-system/pull/1)() |
| 20240808 | أروى عاطف أحمد | Class Diagram | `feature/arwa-design` | [[PR Link]](https://github.com/arwaatef122/doctor-appointment-system/pull/1)() |
| 20240809 | محمد عاطف أحمد | Sequence Diagram | `feature/mohamed-work` | [[PR Link]](https://github.com/arwaatef122/doctor-appointment-system/pull/2)() |
| 20240809 | محمد عاطف أحمد | Implementation | `feature/mohamed-work` | [[PR Link]](https://github.com/arwaatef122/doctor-appointment-system/pull/2)() |

---

## System Requirements Overview
- **R1:** A patient can view the days and times when a doctor is available[cite: 1].
- **R2:** A patient can book an appointment during an available time slot[cite: 1].
- **R3:** A doctor can accept or decline an appointment request[cite: 1].
- **R4:** A patient can have at most 3 upcoming appointments at any given time (Count future Pending + Accepted appointments; Declined, Cancelled and past appointments do not count)[cite: 1].

---

## Non-Functional Requirements Handling (R5 - R7)
- **R5 (Security):** Patient medical data shall be accessible only to authorized staff through secure Role-Based Access Control (RBAC)[cite: 1].
- **R6 (Performance):** Available appointment times shall be displayed within 2 seconds by optimizing database queries and rendering logic[cite: 1].
- **R7 (Usability):** The application interface shall be fully responsive and usable on mobile phone screens[cite: 1].

---

## Run Instructions (Implementation)
1. Ensure Python is installed on your machine.
2. Run the application script from the terminal:
   ```bash
   python app.py
