from django import forms
from .models import MD
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MDCreationForm(UserCreationForm):
    pid = forms.CharField(max_length = 255)
    class Meta(UserCreationForm.Meta):
        model = User
        field = ('username','pid')
