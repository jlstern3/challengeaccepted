from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('users/register', views.register),
    path('users/create_user', views.create_user),
    path('users/logout', views.logout),
    path('main_page', views.main_page),
    path('users/login', views.login),
    path('users/profile/<int:user_id>', views.user_profile),
    path('users/profile/<int:user_id>/edit', views.edit_profile),
    path('challenges', views.challenges),
    path('challenges/accept/<int:challenge_id>', views.accept_challenge),
    path('challenge_search', views.challenge_search),
    path('challenges/details/<int:challenge_id>', views.challenge_details),
]