# Generated by Django 2.0 on 2018-08-14 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0007_post_timeout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AlterField(
            model_name='post',
            name='number',
            field=models.CharField(blank=True, max_length=10, primary_key=True, serialize=False),
        ),
    ]
