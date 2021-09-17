from rest_framework import serializers
from appadmin.models import Admin,Donor

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields=('id','adminname','username','password')

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donor
        fields=('id','name','address','bgroup','mobilenumber','username','password')