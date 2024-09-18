from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('posts/<int:event_id>/', views.post_list, name='post_list'),
    path('create_post/', views.create_post, name='create_post'),
    path('add_reaction/<int:post_id>/', views.add_reaction, name='add_reaction'),
    path('create_event/', views.create_event, name='create_event'),
    path('team/', views.team_members, name='team_members'),  # New path for team members
    path('create_post/<int:event_id>/', views.create_post, name='create_post'),
    path('posts/<int:event_id>/my_posts/', views.view_my_posts, name='view_my_posts'),
    path('event/<int:event_id>/participants/', views.event_participants, name='event_participants'),
]
