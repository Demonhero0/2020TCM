from rest_framework import serializers
from project.main.models import Disease,Medicine

class MedicineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medicine
        fields = ('url', 'name', 'composition', 'effect', 'diseases')

class DiseaseSerializer(serializers.HyperlinkedModelSerializer):
    medicines = MedicineSerializer(many=True)
    class Meta:
        model = Disease
        fields = ('url', 'name', 'introduction', 'symptom', 'treatment', 'medicines')
