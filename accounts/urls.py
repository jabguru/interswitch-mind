from django.urls import path, include
from accounts import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
]