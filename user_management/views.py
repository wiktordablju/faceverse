from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from post_management.forms import PostForm
from post_management.models import Post
from user_management.forms import ProfileForm, UserEditForm
from user_management.models import Follow


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
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile_user = get_object_or_404(User, username=username)
    user_posts = Post.objects.filter(author=user, group__isnull=True).order_by('-created_at')
    user_groups = user.user_groups.all()
    form = PostForm()
    is_own_profile = (request.user == user)

    context = {
        'user': user,
        'posts': user_posts,
        'user_groups': user_groups,
        'is_own_profile': is_own_profile,
        'form': form,
        'profile_user': profile_user
    }
    return render(request, 'user_management/profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Twój profil został zaktualizowany.')
            return redirect('user_management:profile', username=request.user.username)
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'user_management/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
@require_POST
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)

    if request.user != user_to_follow:
        follow, created = Follow.objects.get_or_create(follower=request.user, followed=user_to_follow)
        if not created:
            follow.delete()
            action = 'unfollowed'
        else:
            action = 'followed'
    else:
        action = 'self'

    followers_count = user_to_follow.followers.count()
    return JsonResponse({'status': 'ok', 'action': action, 'followers_count': followers_count})


@login_required
def check_follow_status(request, username):
    user_to_check = get_object_or_404(User, username=username)
    is_following = Follow.objects.filter(follower=request.user, followed=user_to_check).exists()
    return JsonResponse({'is_following': is_following})
