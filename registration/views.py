from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms


def registration(request):
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = forms.UserRegistrationForm()

        if request.user.is_authenticated:
            user_name = request.user.username  # Pobiera nazwę zalogowanego użytkownika
        else:
            user_name = None  # Ustawia None, jeśli użytkownik nie jest zalogowany
    return render(request, 'registration/registration.html', {'form': form, 'user_name': user_name})
