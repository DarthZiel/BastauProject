from django import forms
from django.http import request

from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


ROLES = [('Студент', 'Студент'),
        ('Партнер', 'Партнер')]
class AddCaseForm(forms.Form):
    class Meta:
        model = Case
        fields = '__all__'


class RegisterUserForm(UserCreationForm):
    email = forms.CharField(label='Email',widget= forms.EmailInput(attrs={'class': 'form-input'}))
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-input'}))
    role = forms.ChoiceField(widget=forms.RadioSelect, choices=ROLES)

    class Meta:
        model = User
        fields = ['email', 'phone', 'role']

class LoginUserForm(AuthenticationForm):
    email = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class UserStudentForm(forms.ModelForm):
    user_id = forms.CharField(label='Юзер')

    class Meta:
        model = Student

        # fields = ['Fio', 'Educational_institution', 'date_of_birth', 'region', 'Direction_of_study', 'Education', 'Course']
        fields = "__all__"
class UserPartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'

from django.forms import ModelForm, TextInput, Textarea, Select, DateTimeInput
from django.contrib.auth.forms import AuthenticationForm

class AddCaseForm(forms.ModelForm):
    user_id = forms.CharField(label='Юзер')
    class Meta:
        model = Case
        # fields = ['title', 'description', 'category', 'date_of_close']
        fields = '__all__'

        # widgets = {
        #     "title": TextInput(attrs={
        #         'class': '',
        #         'placeholder': 'Название кейса'
        #     }),
        #     "description": Textarea(attrs={
        #         'class': '',
        #         'placeholder': 'Описание кейса'
        #     }),
        #     "category": Select (attrs={
        #         'class': '',
        #         'placeholder': 'Выберите категорию'
        #     }),
        #     "date_of_close": DateTimeInput(attrs={
        #         'class': '',
        #         'placeholder': 'Дата завершения кейса'
        #     }),
        #     "user_id": Select(attrs={
        #         'class': '',
        #         'placeholder': 'Выберите категорию'
        #     })
        # }

