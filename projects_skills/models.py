from django.db import models
from accounts.models import User

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    def __str__(self):
        return self.name

class UserSkill(models.Model):
    user = models.ForeignKey(User, related_name='skills', on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True, max_length=320)

    class Meta:
        verbose_name_plural = 'User Skills'
        verbose_name = 'User Skill'
        unique_together = ('user', 'skill')
    
    def __str__(self):
        return f'{self.user.get_full_name()} > {self.skill.name}'

class Project(models.Model):
    user = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=320)
    demo_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
