from django import forms
from .models import *
from django.forms import ModelForm, TextInput, Textarea, Select, DateTimeInput
from django.contrib.auth.forms import AuthenticationForm

class AddCaseForm(ModelForm):
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

class AuthUserForm(AuthenticationForm,ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
