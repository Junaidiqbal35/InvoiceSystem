from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('vendee/signup/', views.VendeeSignUpView.as_view(), name='vendee_signup'),
]
