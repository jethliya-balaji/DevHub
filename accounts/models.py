from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django_countries.fields import CountryField
import uuid

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        username = self.model.generate_username(first_name, last_name)

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name.capitalize(),
            last_name = last_name.capitalize(),
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id              = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)

    # Addetional fields
    title_tag = models.CharField(max_length=60, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile', default='profile/default.png')
    about = models.TextField(blank=True, null=True, max_length=900)
    country = CountryField(blank=True)
    expertise_levels = models.CharField(max_length=50, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')], blank=True)
    experience_years = models.CharField(max_length=50, choices=[('0-1', '0-1'), ('1-3', '1-3'), ('3-5', '3-5'), ('5-10', '5-10'), ('10+', '10+')], blank=True)
    degree = models.CharField(max_length=50, choices=[('Bachelor', 'Bachelor'), ('Master', 'Master'), ('PhD', 'PhD'), ('Other', 'Other')], blank=True)
    is_looking = models.CharField(max_length=50, choices=(('Remote Job', 'Remote Job'), ('Full Time Job', 'Full Time Job'), ('Part Time Job', 'Part Time Job')), blank=True)
    is_hirable = models.BooleanField(default=False)
    is_hiring_manager = models.BooleanField(default=False)
    
    # social media fields
    linkedin_username = models.CharField(max_length=50, blank=True, null=True)
    github_username = models.CharField(max_length=50, blank=True, null=True)
    twitter_username = models.CharField(max_length=50, blank=True, null=True)
    facebook_username = models.CharField(max_length=50, blank=True, null=True)
    
    # required
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_superadmin   = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

    @classmethod
    def generate_username(self, first_name, last_name):
        username = f'{last_name.lower()}{first_name.lower()}'
        if User.objects.filter(username=username).exists():
            username = f'{last_name.lower()}{first_name.lower()}{User.objects.count()}'
        return username
