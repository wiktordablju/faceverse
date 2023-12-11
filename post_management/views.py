from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import PostForm, CommentForm, GroupPostForm
from .models import Post
from group_management.models import Group


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('core:home')
    else:
        form = PostForm()
    return render(request, 'core/home.html', {'form': form})


@login_required
def create_group_post(request, group_id):
    group = Group.objects.get(id=group_id)
    if request.method == 'POST':
        form = GroupPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.group = group
            post.save()
            return redirect('group_management:group_detail', group_id=group_id)

    else:
        form = GroupPostForm()
    return render(request, 'post_management/create_group_post.html', {'form': form, 'group': group})


@login_required
@require_POST
def like_post(request):
    post_id = request.POST.get('id')
    post = Post.objects.get(id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return JsonResponse({'likes_count': post.likes.count(), 'is_liked': is_liked})


def add_comment_to_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'core:home'))
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})
