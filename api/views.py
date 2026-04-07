from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
# Create your views here.

# basic api endpoint for understand 
# def studentsView(request):
#     khalifas = [
#         { 'id': "1", 'name': "Abu Bakar RA"},
#         { 'id': "2", 'name': "Umar e Farroq RA" },
#         { 'id': "3", 'name': "Osman RA" },
#         { 'id': "4", 'name': "Hazrath Ali RA" },
#     ]
#     return JsonResponse(khalifas, safe=False)

def studentsView(request):
    # this below is manual way of doing serialazation 
    students = Student.objects.all().values()
    print('11111', students)
    students_list = list(students)
    print('22222', students_list)
    # safe=false because we are sending non-dict soo 
    return JsonResponse(students_list, safe=False)