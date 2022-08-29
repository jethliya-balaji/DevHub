from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email", "password")

    def clean_email(self):
        return self.cleaned_data['email'].lower()

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                try:
                    user = User.objects.get(email=email)
                    if not user.is_active:
                        raise forms.ValidationError("The account You tried to Sign in with is not an active account.")
                except User.DoesNotExist:
                    raise forms.ValidationError({'email': ["No such email is registered."]})
                raise forms.ValidationError({'password': ["Incorrect password."]})


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")

    def clean_first_name(self):
        return self.cleaned_data['first_name'].capitalize()
    
    def clean_last_name(self):
        return self.cleaned_data['last_name'].capitalize()
    
    def clean_email(self):
        return self.cleaned_data['email'].lower()

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        user.username = User.generate_username(first_name, last_name)

        if commit:
            user.save()
        return user

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "is_hirable", "is_looking", "profile_image", "title_tag", "about", "country", "expertise_levels", "experience_years", "degree", "facebook_username", "linkedin_username", "twitter_username", "github_username") 

    def clean_first_name(self):
        return self.cleaned_data['first_name'].capitalize()

    def clean_last_name(self): 
        return self.cleaned_data['last_name'].capitalize()

    def clean_email(self):
        return self.cleaned_data['email'].lower()

    def clean_title_tag(self):
        if self.cleaned_data['title_tag']:
            return self.cleaned_data['title_tag'].title()

    def clean_about(self):
        return self.cleaned_data['about'].capitalize()
    
    def clean_facebook_username(self):
        if self.cleaned_data['facebook_username']:
            return self.cleaned_data['facebook_username'].lower()

    def clean_twitter_username(self):
        if self.cleaned_data['twitter_username']:
            return self.cleaned_data['twitter_username'].lower()

    def clean_linkedin_username(self):
        if self.cleaned_data['linkedin_username']:
            return self.cleaned_data['linkedin_username'].lower()
    
    def clean_github_username(self):
        if self.cleaned_data['github_username']:
            return self.cleaned_data['github_username'].lower()