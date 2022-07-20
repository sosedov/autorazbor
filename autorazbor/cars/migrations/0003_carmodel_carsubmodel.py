# Generated by Django 4.0.6 on 2022-07-19 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_carmark_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('car_mark', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.carmark')),
            ],
            options={
                'verbose_name': 'Модель авто',
                'verbose_name_plural': 'Модели авто',
            },
        ),
        migrations.CreateModel(
            name='CarSubmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('car_model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.carmodel')),
            ],
            options={
                'verbose_name': 'Комплектация авто',
                'verbose_name_plural': 'Комплектации авто',
            },
        ),
    ]
