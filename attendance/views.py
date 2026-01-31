import json
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from .models import Attendance
from .serializers import AttendanceSerializer
from employees.models import Employee



class AttendanceCreateView(generics.CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class AttendanceListView(generics.ListAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        employee_id = self.kwargs['employee_id']
        return Attendance.objects.filter(employee__employee_id=employee_id)
    

def mark_attendance(request):
    if request.method == "POST":
        Attendance.objects.create(
            employee_id=request.POST['employee'],
            date=request.POST['date'],
            status=request.POST['status']
        )
        return redirect('/attendance/')

    employees = Employee.objects.all()
    return render(request, 'attendance.html', {'employees': employees})

# CAHRT VIEWS :

def attendance_chart(request):
    summary = Attendance.objects.values('status').annotate(count = Count('status'))

    labels = [x['status'] for x in summary]
    data = [x['count'] for x in summary]

    return render(request, 'charts.html', {
        'labels' : labels,
        'data' : data
    })
   
# Employee Attendance:

def employee_attendance(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    records = Attendance.objects.filter(employee=employee).order_by('-date')

    return render(request, 'attendance/employee_attendance.html', {
        'employee': employee,
        'records': records
    })
