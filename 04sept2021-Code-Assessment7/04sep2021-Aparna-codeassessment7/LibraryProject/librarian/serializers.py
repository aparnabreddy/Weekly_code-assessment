from django.db.models import fields
from rest_framework import serializers
from librarian.models import Librarian

class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model=Librarian
        fields=('id','librarian_code','name','address','mobile_no','pincode','email_id','username','password')






