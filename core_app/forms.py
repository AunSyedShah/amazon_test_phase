from django import forms
from django.contrib.auth.models import User
from .models import Image, Video, Email
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class AuthenticationModelForm(AuthenticationForm):
    class Meta:
        model = User
        fields = "__all__"
        labels = {
            'username': 'Username',
            'password': 'PWD',
        }


class UserCreationModelForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }


class ImageModelForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
        # allow images only
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/jpeg, image/png'}),
        }
        labels = {
            'image': 'Select Image',
        }


class VideoModelForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('video',)
        # allow videos only
        widgets = {
            'video': forms.FileInput(attrs={'accept': 'video/*'}),
        }
        labels = {
            'video': 'Select Video',
        }


class EmailModelForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('name', 'user_email', 'subject', 'message')
        labels = {
            'name': 'Name',
            'user_email': 'Email',
            'subject': 'Subject',
            'message': 'Message',
        }
