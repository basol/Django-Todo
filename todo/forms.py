from django import forms
from .models import Todo


class CreateTodoForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    is_completed = forms.BooleanField(required=False)


class CreateTodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text', 'is_completed']