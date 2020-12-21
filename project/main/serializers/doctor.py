from rest_framework import serializers
from project.main.models import Disease

class DiseaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disease
        fields = ('url', 'name', 'introduction', 'symptom', 'treatment', 'medicines')