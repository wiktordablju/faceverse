from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from post_management.models import Post
from .forms import GroupForm, GroupEditForm
from .models import Group, User
from post_management.forms import GroupPostForm
from django.utils.text import slugify  # Dodane importowanie slugify


@login_required
def groups(request):
    all_groups = Group.objects.all()
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            group.members.add(request.user)
            group.moderators.add(request.user)
            return redirect('group_management:groups')
    else:
        form = GroupForm()
    return render(request, 'group_management/groups.html', {'form': form, 'groups': all_groups})


@login_required
def group_detail(request, group_slug):  # Zmieniono group_id na group_slug
    group = get_object_or_404(Group, slug=group_slug)  # Zmieniono ID na slug
    user_is_member = request.user in group.members.all()
    user_is_moderator = request.user in group.moderators.all()

    if request.method == 'POST':
        if 'join_group' in request.POST:
            group.members.add(request.user)
            user_is_member = True
        elif 'promote_member' in request.POST:
            member_id = request.POST.get('member_id')
            member_to_promote = get_object_or_404(User, id=member_id)

            if member_to_promote in group.members.all() and not member_to_promote in group.moderators.all():
                group.moderators.add(member_to_promote)
                messages.success(request, f'{member_to_promote.username} został awansowany na moderatora.')
        elif user_is_member:
            post_form = GroupPostForm(request.POST)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.author = request.user
                post.group = group
                post.save()
                return redirect('group_management:group_detail',
                                group_slug=group.slug)  # Zmieniono group_id na group_slug

    post_form = GroupPostForm() if user_is_member else None
    posts = Post.objects.filter(group=group).order_by('-created_at') if user_is_member else []
    members = group.members.all() if user_is_moderator else None

    return render(request, 'group_management/group_detail.html', {
        'group': group,
        'post_form': post_form,
        'posts': posts,
        'user_is_member': user_is_member,
        'user_is_moderator': user_is_moderator,
        'members': members
    })


@login_required
def edit_group(request, group_slug):  # Zmieniono group_id na group_slug
    group = get_object_or_404(Group, slug=group_slug)  # Zmieniono ID na slug

    if request.user not in group.moderators.all():
        return redirect('group_management:group_detail', group_slug=group.slug)  # Zmieniono group_id na group_slug

    if request.method == 'POST':
        form = GroupEditForm(request.POST, request.FILES, instance=group)
        if form.is_valid():
            form.save()
            messages.success(request, 'Grupa została zaktualizowana.')
            return redirect('group_management:group_detail', group_slug=group.slug)  # Zmieniono group_id na group_slug
    else:
        form = GroupEditForm(instance=group)

    return render(request, 'group_management/edit_group.html', {'form': form, 'group': group})
