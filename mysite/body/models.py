import os

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserGallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField('User_image', upload_to="image/user/")

    class Meta:
        verbose_name = "Картинка пользователя"
        verbose_name_plural = "Картинки пользователя"
        db_table = "UserGallery"


