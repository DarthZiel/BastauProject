from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import AddCaseForm,StudentSignUpForm, PartnerSignUpForm,LoginUserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, UpdateView
from .models import *
from django.contrib.auth import logout, login

menu = [
    {'title': 'Партнеры', 'url_name': 'partners'},
    {'title': 'Кейсы', 'url_name': 'showcases'},
    {'title': 'Контакты', 'url_name': 'contacts'},
]


def logout_user(request):
    logout(request)
    return redirect('login')

def personal(request):
    return render(request, 'personal.html',{'menu':menu})



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

class ShowCasesPartner(ListView):
    model = Case
    template_name = 'casepartners.html'
    extra_context = { 'menu': menu}


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



def register(request):
    return render(request, 'register.html',{'menu':menu})


class student_register(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'student_register.html'
    extra_context = {'menu':menu}
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

    def upload_file(request):
        if request.method == 'POST':
            form = PartnerSignUpForm(request.POST, request.FILES)
            if form.is_valid():

                instance.save()
                return HttpResponseRedirect('/success/url/')
        else:
            form = UploadFileForm()
        return render(request, 'upload.html', {'form': form})

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
