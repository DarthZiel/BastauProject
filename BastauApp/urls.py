from django.urls import path
from .views import ShowCases, ShowPartners,detail_view, student_update, partner_update, ShowCasesPartner, case_update, delete_case, delete_answer, ShowAnswer, ShowAnswerStudent, detail_view_for_Partner
from . import views
from BastauSite import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

    # path('register/',  views.register, name='register'),
    path('createcase/', views.createcase, name= 'createcase'),
    path('showcases/', ShowCases.as_view(), name='showcases'),
    path('showcases/<case_id>', detail_view, name= 'detail_case' ),
    path('bio/student/<user_id>', views.detail_student, name= 'detail_student' ),
    path('bio/partner/<user_id>', views.detail_partner, name= 'detail_partner' ),
    path('mycases/<case_id>', detail_view_for_Partner, name= 'detail_view_for_Partner' ),
    path('ListWinners/', views.ListWinners, name='ListWinners'),
    path('partners/', ShowPartners.as_view(), name='partners'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('personal_partner/<int:pk>', partner_update.as_view(), name='personal_partner'),
    path('personal/student/<int:pk>', student_update.as_view(), name='personal'),
    path('mycases/', views.ShowCasesPartner.as_view(), name='mycases'),
    path('mycases/edit/<int:pk>', views.case_update.as_view(), name='case_update'),
    path('delete/<int:pk>', views.delete_case.as_view(), name='delete_case'),
    path('mycases/answers/<case_id>', views.ShowAnswer, name='show_answer'),
    path('answers/', views.ShowAnswerStudent.as_view(), name='show_answer_student'),
    path('answers/delete/<int:pk>', views.delete_answer.as_view(), name='delete_answer'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.student_register.as_view(), name='student_register'),
    path('partner_register/', views.partner_register.as_view(), name='partner_register'),
    path('mycases/answers/answer/<int:pk>', views.AnswerToCase.as_view(), name='answer'),
    path("search/", views.Search.as_view(), name='search'),
    path('winner/<int:pk>', views.edit, name='winner'),
    path('reset_password/', views.PasswordResetViewBastau.as_view(), name='reset_password'),
    path('reset_password_sent/', views.PasswordResetDoneViewBastau.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmViewBastau.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', views.PasswordResetCompleteViewBastau.as_view(), name='password_reset_complete'),
    path('showcases/<slug:tag_slug>/', views.TagIndexView.as_view(), name='case_by_tag'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)