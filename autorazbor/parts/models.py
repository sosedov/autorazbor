from datetime import datetime

from django.db import models

from cars.models import CarSubmodel

from generic.models import AbstractModel

from django.core.validators import EmailValidator


class PartCategory(AbstractModel):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.changed = datetime.now()
        super(PartCategory, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Запчасть'
        verbose_name_plural = 'Запчасти'


class PartSubCategory(AbstractModel):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(PartCategory, on_delete = models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.changed = datetime.now()
        super(PartSubCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Вид запчасти'
        verbose_name_plural = 'Виды запчастей'


class Parts(AbstractModel):
    car_submodel = models.ForeignKey(CarSubmodel, on_delete = models.CASCADE, default=None, null=True)
    part_subcategory = models.ForeignKey(PartSubCategory, on_delete = models.CASCADE, default=None, null=True)
    price = models.SlugField(max_length=250)
    seller_name = models.CharField(max_length=250)
    seller_phone = models.PositiveIntegerField(unique = True)
    seller_email = models.CharField(max_length=255, validators=[EmailValidator(message="invalid email")])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.changed = datetime.now()
        super(Parts, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Информация о товаре'
        verbose_name_plural = 'Информация о товарах'