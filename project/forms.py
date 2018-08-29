from django import forms
#from models import Community_post
from django.contrib.auth.models import User



class Signup_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class Login_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'id', 'placeholder': 'ID', 'autocomplete': 'off'}),
            'password': forms.PasswordInput(attrs={'class': 'pwd', 'placeholder': 'Enter the password', 'autocomplete': 'off'})

        }
        labels = {
            'username': '',
            'password': ''
        }
        help_texts = {
            'username': None
        }