from django.forms import ModelForm
from .models import UserSkill, Project

class UserSkillForm(ModelForm):
    class Meta:
        model = UserSkill
        fields = ['skill', 'description']

    def clean_description(self):
        description = self.cleaned_data['description'].capitalize()
        return description

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'demo_link', 'github_link']

    def clean_name(self):
        name = self.cleaned_data['name'].capitalize()
        return name

    def clean_description(self):
        description = self.cleaned_data['description'].capitalize()
        return description