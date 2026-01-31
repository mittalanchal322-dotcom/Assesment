from django.shortcuts import render
from employees.models import Employee
from attendance.models import Attendance
from django.db.models import Count

def dashboard(request):

    total_employees = Employee.objects.count()

    # Attendance summary:

    attendance_summary = Attendance.objects.values('status').annotate(count = Count('status'))

    labels =  [x['status']  for x in attendance_summary]
    data =  [x['count'] for x in attendance_summary]

    labels = labels or ["No Data"]
    data = data or [1]

    context = {
        'total_employees' : total_employees,
        'attendance_labels' : labels,
        'attendance_data' : data
    }
    return render(request, 'dashboard.html', context)