from django.urls import path
from .views import employee_page, delete_employee

app_name = 'employees'

urlpatterns = [
    # Employee list + add employee
    path('', employee_page, name='employee_list'),

    # Delete employee by employee_id
    path('delete/<str:employee_id>/', delete_employee, name='delete_employee')
]