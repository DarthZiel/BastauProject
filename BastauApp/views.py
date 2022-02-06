from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddCaseForm
from django.views.generic import ListView
from .models import *
# Create your views here.
menu = [
        {'title':'Создать кейс', 'url_name':'createcase'},
        {'title':'Показать кейсы', 'url_name':'showcases'},    
        {'title':'Логин','url_name':'login'},
        {'title':'Контакты','url_name':'contacts'}    
]
def contacts(request):
    return render(request,'contacts.html',{'menu':menu})
def index(request):
    return render(request,'index.html',{'menu':menu})

def about(request):
    return render(request,'about.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html',{'menu':menu})

def createcase(request):
    if request.method == 'POST':
        form = AddCaseForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddCaseForm()
        data = {
            'form': form
        }
    return render(request,'createcase.html',{'menu':menu})
class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    # def get_context_data(self,*,object_list=None,**kwargs):
    #     content = super().get_context_data(**kwargs)
    #     c_def = self.get_user_content(title='Регистрация')
    #     return dict(list(content.items()) + list(c_def.items()))
    
class ShowCases(ListView):
    model = Case 
    template_name = 'ShowCase.html'
    extra_context = {"name":'Кейсы','menu':menu}
