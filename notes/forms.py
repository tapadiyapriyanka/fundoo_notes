from django import forms
from .models import Notes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.admin import widgets

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email') #'last_name', 'email', 'password')

class registrationForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput( attrs = {'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Last Name'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Email Address'}))
    username = forms.CharField(max_length=20, required=True, widget=forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Username'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput( attrs = {'class':'form-control', 'placeholder':'Password'}))
    confirmPassword = forms.CharField(max_length=32, widget=forms.PasswordInput( attrs = {'class':'form-control', 'placeholder':'Confirm Password'}))

class loginForm(forms.Form):
    username = forms.CharField(max_length=20, required=True, widget=forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Username'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput( attrs = {'class':'form-control', 'placeholder':'Password'}))


class create_note_form(forms.ModelForm):
    class Meta:
        model = Notes
        widgets = {
          'description': forms.Textarea(attrs={'rows':1, 'cols':25})
        }
        fields = ('title', 'description', 'is_pinned', 'color')

class update_note_form(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Notes
        fields = ['id', 'title', 'description', 'is_pinned', 'color']

class DateInput(forms.DateInput):
    input_type = 'date'

class reminder_form(forms.ModelForm):
    mydate = forms.DateField(widget=widgets.AdminDateWidget)
    class Meta:
        model = Notes
        fields = ['mydate']
        


# class note_pin_form(forms.ModelForm):
#     class Meta:
#         model = Notes
#         fields = ('is_pinned')
