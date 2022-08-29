from django_filters import FilterSet, ModelMultipleChoiceFilter
from .models import User
from projects_skills.models import Skill
from django import forms

class UserFilter(FilterSet):
    skill = ModelMultipleChoiceFilter(field_name='skills__skill', widget=forms.SelectMultiple, queryset=Skill.objects.all())
    # SelectMultiple CheckboxSelectMultiple

    class Meta:
        model = User
        fields = ['is_hirable', 'is_looking', 'expertise_levels', 'experience_years', 'degree', 'country']
