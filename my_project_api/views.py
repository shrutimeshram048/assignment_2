from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from my_project_api.serializers import CountriesSerializer
from my_project_api.models import Countries

class CountriesViewSet(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    