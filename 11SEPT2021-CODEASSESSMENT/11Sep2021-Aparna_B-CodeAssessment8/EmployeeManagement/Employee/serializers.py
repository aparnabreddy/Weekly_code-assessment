from rest_framework import serializers
from Employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('empcode','name', 'address', 'pincode', 'mobilenum', 'salary', 'username', 'password')