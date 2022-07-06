from django.contrib.auth.models import User
from rest_framework import serializers

from body.models import UserGallery


class UserGallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserGallery
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')