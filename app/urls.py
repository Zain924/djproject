from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.index , name = 'home' ),
    path('projects/', views.add, name ='projects'),
    path('download-cv/', views.download_cv, name='download_cv')
]