from django import forms
from django.contrib.auth.models import User
from .models import Image, Video, Email


class SignInForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


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
