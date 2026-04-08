from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
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

# this below is manual way of doing serialazation ( converting complex code to JSON )
# def studentsView(request):
#     students = Student.objects.all().values()
#     students_list = list(students)
#     # safe=false because we are sending non-dict soo 
#     return JsonResponse(students_list, safe=False)

# using serializers
@api_view(['GET'])
def studentsView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        student.delete()
        
    
