# Generated by Django 4.0 on 2022-02-20 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BastauApp', '0002_alter_answer_file_alter_answer_id_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='File',
            field=models.FileField(blank=True, upload_to='file/', verbose_name='Файл'),
        ),
    ]
