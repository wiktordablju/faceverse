from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from group_management.models import Group
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
    my_groups = Group.objects.filter(members=request.user)
    group_posts = Post.objects.filter(group__in=my_groups)
    followed_user_posts = Post.objects.filter(
        author__in=User.objects.filter(followers__follower=request.user),
        group__isnull=True
    )
    all_posts = group_posts | followed_user_posts | Post.objects.filter(author=request.user)
    user_posts = all_posts.distinct().order_by('-created_at')
    form = PostForm()

    context = {
        'form': form,
        'posts': user_posts
    }

    return render(request, 'core/home.html', context)



