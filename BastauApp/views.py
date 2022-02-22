from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import FormMixin
from .forms import AddCaseForm, StudentSignUpForm, PartnerSignUpForm, LoginUserForm, AddAnswer
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, UpdateView, DeleteView
from .models import *
from django.contrib.auth import logout, login
import datetime

menu = [
    {'title': 'Партнеры', 'url_name': 'partners'},
    {'title': 'Кейсы', 'url_name': 'showcases'},
    {'title': 'Контакты', 'url_name': 'contacts'},
]


def logout_user(request):
    logout(request)
    return redirect('login')


def personal(request):
    return render(request, 'personal.html', {'menu': menu})


def contacts(request):
    return render(request, 'contacts.html', {'menu': menu})


def index(request):
    return render(request, 'index.html', {'menu': menu})


def about(request):
    return render(request, 'about.html')


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
    now = datetime.datetime.now()
    model = Case
    queryset = Case.objects.filter(date_of_close__gte = now)


    template_name = 'ShowCase.html'
    extra_context = {"name": 'Кейсы', 'menu': menu}


class ShowCasesPartner(ListView):
    model = Case
    template_name = 'casepartners.html'
    extra_context = {'menu': menu}


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
def detail_view_for_Partner(request, case_id):
    context = {}
    # add the dictionary during initialization
    context["data"] = Case.objects.get(pk=case_id)
    context["menu"] = menu

    return render(request, "DetailCaseOfPartner.html", context)

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


def register(request):
    return render(request, 'register.html', {'menu': menu})


class student_register(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'student_register.html'
    extra_context = {'menu': menu}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class partner_register(CreateView):
    model = User
    form_class = PartnerSignUpForm
    template_name = 'partner_register.html'
    extra_context = {'menu': menu}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class student_update(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'personal.html'
    success_url = "/"
    extra_context = {'menu': menu}


class partner_update(UpdateView):
    model = Partner
    fields = '__all__'
    success_url = "/"
    template_name = 'personal_partner.html'
    extra_context = {'menu': menu}


class case_update(UpdateView):
    model = Case
    fields = '__all__'
    success_url = "/mycases"
    template_name = 'createcase.html'
    extra_context = {'menu': menu}


class delete_case(DeleteView):
    model = Case
    template_name = 'delete_case.html'
    success_url = "/mycases"
    extra_context = {'menu': menu}



class AnswerToCase(FormMixin, DetailView):
    model = Case
    template_name = 'addanswer.html'
    form_class = AddAnswer
    success_url = '/'
    context_object_name = 'get_case'
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.id_case = self.get_object()
        self.object.id_student = self.request.user
        self.object.save()
        return super().form_valid(form)



# class case_update(UpdateView):
#     model = Case
#     fields = '__all__'
#     template_name = "updatecase.html"
#     extra_context = {'menu':menu}
#     success_url = "personal_partner"

class delete_answer(DeleteView):
    model = Answer
    template_name = 'delete_answer.html'
    success_url = "/mycases"
    extra_context = {'menu': menu}
