from rest_framework import serializers
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
# 👉 Metadata = Data about data 
# It’s not the actual data itself — it’s information that describes the data or how it should be used. 
    class Meta:
        model = Student
        fields = "__all__"