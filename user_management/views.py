from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
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
def profile(request):
    user_posts = Post.objects.filter(author=request.user, group__isnull=True).order_by('-created_at')
    form = PostForm()
    user_groups = request.user.user_groups.all()  # Pobranie grup, do których należy użytkownik

    context = {
        'form': form,
        'posts': user_posts,
        'user_groups': user_groups,  # Dodanie listy grup do kontekstu
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
