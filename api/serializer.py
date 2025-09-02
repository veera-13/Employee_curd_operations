from api.models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    empid=serializers.IntegerField()
    empname=serializers.CharField()
    job=serializers.CharField()
    salary=serializers.FloatField()

    def create(self,data):
        return Employee.objects.create(**data)
    
    # def update(self,instance_data,validatio):
