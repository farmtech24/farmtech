
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserLoginForm(AuthenticationForm):
    """
    Form for user login.
    """
    username = forms.CharField(label='Nombre de usuario', max_length=150)
    password = forms.CharField(label='Contraseña', strip=False, widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
    """
    Form for user registration.
    """
    username = forms.CharField(label='Nombre de usuario', max_length=150)
    password1 = forms.CharField(label='Contraseña', strip=False, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', strip=False, widget=forms.PasswordInput)
    farm_name = forms.CharField(label='Nombre de la finca', max_length=100)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2', 'farm_name']
