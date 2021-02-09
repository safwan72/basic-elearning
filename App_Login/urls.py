from django.urls import path
from . import views
app_name='App_Login'

urlpatterns = [
    path('ssignup/', views.student_signupview,name='ssignup'),
    path('tsignup/', views.teacher_signupview,name='tsignup'),
    path('s_profile/', views.student_profile_change,name='s_profile'),
    path('t_profile/', views.teacher_profile_change,name='t_profile'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
]
