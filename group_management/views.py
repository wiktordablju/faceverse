from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from post_management.models import Post
from .forms import GroupForm
from .models import Group
from post_management.forms import GroupPostForm


@login_required
def groups(request):
    all_groups = Group.objects.all()
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            group.members.add(request.user)
            return redirect('group_management:groups')
    else:
        form = GroupForm()
    return render(request, 'group_management/groups.html', {'form': form, 'groups': all_groups})


@login_required
def group_detail(request, group_id):
    group = Group.objects.get(id=group_id)
    posts = Post.objects.filter(group=group).order_by('-created_at')
    post_form = GroupPostForm()

    if request.method == 'POST':
        post_form = GroupPostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.group = group  # Ustawienie grupy bezpośrednio w widoku
            post.save()
            return redirect('group_management:group_detail', group_id=group.id)

    return render(request, 'group_management/group_detail.html', {'group': group, 'post_form': post_form, 'posts': posts})


