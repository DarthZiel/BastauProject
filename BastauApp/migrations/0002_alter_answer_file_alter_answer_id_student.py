# Generated by Django 4.0 on 2022-02-20 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BastauApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='File',
            field=models.FileField(upload_to='file', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='id_student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BastauApp.user', verbose_name='id_student'),
        ),
    ]
