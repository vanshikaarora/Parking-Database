# Generated by Django 2.0 on 2018-08-11 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='amount',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='post',
            name='number',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='timeIn',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='vehicleType',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]