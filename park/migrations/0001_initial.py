# Generated by Django 2.0 on 2018-08-22 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatePost',
            fields=[
                ('date', models.CharField(blank=True, max_length=25)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('vehicleType', models.CharField(blank=True, max_length=200)),
                ('number', models.CharField(blank=True, max_length=10, primary_key=True, serialize=False)),
                ('amount', models.CharField(blank=True, max_length=3)),
                ('timeIn', models.CharField(blank=True, max_length=30)),
                ('timeOut', models.CharField(blank=True, max_length=30)),
                ('date', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='datepost',
            name='vehicleNumber',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, to='park.Post'),
        ),
    ]
