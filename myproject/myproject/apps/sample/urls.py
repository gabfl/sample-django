from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('hello', views.hello),
    path('world', views.world),
    path('users', views.users),
    path('user/<int:user_id>', views.user),
]
