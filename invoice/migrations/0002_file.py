# Generated by Django 3.1 on 2020-09-01 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_copy', models.FileField(null=True, upload_to='invoice/pdfs/', verbose_name='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
