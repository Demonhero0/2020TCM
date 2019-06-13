from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password')

    def save(self, **kwargs):
        if 'password' in self.validated_data:
            self.validated_data['password'] = make_password(self.validated_data['password'])

        super(UserSerializer, self).save(**kwargs)