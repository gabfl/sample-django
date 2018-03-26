from django.urls import path
from rest_framework import routers, serializers, viewsets

from . import views

urlpatterns = [
    path('', views.hello),
    path('users', views.users),
    path('user/<int:user_id>', views.user),
]
