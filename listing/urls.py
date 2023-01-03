from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('submit/', views.submit),
    path('genres/', views.genres),
    path('listing/', views.listing),
]