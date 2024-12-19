from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=200, verbose_name='Имя пользователя', unique=True)
    email = models.EmailField(max_length=200, verbose_name='Email', unique=True)
    password = models.CharField(max_length=200, verbose_name='Пароль')
    avatar = models.FileField(verbose_name='Аватар', blank=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
