from django import forms
from .models import UserImage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ['image']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']