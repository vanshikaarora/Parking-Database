# Generated by Django 2.0 on 2018-08-13 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0004_remove_post_timeout'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='timeOut',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
