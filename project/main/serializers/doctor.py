from rest_framework import serializers
from project.main.models import Disease,Medicine

class MedicineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medicine
        fields = ('url','id', 'name', 'composition', 'effect')

class DiseaseAdminSerializer(serializers.HyperlinkedModelSerializer):
    # medicines = MedicineSerializer(many=True)
    class Meta:
        model = Disease
        fields = ('url','id', 'name', 'introduction', 'symptom', 'treatment', 'hits', 'medicines')

class DiseaseSerializer(serializers.HyperlinkedModelSerializer):
    medicines = MedicineSerializer(many=True)
    class Meta:
        model = Disease
        fields = ('url','id', 'name', 'introduction', 'symptom', 'treatment', 'hits', 'medicines')
    
    # def create(self,validated_data):
    #     print(validated_data)
    #     disease = Disease.objects.get_or_create(**validated_data)
    #     return disease
