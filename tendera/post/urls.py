from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='post-home'),
    path('about/', views.about, name='post-about'),
]