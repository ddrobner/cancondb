from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('submit/', views.submit),
    path('artists/<slug:artist_id>/', views.artist_view),
    path('genres/<slug:genre_id>/', views.genre_view),
    path('genres/', views.genres),
    path('listing/', views.listing),
]