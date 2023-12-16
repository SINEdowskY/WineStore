from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Client

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = [
            "first_name",
            "last_name",
            "date_of_birth", 
            "address_street", 
            "address_number", 
            "address_apartament_number",
            "zip_code",
            "phone_number"
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }