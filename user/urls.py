from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('login_for_medal/', views.login_for_medal, name='login_for_medal'),
    path('logout/', views.logout, name='logout'),
    path('user_info/', views.user_info, name="user_info"),
    path('change_nickname/', views.change_nickname, name = 'change_nickname')
]