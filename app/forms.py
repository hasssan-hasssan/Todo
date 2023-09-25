from django import forms
from app.models import Task


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'taskDone', 'card_color', 'font_color', 'font_family']
        widgets = {'text':forms.Textarea()}
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label=""
        
        
class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'taskDone', 'card_color', 'font_color', 'font_family']
        widgets = {'text':forms.Textarea()}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label="" 
        
