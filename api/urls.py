from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsView),
    # function based 
    path('student/<int:pk>', views.studentDetailView),

    # class based views 
    path('employees/', views.Employees.as_view()),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view()),
]