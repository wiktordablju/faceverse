from django import forms
from .models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']
        labels = {
            'name': "Nazwa",
            'description': 'Opis',
        }


class GroupEditForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description', 'profile_image']
