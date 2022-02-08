from django.urls import path
from .views import ShowCases, ShowPartners,  SignUpView,LoginUser
from . import views
from BastauSite import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/',  SignUpView.as_view(), name='signup'),
    path('createcase/', views.createcase, name = 'createcase'),
    path('showcases/', ShowCases.as_view(), name='showcases'),
    path('contacts/', views.contacts, name='contacts'),
    path('partners/', ShowPartners.as_view(), name='partners'),
    path('login/', LoginUser.as_view(), name='login'),
    path('personal/', views.personal, name='personal'),
    path('logout/',views.logout_user,name='logout'),]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)