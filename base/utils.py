from accounts.models import User
from django.db.models import Q

def searchProfiles(request):
    if 'Q' in request.GET:
        search = request.GET['Q'].title()
        if search:
            profiles = User.objects.distinct().filter(
                Q(first_name__icontains=search) |
                Q(first_name__in=search.split(' ')) |
                Q(last_name__icontains=search) |
                Q(last_name__in=search.split(' ')) |
                Q(title_tag__icontains=search) |
                Q(skills__skill__name__icontains=search) |
                Q(skills__skill__name__in=search.split(' '))
            ).exclude(is_hiring_manager=True)
    return profiles