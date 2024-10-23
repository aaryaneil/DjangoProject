from django.urls import path
from . import views

app_name = 'Loginify'

urlpatterns = [
    path('sign-up/', views.signup, name='signup'),
    path('log-in/', views.login, name='login'),
    path('users/', views.getAllUsers, name='get_all_users'),
    path('users/<str:email>/', views.getUserByEmail, name='get_user'),
    path('users/update/<str:email>/', views.updateUser, name='update_user'),
    path('users/delete/<str:email>/', views.deleteUser, name='delete_user'),
]