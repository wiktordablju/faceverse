from django.shortcuts import render
from django.http import HttpResponse

def registration(request):
    return HttpResponse("Strona rejestracji działa!")

