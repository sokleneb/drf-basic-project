from rest_framework import serializers
from students.models import Student
from employee.models import Employee


class StudentSerializer(serializers.ModelSerializer):
# 👉 Metadata = Data about data 
# It’s not the actual data itself — it’s information that describes the data or how it should be used. 
    class Meta:
        model = Student
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"