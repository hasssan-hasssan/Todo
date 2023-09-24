from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from app.models import Task

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'taskDone']
        widgets = {'text':forms.Textarea()}
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label=""
        
        

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'taskDone']
        widgets = {'text':forms.Textarea()}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label=""