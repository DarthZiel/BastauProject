# Generated by Django 4.0 on 2022-02-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BastauApp', '0006_remove_case_is_won_student_is_won'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='is_won',
        ),
        migrations.AddField(
            model_name='user',
            name='is_won',
            field=models.BooleanField(default=False),
        ),
    ]
