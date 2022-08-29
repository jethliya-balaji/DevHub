from pickle import FALSE
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, RegistrationForm, UserForm

# Create your views here.

def LoginView(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            first_time_login = user.last_login == user.date_joined
            login(request, user)
            messages.success(request, 'You are now logged in')
            if request.GET.get('next'):
                return redirect(request.GET['next'])
            elif first_time_login:
                return redirect('edit_account')
            else:
                return redirect('home')
            
    return render(request, 'accounts/login.html', {'form': form})

def RegisterView(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        if request.POST.get('account_type') == 'True':
            user.is_hiring_manager = True
        form.save()
        messages.success(request, 'You are now registered and can log in.')
        return redirect('login')

    return render(request, 'accounts/register.html' , {'form': form})

@login_required
def AccountView(request):
    user = request.user
    return render(request, 'accounts/account.html', {'user': user})

@login_required
def EditAccountView(request):
    user = request.user
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated.')
            return redirect('account')
    else:
        form = UserForm(instance=user)
    return render(request, 'accounts/edit_account.html', {'form': form})
