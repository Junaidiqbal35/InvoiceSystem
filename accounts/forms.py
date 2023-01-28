from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.forms import PasswordInput

from accounts.models import User, OrderItems


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


