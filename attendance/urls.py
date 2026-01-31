from django.urls import path
from .views import mark_attendance, attendance_chart, employee_attendance

app_name = 'attendance'

urlpatterns = [ 
    # Mark attendance
    path('',mark_attendance, name='mark_attendance'),

    # Attendance summary chart
    path('charts/', attendance_chart, name='attendance_chart'),

    # Employee Attendance
    path('employee/<str:employee_id>/', employee_attendance, name='employee_attendance'),
]