from project.main.models import Disease
from project.main.serializers.doctor import DiseaseSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from project.main.serializers.doctor import Disease
from django.core import serializers
from django.shortcuts import render

import jieba
import jieba.analyse

class DiseaseViewSet(viewsets.ModelViewSet):

    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

class CheckViewSet(APIView):

    def get(self,request):
        return render(request, 'index.html')
        # return Response({'msg': 'use post request'}, status=status.HTTP_200_OK, template_name='index.html')

    # example {"content":"经常性头晕，频繁肚子痛"}
    # {"content":"流鼻涕，有点发热，恶心"}
    def post(self,request,format=None):
        print(request.data)
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
            return render(request, 'index.html', {'res':res.data, "content":content})
            # return Response({'msg': res.data}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'error'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': 'do nothing'}, status=status.HTTP_200_OK)
        