from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required(login_url='core:welcome')
def profile(request):
    return render(request, 'user_management/profile.html')


@login_required(login_url='core:welcome')
def friends(request):
    return render(request, 'user_management/friends.html')


def logout_view(request):
    logout(request)
    return redirect('core:welcome')
