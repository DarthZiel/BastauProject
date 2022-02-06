from django import forms
from .models import *

class AddCaseForm(forms.Form):
    class Meta:
        model = Case
        fields = '__all__'