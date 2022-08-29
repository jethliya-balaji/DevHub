from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.LoginView, name='login'),
    path('register/', views.RegisterView, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('account/', views.AccountView, name='account'),
    path('edit/account/', views.EditAccountView, name='edit_account'),
]