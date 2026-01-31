from django.urls import path
from .views import EmployeeListCreateView, EmployeeDeleteView

urlpatterns = [
    path('', EmployeeListCreateView.as_view()),
    path('<str:employee_id>/', EmployeeDeleteView.as_view()),
]
