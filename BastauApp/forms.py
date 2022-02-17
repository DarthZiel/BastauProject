from django import forms
from django.db import transaction

from django.forms import ModelForm, TextInput, Textarea, Select, DateTimeInput, EmailField
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class AddCaseForm(forms.Form):
    class Meta:
        model = Case
        fields = '__all__'

REGIONS = [
        ('Акмолинская', 'Акмолинская'),
        ('Актюбинская', 'Актюбинская'),
        ('Алматинская', 'Алматинская'),
        ('Атырауская', 'Атырауская'),
        ('Восточно-Казахстанская', 'Восточно-Казахстанская'),
        # 'Жамбылская','Западно-Казахстанская','Карагандинская','Костанайская','Кызылординская','Мангистауская','Павлодарская','Северо-Казахстанская','Южно-Казахстанская'
    ]
EDUCATION = [
    ('Высшее', 'Высшее'), ('ср-спе', 'Среднее-специальное'), ('среднее', 'Среднее')
]

COURSE = [
    ('1', '1'),
    ('2', '2'),
    # '3','4','5'
]
# class RegisterUserForm(UserCreationForm):
#     email = forms.CharField(label='Email',widget= forms.EmailInput(attrs={'class': 'form-input'}))
#     phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     role = forms.ChoiceField(widget=forms.RadioSelect, choices=ROLES)
# #
#     class Meta:
#         model = User
#         fields = ['email', 'phone', 'role']
class StudentSignUpForm(UserCreationForm):
    Fio = forms.CharField(required=True)
    Educational_institution = forms.CharField(required=True)
    age = forms.CharField(required=True)
    region = forms.ChoiceField(required=True,widget=forms.Select, choices=REGIONS)
    Direction_of_study = forms.CharField(required=True)
    Education = forms.ChoiceField(required=True,widget=forms.Select, choices= EDUCATION)
    Course = forms.ChoiceField(required=True,widget=forms.Select, choices= COURSE)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email','phone']
        field_classes = {'email': EmailField}


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.email = self.cleaned_data.get('email')
        user.phone = self.cleaned_data.get('phone')

        student = Student.objects.create(user=user)
        student.Fio = self.cleaned_data.get('Fio')
        student.age = self.cleaned_data.get('age')
        student.Educational_institution = self.cleaned_data.get('Educational_institution')
        # student.region = self.cleaned_data.get('Регион')
        # student.Course = self.cleaned_data.get('Курс')
        student.Direction_of_study = self.cleaned_data.get('Direction_of_study')
        student.Education = self.cleaned_data.get('Education')
        student.save()
        return user


class PartnerSignUpForm(UserCreationForm):
    Fio = forms.CharField()
    name_of_partner = forms.CharField()
    site = forms.URLField()
    avatar = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        fields = ['email','phone']
        field_classes = {'email': EmailField}
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_partner = True
        user.is_staff = True
        user.email = self.cleaned_data.get('email')
        user.phone = self.cleaned_data.get('phone')
        user.save()
        partner = Partner.objects.create(user=user)
        partner.Fio = self.cleaned_data.get('Fio')
        partner.name_of_partner = self.cleaned_data.get('name_of_partner')
        partner.site = self.cleaned_data.get('site')
        partner.avatar = self.cleaned_data.get('avatar')
        partner.save()
        return user

class AddCaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['title', 'description', 'category', 'date_of_close', 'user_id']

        widgets = {
            "title": TextInput(attrs={
                'class': '',
                'placeholder': 'Название кейса'
            }),
            "description": Textarea(attrs={
                'class': '',
                'placeholder': 'Описание кейса'
            }),
            "category": Select (attrs={
                'class': '',
                'placeholder': 'Выберите категорию'
            }),
            "date_of_close": DateTimeInput(attrs={
                'class': '',
                'placeholder': 'Дата завершения кейса'
            }),
            "url": TextInput(attrs={
                'class': '',
                'placeholder': 'Название ссылки'
            }),
        }

# class DetailCase(forms.ModelForm):
#     class Meta:
#         model = Case
#         fields = ['title', 'description', 'category', 'date_of_close', 'user_id']
class LoginUserForm(AuthenticationForm):
    email = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
