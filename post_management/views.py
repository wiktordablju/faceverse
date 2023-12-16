from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import PostForm, CommentForm, GroupPostForm
from .models import Post
from group_management.models import Group

def create_post(request):
    redirect_url = request.META.get('HTTP_REFERER', 'user_management:profile')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(redirect_url)  # Przekieruj na poprzednią stronę
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'post_management/create_post.html', context)

@login_required
def create_group_post(request, group_slug):  # Zmienione na 'group_slug'
    try:
        group = Group.objects.get(slug=group_slug)  # Użyj sluga grupy
    except Group.DoesNotExist:
        raise Http404("Grupa o danym slugu nie istnieje")  # Rzuć wyjątek 404, jeśli grupa nie istnieje

    if request.method == 'POST':
        form = GroupPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.group = group
            post.save()
            return redirect('group_management:group_detail', group_slug=group_slug)  # Przekieruj na szczegóły grupy

    else:
        form = GroupPostForm()
    return render(request, 'post_management/create_group_post.html', {'form': form, 'group_slug': group_slug})

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

        if form.is_valid() and form.cleaned_data['content']:  # Sprawdź, czy pole komentarza nie jest puste
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'core:home'))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'core:home'))
