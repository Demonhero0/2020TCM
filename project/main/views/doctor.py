from project.main.models import Disease
from project.main.serializers.doctor import DiseaseSerializer,MedicineSerializer,DiseaseAdminSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from project.main.serializers.doctor import Disease,Medicine
from django.core import serializers
from django.shortcuts import render

import jieba
import jieba.analyse

class DiseaseAdminViewSet(viewsets.ModelViewSet):

    queryset = Disease.objects.all()
    serializer_class = DiseaseAdminSerializer

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class CheckViewSet(APIView):

    def get(self,request):
        content = request.GET.get('content',[])
        print(content)
        if content:
            disease_query = Disease.objects.none()
            disease_query = disease_query.union(Disease.objects.filter(name__contains=content))
            disease_query = disease_query.union(Disease.objects.filter(symptom__contains=content))
            # print(disease_query)
            tags = jieba.analyse.extract_tags(content, topK=20, withWeight=True, allowPOS=('ns','n','v'))
            print('tags: ',tags)
            for tag in tags:
                disease_query = disease_query.union(Disease.objects.filter(symptom__contains=tag[0]))
                disease_query = disease_query.union(Disease.objects.filter(name=tag[0]))
            # print(disease_query)
            res = DiseaseSerializer(disease_query,context={"request":request}, many=True)
            # print(res)
            return render(request, 'result.html', {'res':res.data, "content":content})
            # return Response({'msg': res.data}, status=status.HTTP_200_OK)
        else:
            disease_query = Disease.objects.all().order_by('-hits')[:3]
            res = DiseaseSerializer(disease_query,context={"request":request}, many=True)
            return render(request, 'index.html', {'res':res.data})
        return Response({'msg': 'do nothing'}, status=status.HTTP_200_OK)
        # return Response({'msg': 'use post request'}, status=status.HTTP_200_OK, template_name='index.html')

    # example {"content":"经常性头晕，频繁肚子痛"}
    # {"content":"流鼻涕，有点发热，恶心"}
    def post(self,request,format=None):
        # print(request.data)
        content = request.data.get('content',[])
        if content:
            tags = jieba.analyse.extract_tags(content, topK=20, withWeight=True, allowPOS=('ns','n','v'))
            print(tags)
            disease_query = Disease.objects.none()
            for tag in tags:
                disease_query = disease_query.union(Disease.objects.filter(symptom__contains=tag[0]))
                disease_query = disease_query.union(Disease.objects.filter(name=tag[0]))
            print(disease_query)
            res = DiseaseSerializer(disease_query,context={"request":request}, many=True)
            print(res)
            return render(request, 'result.html', {'res':res.data, "content":content})
            # return Response({'msg': res.data}, status=status.HTTP_200_OK)
        else:
            return render(request, 'result.html', {"content":content})
        return Response({'msg': 'do nothing'}, status=status.HTTP_200_OK)

class DiseaseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

    def retrieve(self, request, pk=None):
        disease = Disease.objects.get(id=pk)
        disease.hits += 1
        disease.save()
        res = DiseaseSerializer(disease,context={"request":request})
        return render(request, 'disease_detail.html', {"disease":res.data})
        