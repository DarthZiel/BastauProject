# Generated by Django 3.2.5 on 2022-05-19 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BastauApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='file',
            field=models.FileField(blank=True, upload_to='file', verbose_name='Файл'),
        ),
    ]