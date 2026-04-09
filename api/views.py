from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from employee.models import Employee
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
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
    
@api_view(['GET', 'PUT', 'DELETE'])
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
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# class based views doesnot need decorator apiView as like function based one and 
# this decides which method to call on its own 
class Employees(APIView):
    def get(self, request):
        emps = Employee.objects.all()
        serializer = EmployeeSerializer(emps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class EmployeeDetail(APIView):
    # this method is used to get that particular object and its reusable 
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        employee = self.get_object(pk)
        # in serailizer we are paaing object also bcz wkt which object to target and 
        # then what data has been changed for that particular from drf frontend
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
