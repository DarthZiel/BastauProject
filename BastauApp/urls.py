from django.urls import path
from .views import RegisterUser, ShowCases, ShowPartners
from . import views
from BastauSite import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('register/',RegisterUser.as_view(),name='register'),
    path('login/',views.login,name='login'),
    path('createcase/',views.createcase,name = 'createcase'),
    path('showcases/',ShowCases.as_view(),name='showcases'),
    path('contacts/',views.contacts,name='contacts'),
    # path('personal/',views.personal,name='personal'),
    path('personal/',views.LoginUser.as_view(),name='personal'),
    path('partners/',ShowPartners.as_view(),name='partners')
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)