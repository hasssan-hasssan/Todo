from django import forms
from app.models import Task

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'taskDone']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label=""