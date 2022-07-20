from django.db import models

from user.models import User

from parts.models import Parts


class Order(models.Model):
    manager = models.ForeignKey(User, on_delete = models.CASCADE, related_name='Менеджер')
    customer = models.ForeignKey(User, on_delete = models.CASCADE, related_name='Покупатель')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Order_Items(models.Model):
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
    part = models.ForeignKey(Parts, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Заказ запчасти'
        verbose_name_plural = 'Заказы запчастей'