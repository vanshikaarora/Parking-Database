# Generated by Django 2.0 on 2018-08-15 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0008_auto_20180814_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]