# Generated by Django 3.2.5 on 2022-05-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BastauApp', '0002_case_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='is_won',
        ),
        migrations.AddField(
            model_name='answer',
            name='status',
            field=models.CharField(choices=[('Ваш ответ еще не просмотрен', 'Ваш ответ еще не просмотрен'), ('К сожалению вы проирали', ' сожалению вы проирали'), ('Поздравляем, вы выиграли', 'Поздравляем, вы выиграли')], default=('Ваш ответ еще не просмотрен', 'Ваш ответ еще не просмотрен'), max_length=50, verbose_name='Область'),
        ),
    ]