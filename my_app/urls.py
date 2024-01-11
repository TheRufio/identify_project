from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), # home
    path('registration', views.registration)
]