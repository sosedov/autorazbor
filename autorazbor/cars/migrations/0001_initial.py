# Generated by Django 4.0.6 on 2022-07-19 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMark',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('changed', models.DateTimeField(null=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Марка авто',
                'verbose_name_plural': 'Марки авто',
            },
        ),
    ]