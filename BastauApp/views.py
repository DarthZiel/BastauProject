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
from .filters import CaseFilter
import datetime
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
menu = [
    {'title': 'Партнеры', 'url_name': 'partners'},
    {'title': 'Кейсы', 'url_name': 'showcases'},
    {'title': 'Победители', 'url_name': 'ListWinners'},
]
def register(request):
    context = {}
    # add the dictionary during initialization
    context["menu"] = menu

    return render(request, "register.html", context)

class Categories(ListView):
    def get_cat(self):
        return Category.objects.all()


def logout_user(request):
    logout(request)
    return redirect('login')


def personal(request):
    context = {}
    # add the dictionary during initialization
    context["menu"] = menu

    return render(request, "personal.html", context)


def ListWinners(request):
    context = {'menu': menu}
    context['data'] = Answer.objects.filter(is_won=True)

    return render(request, 'ListWinners.html',context)


def index(request):

    return render(request, 'index.html', {'menu': menu})


def about(request):
    return render(request, 'about.html')

# def createcase(request):
#     active_user = {'user_id': request.user.partner}
#
#     form = AddCaseForm(active_user)
#     if request.method == 'POST':
#         form = AddCaseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('showcases')
#     data = {
#         'form': form,
#         'menu': menu,
#
#     }
#     return render(request, 'createcase.html', data)
class createcase(CreateView, ListView):
    model = Case
    form_class = AddCaseForm
    template_name = 'createcase.html'
    success_url = "/showcases"
    context_object_name = "partners"
    extra_context = {
        'menu': menu,
    }

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.user_id = Partner.objects.get(user=self.request.user)
        self.object.save()
        return super().form_valid(form)

class ShowCases(ListView):
    # now = datetime.datetime.now()
    model = Case
    template_name = 'ShowCase.html'
    paginate_by = 6
    context_object_name = 'orders'
    extra_context = {"name": 'Кейсы', 'menu': menu}

    def get_queryset(self):
        now = datetime.datetime.now()
        qs = Case.objects.all().filter(is_published=True, date_of_close__gte=now)
        case = CaseFilter(self.request.GET, queryset=qs)
        return case.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CaseFilter(self.request.GET, queryset=self.get_queryset())
        return context

class ShowCasesPartner(ListView):
    model = Case
    context_object_name = 'case'
    template_name = 'casepartners.html'
    extra_context = {'menu': menu}
    paginate_by = 6
    def get_queryset(self):
        queryset = Case.objects.filter(user_id=self.request.user.partner)
        return queryset

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
    paginate_by = 5
    extra_context = {'name': 'Партнеры', 'menu': menu}

class LoginUser(LoginView):
    form = LoginUserForm
    template_name = "login.html"
    extra_context = {'menu': menu}

    def get_success_url(self):
        return reverse_lazy('index')

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

class student_update(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'personal.html'
    success_url = "/"
    extra_context = {'menu': menu}


class partner_update(UpdateView):
    model = Partner
    fields = ['Fio', 'name_of_partner', 'site', 'avatar', 'about_company']
    success_url = "/"
    context_object_name = 'partner'
    template_name = 'personal_partner.html'
    extra_context = {'menu': menu}


class case_update(UpdateView):
    model = Case
    fields = '__all__'
    success_url = "/mycases"
    template_name = 'updatecase.html'
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
    extra_context = {'menu': menu}
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.id_case = self.get_object()
        self.object.id_student = Student.objects.get(user=self.request.user)
        self.object.is_won = False
        self.object.save()
        return super().form_valid(form)


class delete_answer(DeleteView):
    model = Answer
    template_name = 'delete_answer.html'
    success_url = "/answers"
    extra_context = {'menu': menu}

def ShowAnswer(request, case_id):
    context = {}
    # add the dictionary during initialization
    context["data"] = Case.objects.get(pk=case_id)
    context["menu"] = menu
    return render(request,'showanswer.html', context)

class ShowAnswerStudent(ListView):
    model = Answer
    template_name = 'showanswer_student.html'
    extra_context = {'name': 'Ответы', 'menu': menu}

    def get_queryset(self):
        queryset = Answer.objects.filter(id_student=self.request.user.student)
        return queryset


def detail_student(request, user_id):
    a = User.objects.get(pk=user_id)
    context = {}
    context["student_info"] = Student.objects.get(user=a)
    context["menu"] = menu
    return render(request, "Bio_student.html", context)

def detail_partner(request, user_id):
    a = User.objects.get(pk=user_id)
    context = {}
    context["partner_info"] = Partner.objects.get(user=a)
    context["menu"] = menu
    return render(request, "Bio_partner.html", context)


class TagIndexView(ListView):
    template_name = 'ShowCase.html'
    model = Case
    extra_context = {'name': 'Партнеры', 'menu': menu}
    def get_queryset(self):
        queryset = Case.objects.filter(tags__slug= self.kwargs.get('tag_slug'))
        return queryset

class PasswordResetViewBastau(PasswordResetView):
    template_name = "reset_password/password_reset.html"
    extra_context = {'menu': menu}

class PasswordResetDoneViewBastau(PasswordResetDoneView):
    template_name="reset_password/password_reset_sent.html"
    extra_context = {'menu': menu}

class PasswordResetConfirmViewBastau(PasswordResetConfirmView):
    template_name="reset_password/password_reset_form.html"
    extra_context = {'menu': menu}

class PasswordResetCompleteViewBastau(PasswordResetCompleteView):
    template_name = "reset_password/password_reset_done.html"
    extra_context = {'menu': menu}

def edit(request, pk):
    answer = Answer.objects.get(id=pk)
    if answer.is_won == False:
        answer.is_won = True
        answer.save()
        return render(request, 'winner.html')
    else:
        return HttpResponse('ты дебил? ты уже его выбрал')

