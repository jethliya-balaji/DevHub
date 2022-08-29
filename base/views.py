from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.filters import UserFilter
from accounts.models import User
from .models import SavedProfile
from .utils import searchProfiles
from .harperdb_service import get_all_users, get_user_by_id
from .linkedin_data import get_linkedin_data

# Create your views here.
@login_required
def HomeView(request):
    profiles = get_all_users()
    return render(request, 'base/home.html' , {'profiles': profiles})

@login_required
def HBDProfileView(request, pk):
    profile = get_user_by_id(pk)
    HDB = True
    return render(request, 'base/profile.html', {'profile': profile, 'HDB': HDB})

@login_required
def SearchView(request):
    if 'Q' in request.GET:
        search = request.GET['Q']
        if search:
            profiles = searchProfiles(request)
            profileFilter = UserFilter(request.GET, queryset=profiles)
            profiles = profileFilter.qs.exclude(id=request.user.id)
            return render(request, 'base/searched.html', {'profiles': profiles, 'search': search, 'filter': profileFilter})
    return redirect('home')

@login_required
def ProfileView(request, username):
    try:
        context = {}
        profile = User.objects.get(username=username)
        if profile.is_hiring_manager:
            return redirect('home')
        if profile.id == request.user.id:
            return redirect('account')
        if profile.linkedin_username:
            linkedinName, linkedinHeadline, linkedinIndustryName, linkedinSummary, linkedinGeoCountryName, linkedinEducation, linkedinExperience = get_linkedin_data(profile.linkedin_username)
            context.update({'linkedinName':linkedinName, 'linkedinHeadline':linkedinHeadline, 'linkedinIndustryName':linkedinIndustryName, 'linkedinSummary':linkedinSummary, 'linkedinGeoCountryName':linkedinGeoCountryName, 'linkedinEducation':linkedinEducation, 'linkedinExperience':linkedinExperience})
        saved = SavedProfile.objects.filter(user=request.user, profile=profile).exists()
        context.update({'profile': profile, 'saved': saved})
        return render(request, 'base/profile.html', context)
    except User.DoesNotExist:
        messages.error(request, 'Profile not found')
        return redirect('home')

@login_required
def SaveProfile(request, username):
    if request.user.is_hiring_manager:
        profile = User.objects.get(username=username)
        SavedProfile.objects.get_or_create(user=request.user, profile=profile)
        messages.success(request, f'Profile saved successfully!')
        return redirect('profile', username=username)
    messages.error(request, 'You do not have permission for this action.')
    return redirect('profile', username=username)

@login_required
def SavedProfiles(request):
    if request.user.is_hiring_manager:
        profiles = SavedProfile.objects.filter(user=request.user)
        return render(request, 'base/saved_profiles.html', {'profiles': profiles})
    messages.error(request, 'You do not have permission for this action.')
    return redirect('home')

@login_required
def RemoveProfile(request, username):
    if request.user.is_hiring_manager:
        profile = User.objects.get(username=username)
        SavedProfile.objects.filter(user=request.user, profile=profile).delete()
        messages.success(request, f'Profile removed successfully!')
        return redirect('profile', username=username)
    messages.error(request, 'You do not have permission for this action.')
    return redirect('home')
