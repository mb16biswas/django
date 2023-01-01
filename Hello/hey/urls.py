from django.contrib import admin
from django.urls import path
from hey import views

urlpatterns = [
    path("hey", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'), 
]