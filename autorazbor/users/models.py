from django.db import models

from django.contrib.auth.models import AbstractUser

from django.core.validators import EmailValidator

from generic.models import AbstractModel


class User(AbstractUser):
    username = models.CharField(max_length=255, validators=[EmailValidator(message="invalid email")], unique = True)
    phone = models.PositiveIntegerField(default=None, null=True, unique = True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Tariff(AbstractModel):
    name = models.CharField(max_length=250)
    value = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Наценка'
        verbose_name_plural = 'Наценка на товары'