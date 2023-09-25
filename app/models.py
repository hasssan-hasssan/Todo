from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """ Tasks model """
    
    text = models.CharField(max_length=250)
    taskDone = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Each user has own tasks
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    # Personalize task
    BG_COLOR_CHOICES = (
        ('default', 'Default'),
        ('bg-primary','Primary'),
        ('bg-secondary', 'Secondary'),
        ('bg-success', 'Success'),
        ('bg-danger', 'Danger'),
        ('bg-warning', 'Warning'),
        ('bg-info', 'Info'),
        ('bg-light', 'Light'),
        ('bg-dark', 'Dark'),
        ('bg-white', 'White'),
    )

    TEXT_COLOR_CHOICES = (
        ('default', 'Default'),
        ('text-primary','Primary'),
        ('text-secondary', 'Secondary'),
        ('text-success', 'Success'),
        ('text-danger', 'Danger'),
        ('text-warning', 'Warning'),
        ('text-info', 'Info'),
        ('text-light', 'Light'),
        ('text-dark', 'Dark'),
        ('text-white', 'White'),
    )
    
    FONT_FAMILY_CHOICES = (
        ('default', 'Default'),
        ('Consolas','Consolas'),
        ('Segoe Print','Segoe Print'),
        ('Gabriola','Gabriola'),
    )
    
    card_color = models.CharField(max_length=14, choices=BG_COLOR_CHOICES, default='default')
    font_color = models.CharField(max_length=14, choices=TEXT_COLOR_CHOICES, default='default')
    font_family = models.CharField(max_length=14, choices=FONT_FAMILY_CHOICES, default='default')   
    
    def __str__(self):
        return self.text[:100]
