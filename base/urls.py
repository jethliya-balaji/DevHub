from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('search/', views.SearchView, name='search'),
    path('profile/<str:username>/', views.ProfileView, name='profile'),
    path('profile/<str:pk>', views.HBDProfileView, name='hdbprofile'),
    path('save/profile/<str:username>/', views.SaveProfile, name='save_profile'),
    path('saved/', views.SavedProfiles, name='saved_profiles'),
    path('remove/profile/<str:username>/', views.RemoveProfile, name='remove_profile'),
]