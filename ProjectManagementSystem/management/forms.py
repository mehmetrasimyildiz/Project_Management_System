from django import forms
from .models import Task ,Developer

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['recorded_at']

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = '__all__'