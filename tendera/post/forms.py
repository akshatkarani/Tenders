from django import forms
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .models import Review

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'item', 'quantity', 'document', 'description', 'elegibility']

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'item', 'quantity', 'document', 'description', 'elegibility']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'document']
