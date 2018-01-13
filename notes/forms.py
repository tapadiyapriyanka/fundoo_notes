from django import forms
from .models import Notes
from django.forms import PasswordInput

# class signupform(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = userdetails
#         fields = ('username', 'email', 'password')

class signupform(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    email     = forms.EmailField(label='Enter Email', max_length=100)
    password  = forms.CharField(widget=forms.PasswordInput, label="Enter password", max_length=20)

class create_note_form(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'description', 'is_pinned', 'color')

# class note_pin_form(forms.ModelForm):
#     class Meta:
#         model = Notes
#         fields = ('is_pinned')
