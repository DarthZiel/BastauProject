from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddCaseForm, AuthUserForm
from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView
from .models import *
# Create your views here.
menu = [
       # {'title':'Создать кейс', 'url_name':'createcase'},
        {'title':'Партнеры','url_name':'partners'},
        {'title':'Кейсы', 'url_name':'showcases'},    
        #{'title':'Логин','url_name':'login'},
        {'title':'Контакты','url_name':'contacts'},
        {'title':'Личный кабинет','url_name':'personal'}
]

def personal(request):
    return render(request,'personal.html',{'menu':menu})
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
    form = AddCaseForm()
    error = ''
    if request.method == 'POST':
        form = AddCaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createcase')
    else:
        error = 'Форма была неверной'

    data = {
        'form': form,
        'error': error
    }
    return render(request,'createcase.html',data)

class LoginUser(LoginView):
    template_name = 'personal.html'
    # form_class = AuthUserForm
    form_class = AuthUserForm
    # success_url = reverse_lazy('createcase')

    def get_success_url(self):
        return reverse_lazy('createcase')

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
class ShowPartners(ListView):
    model = Partner 
    template_name = 'partners.html'
    extra_context = {'name':'Партнеры','menu':menu}
