from unicodedata import name
from django.db import models

# Create your models here.
class Auto(models.Model):
    name = models.CharField("Марка", max_length=250,)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Марка"


class Auto_Model(models.Model):
    name = models.CharField("Модель", max_length=250)
    auto = models.ForeignKey(Auto, verbose_name="Марка", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Модель"


class Auto_SubModel(models.Model):
    name = models.CharField("Подмодель", max_length=250)
    automodel = models.ForeignKey(Auto_Model, verbose_name="Модель", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Подмодель"

class Part(models.Model):
    name = models.CharField("Запчасть", max_length=250)
    auto = models.ForeignKey(Auto, verbose_name="Запчасть", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Запчасть"
        verbose_name_plural = "Запчасти"

class Part_Model(models.Model):
    name = models.CharField("Дополнительно", max_length=250)
    auto = models.ForeignKey(Part, verbose_name="Дополнительно", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Дополнительно"
