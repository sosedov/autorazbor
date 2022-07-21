import os

from datetime import datetime

from django.db import models

from generic.models import AbstractModel


class CarMark(AbstractModel):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.changed = datetime.now()
        super(CarMark, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Марка авто'
        verbose_name_plural = 'Марки авто'


class CarModel(AbstractModel):
    name = models.CharField(max_length=250)
    car_mark = models.ForeignKey(CarMark, on_delete = models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.changed = datetime.now()
        super(CarModel, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Модель авто'
        verbose_name_plural = 'Модели авто'


class CarSubmodel(AbstractModel):
    name = models.CharField(max_length=250)
    car_model = models.ForeignKey(CarModel, on_delete = models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.changed = datetime.now()
        super(CarSubmodel, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Комплектация авто'
        verbose_name_plural = 'Комплектации авто'