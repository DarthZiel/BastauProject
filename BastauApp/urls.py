from django.urls import path
from .views import ShowCases, ShowPartners,detail_view, student_update
from . import views
from BastauSite import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/',  views.register, name='register'),
    path('createcase/', views.createcase, name= 'createcase'),
    path('showcases/', ShowCases.as_view(), name='showcases'),
    path('showcases/<case_id>', detail_view, name= 'detail_case' ),
    path('contacts/', views.contacts, name='contacts'),
    path('partners/', ShowPartners.as_view(), name='partners'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('<pk>/personal/',student_update.as_view(), name='personal'),
    path('logout/', views.logout_user, name='logout'),
    path('student_register/', views.student_register.as_view(), name='student_register'),
    path('partner_register/', views.partner_register.as_view(), name='partner_register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)