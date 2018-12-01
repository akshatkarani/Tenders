from django import forms
from .models import Advert


class AdvertCreateForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ['name', 'image','hours','email', 'address', 'products', 'details']

class AdvertUpdateForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ['name', 'image','hours','email', 'address', 'products', 'details']
