from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Post(models.Model):
    event = models.ForeignKey(Event, related_name='posts', on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    to = models.ForeignKey(User, null=True, blank=True, related_name='received_posts', on_delete=models.SET_NULL)
    content = models.TextField()
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f'Post by {self.author.username if self.author else "Anonymous"} to {self.to.username if self.to else "No One"}'

class Reaction(models.Model):
    post = models.ForeignKey(Post, related_name='reactions', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reaction_type = models.CharField(max_length=50)  # e.g., "Like", "Love"

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f'Reaction by {self.user.username} on Post {self.post.id}'
