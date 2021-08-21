from rest_framework import serializers
from student.models import student

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=('name', 'admission_number', 'roll_number', 'college', 'parent_name')