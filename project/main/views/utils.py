from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token

from project.main.serializers.users import UserSerializer

class UtilsViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def hello(self, requeset):
        return Response({"message":"Hello SYSU"})

    @action(detail=False, methods=['get'])
    def add(self, request):
        a = float(request.GET.get('a',0))
        b = float(request.GET.get('b',0))
        return Response({"result":a+b})

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = AuthTokenSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response({
                'code': 1,
                'message': '登录失败',
                'errors': serializer.errors
            })
        user = serializer.validated_data['user']
        userSerializer = UserSerializer(user, context={'request': request})
        userUrl = userSerializer.data['url']
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'code': 0,
            'message': "成功",
            'token': token.key,
            'url': userUrl,
            'id': user.id
        })


@api_view(['GET'])
def descriptionView(request):
    return Response({
        'code': 0,
        'message': 'DRF-Starter Project',
    })
