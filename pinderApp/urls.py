from django.urls import path
from pinderApp import views

urlpatterns = [
    path('', views.landing, name="Inicio"),
 
]