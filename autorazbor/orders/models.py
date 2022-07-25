from datetime import datetime

from django.db import models

from users.models import User

from generic.models import AbstractModel

from parts.models import Parts


class Order(AbstractModel):
    manager = models.ForeignKey(User, on_delete = models.CASCADE, related_name='manager')
    customer = models.ForeignKey(User, on_delete = models.CASCADE,  related_name='customer')

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Order_Items(AbstractModel):
    order = models.ForeignKey(Order, on_delete = models.CASCADE, default=None, null=True)
    part = models.ForeignKey(Parts, on_delete = models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Заказ запчасти'
        verbose_name_plural = 'Заказы запчастей'