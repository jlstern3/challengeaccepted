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
    path('users/profile/<int:user_id>/update', views.update_profile),
    path('challenges', views.challenges),
    path('checked_box', views.checked_box),
    path('challenges/accept/<int:challenge_id>', views.accept_challenge),
    path('challenge_search', views.challenge_search),
    path('challenges/details/<int:challenge_id>', views.challenge_details),
    path('challenges/remove_accepted/<int:challenge_id>', views.remove_accepted_challenge),
    path('challenges/complete/<int:challenge_id>', views.challenge_complete),
    path('challenges/remove_completed/<int:challenge_id>', views.remove_completed_challenge),
]