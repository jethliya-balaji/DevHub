from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import UserSkillForm, ProjectForm
from .models import UserSkill, Project


# Create your views here.

@login_required
def EditSkillView(request):
    UserSkillFormSet = modelformset_factory(UserSkill, form=UserSkillForm, can_delete=True, extra=0)
    formset = UserSkillFormSet(request.POST or None, queryset=request.user.skills.all())
    if formset.is_valid():
        for form in formset:
            if form.is_valid() and form.has_changed():
                if form.cleaned_data['DELETE']:
                    form.instance.delete()
                    messages.success(request, 'Skill Removed')
                else:
                    instance = form.save(commit=False)
                    instance.user = request.user
                    instance.save()
                    messages.success(request, 'Skill Saved')
        return redirect('account')
    return render(request, 'projects_skills/edit_skill.html', {'formset': formset})

@login_required
def AddSkillView(request):
    form = UserSkillForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Skill Added!')
        return redirect('account')
    return render(request, 'projects_skills/add_skill.html', {'form': form})

@login_required
def EditProjectView(request):
    ProjectFormSet = modelformset_factory(Project, form=ProjectForm, can_delete=True, extra=0)
    formset = ProjectFormSet(request.POST or None, queryset=request.user.projects.all())
    if formset.is_valid():
        for form in formset:
            if form.is_valid() and form.has_changed():
                if form.cleaned_data['DELETE']:
                    form.instance.delete()
                    messages.success(request, 'Project Removed')
                else:
                    instance = form.save(commit=False)
                    instance.user = request.user
                    instance.save()
                    messages.success(request, 'Project Saved')
        return redirect('account')
    return render(request, 'projects_skills/edit_project.html', {'formset': formset})

@login_required
def AddProjectView(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Project Added!')
        return redirect('account')
    return render(request, 'projects_skills/add_project.html', {'form': form})
