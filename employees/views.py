from django.shortcuts import render, redirect
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeListCreateView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDeleteView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    lookup_field = 'employee_id'


def employee_page(request):
    if request.method == "POST":
        Employee.objects.create(
            employee_id = request.POST['employee_id'],
            full_name = request.POST['full_name'],
            email = request.POST['email'],
            department = request.POST['department']
        )
        return redirect('/employees/')
    employees = Employee.objects.all()
    return render (request, 'employees.html', {'employees' : employees})

def delete_employee(request, employee_id):
    Employee.objects.filter(employee_id= employee_id).delete()
    return redirect('/employees/')

