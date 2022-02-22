# Generated by Django 4.0.2 on 2022-02-22 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('phone', models.CharField(help_text='Номер телефона', max_length=20)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_partner', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Юзер',
                'verbose_name_plural': 'Юзеры',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='id')),
                ('Fio', models.CharField(blank=True, max_length=100, verbose_name='ФИО')),
                ('name_of_partner', models.CharField(max_length=100, verbose_name='Название организации')),
                ('site', models.URLField()),
                ('avatar', models.ImageField(blank=True, upload_to='img/', verbose_name='Аватар')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='id')),
                ('Fio', models.CharField(blank=True, max_length=100, verbose_name='ФИО')),
                ('Educational_institution', models.CharField(max_length=50, verbose_name='Место учебы')),
                ('age', models.CharField(max_length=2, verbose_name='возраст')),
                ('region', models.CharField(choices=[('Акмолинская', 'Акмолинская'), ('Актюбинская', 'Актюбинская'), ('Алматинская', 'Алматинская'), ('Атырауская', 'Атырауская'), ('Восточно-Казахстанская', 'Восточно-Казахстанская')], default=('Акмолинская', 'Акмолинская'), max_length=50)),
                ('Direction_of_study', models.CharField(max_length=50, verbose_name='Специальность')),
                ('Education', models.CharField(choices=[('Высшее', 'Высшее'), ('ср-спе', 'Среднее-специальное'), ('среднее', 'Среднее')], default=('Высшее', 'Высшее'), max_length=50, verbose_name='Образование')),
                ('Course', models.CharField(choices=[('1', '1'), ('2', '2')], default=('Высшее', 'Высшее'), max_length=50, verbose_name='Образование')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
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
                ('is_published', models.BooleanField(default=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Кейс',
                'verbose_name_plural': 'Кейсы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Url', models.URLField(blank=True, verbose_name='Ссылка на ответ')),
                ('File', models.FileField(blank=True, upload_to='file', verbose_name='Файл')),
                ('id_case', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='BastauApp.case', verbose_name='id_case')),
                ('id_student', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='id_student')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
