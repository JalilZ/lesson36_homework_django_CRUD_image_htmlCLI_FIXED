from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('students/', views.students),
    path('students/<int:id>', views.students),
]
