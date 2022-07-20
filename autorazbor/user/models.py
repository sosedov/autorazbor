from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length = 100, unique = True)
    user_email = models.EmailField(max_length=254, default='', unique = True)
    userphone = models.CharField(max_length = 16, unique = True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Tariff(models.Model):
    name = models.CharField(max_length=250)
    value = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Наценка'
        verbose_name_plural = 'Наценка на товары'