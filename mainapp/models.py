from django.db import models
from  django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class CustomUser(AbstractBaseUser, PermissionsMixin):

    class Gender(models.TextChoices):
        MAN = 'M', 'Man'
        WOMAN = 'W', 'Woman'


    username = models.CharField(verbose_name='имя', max_length=50)
    surname = models.CharField(verbose_name='фамилия', max_length=50)
    email = models.EmailField(verbose_name='почта', unique=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.MAN)
    avatar = models.FilePathField(verbose_name='аватарка')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return f"{self.username} {self.surname}"