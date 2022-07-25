# Generated by Django 4.0.6 on 2022-07-20 12:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_carmodel_changed_carmodel_created_and_more'),
        ('parts', '0002_alter_parts_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='partcategory',
            name='changed',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='partcategory',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='parts',
            name='changed',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='parts',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='partsubcategory',
            name='changed',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='partsubcategory',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='partcategory',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='parts',
            name='car_submodel',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.carsubmodel'),
        ),
        migrations.AlterField(
            model_name='parts',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='parts',
            name='part_subcategory',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='parts.partsubcategory'),
        ),
        migrations.AlterField(
            model_name='parts',
            name='seller_email',
            field=models.CharField(max_length=255, validators=[django.core.validators.EmailValidator(message='invalid email')]),
        ),
        migrations.AlterField(
            model_name='parts',
            name='seller_phone',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='partsubcategory',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='parts.partcategory'),
        ),
        migrations.AlterField(
            model_name='partsubcategory',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
