# HRMS – Attendance Management System

## Project Overview

The **HRMS (Human Resource Management System)** is a web-based application developed using Django to manage employee attendance efficiently.  
It provides a centralized dashboard to track employees, mark daily attendance, generate attendance reports, and visualize data using charts.

The system is designed with real-world HR rules such as:
- Viewing attendance records employee-wise
- Displaying attendance insights through visual reports
- Addding or Deleting functionality

This project is suitable for small to medium organizations and academic assessments.

---

## Tech Stack Used

### Backend
- **Python 3.15**
- **Django 6.0.1**
- **Django REST Framework**

### Frontend
- **HTML5**
- **CSS3**
- **Bootstrap 5**
- **JavaScript**
- **Chart.js** (for Donut charts)

### Database
- **SQLite** (default Django database)

---

## Steps to Run the Project Locally

### 1️ Clone the Repository
```bash
git clone <repository-url>
cd HRMS

2️ Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️ Install Dependencies
pip install django djangorestframework

4️  Apply Migrations
python manage.py makemigrations
python manage.py migrate

5️ Create Superuser (Optional)
python manage.py createsuperuser

6️ Run the Development Server
python manage.py runserver

7️ Open in Browser
http://127.0.0.1:8000/

📊 Key Features
Employee management

Attendance marking (Present / Absent)

Attendance dashboard with overview cards

Donut chart visualization for attendance status

Employee-wise attendance records

Clean and professional UI

Developed For

Academic Assessment & Learning Purpose
HRMS Module – Django Web Application