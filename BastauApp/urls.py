from django.urls import path
from .views import RegisterUser, ShowCases
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('register/',RegisterUser.as_view(),name='register'),
    path('login/',views.login,name='login'),
    path('createcase/',views.createcase,name = 'createcase'),
    path('showcases/',ShowCases.as_view(),name='showcases'),
    path('contacts/',views.contacts,name='contacts')
]   