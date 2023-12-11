from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from post_management.forms import PostForm
from post_management.models import Post


@login_required(login_url='core:welcome')
def profile(request):
    return render(request, 'user_management/profile.html')


@login_required(login_url='core:welcome')
def friends(request):
    return render(request, 'user_management/friends.html')


def logout_view(request):
    logout(request)
    return redirect('core:welcome')


@login_required(login_url='core:welcome')
def profile(request):
    # Pobierz tylko posty użytkownika na jego profilu
    user_posts = Post.objects.filter(author=request.user, group__isnull=True).order_by('-created_at')
    form = PostForm()

    context = {
        'form': form,
        'posts': user_posts,
    }
    return render(request, 'user_management/profile.html', context)
