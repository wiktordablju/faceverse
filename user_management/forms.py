from django import forms
from django.contrib.auth.models import User
from .models import Profile


class ProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(widget=forms.FileInput, required=False)

    class Meta:
        model = Profile
        fields = ['bio', 'profile_image']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
