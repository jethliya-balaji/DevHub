from django.urls import path
from . import views

urlpatterns = [
    path('edit/skill/', views.EditSkillView, name='edit_skill'),
    path('add/skill/', views.AddSkillView, name='add_skill'),
    path('edit/project/', views.EditProjectView, name='edit_project'),
    path('add/project/', views.AddProjectView, name='add_project'),
]