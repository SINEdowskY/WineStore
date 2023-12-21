from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Client, Order
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
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

class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = [
            "client_id",
            "shipment"
        ]