from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MDCreationForm(UserCreationForm):
    pid = forms.CharField(max_length = 255)
    class Meta(UserCreationForm.Meta):
        model = MD
        field = ('username','password1','password2','pid')
    
    
    def __init__(self, *args, **kwargs):
        super(MDCreationForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['pid'].widget.attrs['class'] = 'form-control'
        
class MDLoginForm(forms.ModelForm):
    class Meta:
        model = MD
        fields = ['username','password']
        
class RSCreationForm(UserCreationForm):
    # sid = forms.CharField(max_length=255)
    corporation = forms.CharField(max_length=255)
    class Meta(UserCreationForm.Meta):
        model = RS
        field = ('username', 'password1','password2','corporation')
    def __init__(self, *args, **kwargs):
        super(RSCreationForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Login_id'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['corporation'].widget.attrs['class'] = 'form-control'
        self.fields['corporation'].widget.attrs['placeholder'] = "your corporation"

class RSLoginForm(forms.ModelForm):
    class Meta:
        model = RS
        fields = ['username','password']