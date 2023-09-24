from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """ Tasks model """
    text = models.CharField(max_length=250)
    taskDone = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Each user has own tasks
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.text[:100]


class UiSetting(models.Model):
    uiSettings = models.JSONField(null=True, blank=True) # Each user can customize own UI, for example : color, font , radius and etc
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"UI Setting of {str(self.author.username)}"