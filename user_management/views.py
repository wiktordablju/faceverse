from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from post_management.forms import PostForm
from post_management.models import Post
from user_management.forms import ProfileForm, UserEditForm


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
    user_posts = Post.objects.filter(author=user, group__isnull=True).order_by('-created_at')
    user_groups = user.user_groups.all()
    form = PostForm()
    is_own_profile = (request.user == user)

    context = {
        'user': user,
        'posts': user_posts,
        'user_groups': user_groups,
        'is_own_profile': is_own_profile,
        'form': form
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
            return redirect('user_management:profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'user_management/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
