# Generated by Django 3.1 on 2020-09-01 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_auto_20200902_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='qty',
        ),
    ]
