from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from post_management.forms import PostForm
from post_management.models import Post


def welcome(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('core:home')
    else:
        form = AuthenticationForm()

    return render(request, 'core/welcome.html', {'form': form})


@login_required(login_url='core:welcome')
def home(request):
    followed_users = User.objects.filter(followers__follower=request.user)
    user_posts = Post.objects.filter(author__in=followed_users | User.objects.filter(username=request.user.username)).distinct().order_by('-created_at')

    form = PostForm()
    context = {
        'form': form,
        'posts': user_posts
    }
    return render(request, 'core/home.html', context)
