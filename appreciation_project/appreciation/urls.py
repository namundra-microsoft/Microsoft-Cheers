from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('posts/<int:event_id>/', views.post_list, name='post_list'),
    path('create_post/', views.create_post, name='create_post'),
    path('add_reaction/<int:post_id>/', views.add_reaction, name='add_reaction'),
]
