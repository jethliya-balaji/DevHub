from django.db import models
from accounts.models import User

# Create your models here.

class SavedProfile(models.Model):
    user = models.ForeignKey(User, related_name='saved_profiles', on_delete=models.CASCADE)
    profile = models.ForeignKey(User, related_name='saved_by', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'profile')

    def __str__(self):
        return f'{self.user} saved {self.profile}'
