from rest_framework import viewsets
from modelform import models
from modelform import serializers
from modelform.models import  StudentRecord,CollegeRecord
from django.db.models import Count

class StudentRecordViewset(viewsets.ModelViewSet):
    queryset = models.StudentRecord.objects.all()
    serializer_class = serializers.StudentRecordSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'
    filterset_fields = ('name', )
    extra_kwargs = {'url': {'lookup_field':'name'}}


    def get_queryset(self):
        data1 = self.filter_queryset(CollegeRecord.objects.values_list('name','register_date','classname__name', 'classname__studentname__name'))
        data = self.filter_queryset(StudentRecord.objects.all())
        print(data)
        print(data1)

        return data

class StudentAddressViewset(viewsets.ModelViewSet):
    queryset = models.StudentAddress.objects.all()
    serializer_class = serializers.StudentAddressSerializer


    '''def get_queryset(self):
        data1 = self.filter_queryset(CollegeRecord.objects.values_list('name','register_date','classname__name', 'classname__studentname__name'))
        data = self.filter_queryset(StudentRecord.objects.all())
        print(data)
        print(data1)'''



