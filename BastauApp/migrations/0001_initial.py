# Generated by Django 4.0 on 2022-02-05 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('FistName', models.CharField(max_length=50, verbose_name='Имя')),
                ('LastName', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('MidlleName', models.CharField(max_length=50, verbose_name='Отчество')),
                ('phone', models.CharField(help_text='Номер телефона', max_length=20)),
            ],
            options={
                'verbose_name': 'Юзер',
                'verbose_name_plural': 'Юзеры',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Educational_institution', models.CharField(max_length=50, verbose_name='Место учебы')),
                ('date_of_birth', models.DateField()),
                ('region', models.CharField(choices=[('Акмолинская', 'Акмолинская'), ('Актюбинская', 'Актюбинская'), ('Алматинская', 'Алматинская'), ('Атырауская', 'Атырауская'), ('Восточно-Казахстанская', 'Восточно-Казахстанская')], default=('Акмолинская', 'Акмолинская'), max_length=50)),
                ('Direction_of_study', models.CharField(max_length=50, verbose_name='Специальность')),
                ('Education', models.CharField(choices=[('Высшее', 'Высшее'), ('ср-спе', 'Среднее-специальное'), ('среднее', 'Среднее')], default=('Высшее', 'Высшее'), max_length=50, verbose_name='Образование')),
                ('Course', models.CharField(choices=[('1', '1'), ('2', '2')], default=('Высшее', 'Высшее'), max_length=50, verbose_name='Образование')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BastauApp.user', verbose_name='id')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_partner', models.CharField(max_length=100, verbose_name='Название организации')),
                ('site', models.URLField()),
                ('avatar', models.ImageField(upload_to='avatar/', verbose_name='Аватар')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BastauApp.user', verbose_name='id')),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание кейса')),
                ('date_of_create', models.DateTimeField(auto_now=True)),
                ('date_of_edit', models.DateTimeField(auto_now_add=True)),
                ('date_of_close', models.DateTimeField()),
                ('category', models.CharField(choices=[('Медицина', 'Медицина'), ('Программирование', 'Программирование'), ('Архитектура', 'Архитектура')], max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BastauApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Url', models.URLField(blank=True, verbose_name='Ссылка на ответ')),
                ('File', models.FileField(upload_to='', verbose_name='Файл')),
                ('id_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BastauApp.case', verbose_name='id_case')),
                ('id_student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BastauApp.student', verbose_name='id_student')),
            ],
        ),
    ]