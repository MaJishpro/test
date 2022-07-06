from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from body.models import UserGallery
from body.serializers import UserGallerySerializer, UserSerializer


class UserViews(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(methods=['GET'], detail=False)
    def active_user(self, request):
        response = {'authenticated': False}
        if request.user.is_authenticated:
            user = {
                "id": request.user.id,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "login": request.user.username
            }
            response['authenticated'] = True
            response['user'] = user
        return JsonResponse(response)

    @action(methods=['POST'], detail=False)
    def registration_user(self, request):
        try:
            User.objects.create_user(**request.data)
            response = {'status': True}
        except IntegrityError:
            response = {
                "status": False,
                "error": "Username already"
            }
        return JsonResponse(response)

    @action(methods=['POST'], detail=False)
    def login_user(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            response = {
                "status": True,
            }
        else:
            response = {
                "status": False,
                "error": "Errors"
            }
        return JsonResponse(response)


class UserGalleryViews(viewsets.ModelViewSet):
    serializer_class = UserGallerySerializer
    queryset = UserGallery.objects.all()

    @action(methods=['GET'], detail=False)
    def delete_all(self, request):
        UserGallery.objects.all().delete()
        return JsonResponse({"status": "successful"})