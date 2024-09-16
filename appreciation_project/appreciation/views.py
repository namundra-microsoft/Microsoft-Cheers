from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event, Post, Reaction
from .forms import PostForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('event_list')
    else:
        form = PostForm()
    return render(request, 'appreciation/create_post.html', {'form': form})

@login_required
def add_reaction(request, post_id):
    if request.method == 'POST':
        emoji = request.POST.get('emoji')
        post = get_object_or_404(Post, id=post_id)
        reaction, created = Reaction.objects.get_or_create(post=post, user=request.user, emoji=emoji)
        reactions_count = Reaction.objects.filter(post=post, emoji=emoji).count()
        return JsonResponse({'reactions_count': reactions_count, 'emoji': emoji})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def event_list(request):
    events = Event.objects.all()
    return render(request, 'appreciation/event_list.html', {'events': events})

def post_list(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    posts = event.posts.all()
    return render(request, 'appreciation/post_list.html', {'event': event, 'posts': posts})
