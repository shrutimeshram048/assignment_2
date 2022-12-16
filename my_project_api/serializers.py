from rest_framework import serializers
from my_project_api.models import Countries

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ('capital','largest_city','official_languages','area_total','population','GDP_nominal')
        