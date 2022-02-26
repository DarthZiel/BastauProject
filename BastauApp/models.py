from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin, BaseUserManager
from django.shortcuts import reverse


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, phone, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            **extra_fields
        )

        user.set_password(password)  # change password to hash
        user.save(using=self._db)
        return user

    def create_user(self, email, password, phone, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, phone, **extra_fields)

    def create_superuser(self, email, password, phone, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError(('Superuser must have is_staff=True.'))
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError(('Superuser must have is_superuser=True.'))
        return self._create_user(email, password, phone, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    phone = models.CharField(max_length=20, help_text='Номер телефона')
    is_staff = models.BooleanField(default=True)  # must needed, otherwise you won't be at
    is_active = models.BooleanField(default=True)  # must needed, otherwise you won't be «
    is_superuser = models.BooleanField(default=False)  # this field we inherit from Permis
    is_student = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)

    objects = CustomUserManager()
    REQUIRED_FIELDS = ["phone"]
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = "Юзер"
        verbose_name_plural = "Юзеры"


class Student(models.Model):
    user = models.OneToOneField(User, verbose_name='id', on_delete=models.CASCADE, primary_key=True)
    Fio = models.CharField(max_length=100, blank=True, verbose_name='ФИО')
    REGIONS = [
        ('Акмолинская', 'Акмолинская'),
        ('Актюбинская', 'Актюбинская'),
        ('Алматинская', 'Алматинская'),
        ('Атырауская', 'Атырауская'),
        ('Восточно-Казахстанская', 'Восточно-Казахстанская'),
        ('Жамбылская','Жамбылская'),
        ('Жамбылская','Жамбылская'),
        ('Западно-Казахстанская','Западно-Казахстанская'),
        ('Карагандинская','Костанайская'),
        ('Костанайская','Костанайская'),
        ('Кызылординская','Кызылординская'),
        ('Мангистауская','Мангистауская'),
        ('Павлодарская','Павлодарская'),
        ('Северо-Казахстанская','Северо-Казахстанская'),
        ('Южно-Казахстанская','Южно-Казахстанская')
    ]
    EDUCATION = [
        ('Высшее', 'Высшее'), ('ср-спе', 'Среднее-специальное'), ('среднее', 'Среднее')
    ]

    COURSE = [
        ('1', '1'),
        ('2', '2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
    ]
    Educational_institution = models.CharField(max_length=50, verbose_name='Место учебы')
    age = models.CharField(max_length=2,verbose_name='возраст')
    region = models.CharField(max_length=50, choices=REGIONS, default=REGIONS[0])
    Direction_of_study = models.CharField(max_length=50, verbose_name='Специальность')
    Education = models.CharField(max_length=50, verbose_name='Образование', choices=EDUCATION, default=EDUCATION[0])
    Course = models.CharField(max_length=50, verbose_name='Образование', choices=COURSE, default=EDUCATION[0])


    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return self.Fio


class Partner(models.Model):
    user = models.OneToOneField(User, verbose_name='id', on_delete=models.CASCADE, primary_key=True)
    Fio = models.CharField(max_length=100, verbose_name='ФИО', blank=True)
    name_of_partner = models.CharField(max_length=100, verbose_name='Название организации')
    site = models.URLField(max_length=200)
    avatar = models.ImageField("Аватар", upload_to="img/", blank=True)
    about_company = models.TextField(max_length=1000,verbose_name='О компании')


    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

    def __str__(self):
        return self.Fio

class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Case(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание кейса')
    date_of_create = models.DateTimeField(auto_now=True)
    date_of_edit = models.DateTimeField(auto_now_add=True)
    date_of_close = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Кейс"
        verbose_name_plural = "Кейсы"

    def __str__(self):
        return self.title

class Answer(models.Model):
    STATUS = [
        ('Участник', 'Участник'), ('Победитель','Победитель' )]
    Url = models.URLField(verbose_name='Ссылка на ответ', blank=True)
    File = models.FileField(verbose_name='Файл', upload_to = "file",blank=True)
    id_case = models.ForeignKey(Case, verbose_name="id_case", on_delete=models.CASCADE,blank=True,related_name='cases')
    id_student = models.ForeignKey(User, verbose_name="id_student", on_delete=models.CASCADE,blank=True)
    is_won = models.CharField(max_length=20,verbose_name='Победитель',choices=STATUS, default= STATUS[0])
    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"


