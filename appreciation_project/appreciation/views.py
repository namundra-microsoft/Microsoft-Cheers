from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event, Post, Reaction
from .forms import PostForm, EventForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.utils import timezone

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
def create_post(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Get the event from the URL parameter

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.event = event  # Set the event for the post automatically
            post.author = request.user  # Assuming the user is logged in and creating the post
            post.save()
            return redirect('post_list', event_id=event.id)
    else:
        form = PostForm()

    return render(request, 'appreciation/create_post.html', {'form': form, 'event': event})
# def create_post(request, event_id):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('event_list')
#     else:
#         form = PostForm()
#     return render(request, 'appreciation/create_post.html', {'form': form})


@login_required
def add_reaction(request, post_id):
    if request.method == 'POST':
        print(post_id)
        emoji = request.POST.get('emoji')
        post = get_object_or_404(Post, id=post_id)
        reaction, created = Reaction.objects.get_or_create(post=post, user=request.user, reaction_type=emoji)
        res_reaction = {}
        reaction_types = ["Like", "Love", "Laugh", "Wow", "Sad", "Angry"]
        for reaction_type in reaction_types:
            reaction_count = Reaction.objects.filter(post=post, reaction_type=reaction_type).count()
            if reaction_count > 0:
                res_reaction[reaction_type] = reaction_count
        print(res_reaction)
        return JsonResponse(res_reaction)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def event_list(request):
    events = Event.objects.all()
    today = timezone.now().date()
    return render(request, 'appreciation/event_list.html', {'events': events, 'today': today})

# def post_list(request, event_id):
#     event = get_object_or_404(Event, id=event_id)
#     posts = event.posts.all()
#     reaction_emojis = {
#         "Like": "👍",
#         "Love": "❤️",
#         "Laugh": "😂",
#         "Wow": "😮",
#         "Sad": "😢",
#         "Angry": "😡"
#     }
#     res_posts = []
#     reaction_types = ["Like", "Love", "Laugh", "Wow", "Sad", "Angry"]
#     for post in posts:
#         res_reaction = {}
#         for reaction_type in reaction_types:
#             reaction_count = Reaction.objects.filter(post=post, reaction_type=reaction_type).count()
#             if reaction_count > 0:
#                 res_reaction[reaction_emojis[reaction_type]] = reaction_count
#         print(res_reaction)
#         res_posts.append({'post': post, 'reaction': res_reaction})
        
#     return render(request, 'appreciation/post_list.html', {'event': event, 'posts': res_posts})

def post_list(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    posts = event.posts.all()
    reaction_emojis = {
        "Like": "👍",
        "Love": "❤️",
        "Laugh": "😂",
        "Wow": "😮",
        "Sad": "😢",
        "Angry": "😡"
    }
    res_posts = []
    reaction_types = ["Like", "Love", "Laugh", "Wow", "Sad", "Angry"]
    for post in posts:
        res_reaction = {}
        for reaction_type in reaction_types:
            reaction_count = Reaction.objects.filter(post=post, reaction_type=reaction_type).count()
            if reaction_count > 0:
                res_reaction[reaction_emojis[reaction_type]] = reaction_count
        print(res_reaction)
        res_posts.append({'post': post, 'reaction': res_reaction})

    # Determine if the event is active
    is_active = event.end_date >= timezone.now().date()

    return render(request, 'appreciation/post_list.html', {'event': event, 'posts': res_posts, 'is_active': is_active})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Redirect to the event list after creation
    else:
        form = EventForm()
    return render(request, 'appreciation/create_event.html', {'form': form})

def team_members(request):
    users = User.objects.all()  # Get all the users from the database
    return render(request, 'appreciation/team_members.html', {'users': users})