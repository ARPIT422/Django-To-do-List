from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):   #this class makes from the model and includes all the fields of it
    class Meta:
        model = Todo
        fields = "__all__"