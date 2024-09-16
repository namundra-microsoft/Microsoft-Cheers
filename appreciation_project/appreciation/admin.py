from django.contrib import admin
from .models import Event, Post, Reaction

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('event', 'author', 'to', 'content', 'is_anonymous', 'created_at')
    list_filter = ('event', 'is_anonymous')

@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'reaction_type')
