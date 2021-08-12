from rest_framework import serializers
from modelform import models


class StudentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentRecord
        fields = ('id', 'name', 'age', 'year', 'register_date')

class StudentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentAddress
        fields = ('city','pin')