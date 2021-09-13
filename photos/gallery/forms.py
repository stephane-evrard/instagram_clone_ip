from crispy_forms.helper import FormHelper
from django import forms
from .models import Image, Comment, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from registration.forms import RegistrationForm

from django.forms.utils import flatatt

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
  