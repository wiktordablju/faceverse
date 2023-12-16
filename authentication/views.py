from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Zaktualizowane przekierowanie z uwzględnieniem username
            return redirect('user_management:profile', username=user.username)
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})
