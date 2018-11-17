from django import forms
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'item', 'quantity', 'document', 'description']

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'item', 'quantity', 'document', 'description']