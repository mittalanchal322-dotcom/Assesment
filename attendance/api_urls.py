from django.urls import path
from .views import AttendanceCreateView, AttendanceListView

urlpatterns = [
    path('', AttendanceCreateView.as_view()),
    path('<str:employee_id>/', AttendanceListView.as_view()),
]
