from django import forms
from .models import Post, Reaction, Event

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['event', 'to', 'content', 'is_anonymous']
        # widgets = {
        #     'to': forms.Select(choices=[(user.id, user.username) for user in User.objects.all()]),
        # }

class ReactionForm(forms.ModelForm):
    class Meta:
        model = Reaction
        fields = ['reaction_type']
        #fields = ['emoji']
        # widgets = {
        #     'emoji': forms.HiddenInput()  # Hide the input field since we will use buttons
        # }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'start_date', 'end_date']