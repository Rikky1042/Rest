
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
     name=serializers.CharField(max_length=100)
     roll=serializers.IntegerField()
     Class=serializers.CharField(max_length=100)
     School=serializers.CharField(max_length=100)
     mobile=serializers.IntegerField()

     def create(self, validate_data):
       return Student.objects.create(**validate_data)