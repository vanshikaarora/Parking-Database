# Generated by Django 2.0 on 2018-08-13 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0005_post_timeout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='timeOut',
        ),
    ]