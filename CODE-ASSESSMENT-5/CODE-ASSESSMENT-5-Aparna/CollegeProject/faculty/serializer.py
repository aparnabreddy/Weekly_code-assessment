from rest_framework import serializers
from faculty.models import faculty

class facultySerializer(serializers.ModelSerializer):
    class Meta:
        model=faculty
        fields=('faculty_code', 'name', 'department', 'address', 'mobilenumber', 'username', 'password')