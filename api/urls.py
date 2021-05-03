from django.contrib import admin
from django.urls import path,include
from .views import SubmissionsView,Analytics

urlpatterns = [
    path('contact_form/', SubmissionsView.as_view()),
    path('analytics/', Analytics.as_view()),
   
]
