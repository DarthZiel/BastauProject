from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import AddCaseForm,StudentSignUpForm, PartnerSignUpForm,LoginUserForm

from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView

from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import *
from django.contrib.auth import logout, login

menu = [
    # {'title':'Создать кейс', 'url_name':'createcase'},
    {'title': 'Партнеры', 'url_name': 'partners'},
    {'title': 'Кейсы', 'url_name': 'showcases'},
    {'title': 'Контакты', 'url_name': 'contacts'},
]


def logout_user(request):
    logout(request)
    return redirect('login')

def personal(request):
    return render(request, 'personal.html')



def contacts(request):
    return render(request, 'contacts.html', {'menu': menu})


def index(request):
    return render(request, 'index.html', {'menu': menu})


def about(request):
    return render(request, 'about.html')


# def login(request):
#     return render(request, 'login.html', {'menu': menu})


def createcase(request):
    active_user = {'user_id': request.user}

    form = AddCaseForm(active_user)
    if request.method == 'POST':
        form = AddCaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showcases')

    data = {
        'form': form,
        'menu': menu
    }
    return render(request, 'createcase.html', data)


class ShowCases(ListView):
    model = Case
    template_name = 'ShowCase.html'
    extra_context = {"name": 'Кейсы', 'menu': menu}

# class DetailCases(DetailView):
#     model = Case
#     slug_field = "url"
#     template_name = 'DetailCase.html'
#     extra_context = {'menu': menu}

def detail_view(request, case_id):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # add the dictionary during initialization
    context["data"] = Case.objects.get(pk=case_id)
    context["menu"] = menu

    return render(request, "DetailCase.html", context)

class ShowPartners(ListView):
    model = Partner
    template_name = 'partners.html'
    extra_context = {'name': 'Партнеры', 'menu': menu}





class LoginUser(LoginView):
    form = LoginUserForm
    template_name = "login.html"
    extra_context = {'menu': menu}

    def get_success_url(self):
        return reverse_lazy('index')


# def RegisterUser(request):
#     if request.method == "POST":
#         login_form = LoginUserForm
#         student_form = UserStudentForm
#         partner_form = UserPartnerForm
#         if login_form.is_valid():
#             # Do the needful
#             return HttpResponseRedirect(reverse('form-redirect'))
#     else:
#         login_form = LoginUserForm
#         student_form = UserStudentForm
#         partner_form = UserPartnerForm
#
#     return render(request, 'register.html', {
#         'login_form': login_form,
#         'student_form': student_form,
#         'partner_form': partner_form})
#
def register(request):
    return render(request, 'register.html',{'menu':menu})


class student_register(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'student_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class partner_register(CreateView):
    model = User
    form_class = PartnerSignUpForm
    template_name = 'partner_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')