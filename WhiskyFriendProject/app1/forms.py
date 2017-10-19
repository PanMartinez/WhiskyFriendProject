from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Slainteet, Order


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Pole opcjonalne.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Pole opcjonalne.')
    email = forms.EmailField(max_length=254, help_text='Pole obowiązkowe.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class CreateSlainteetForm(forms.ModelForm):
    class Meta:
        model = Slainteet
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput,
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('quantity',)
