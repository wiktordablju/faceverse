from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='core:welcome')
def groups(request):
    return render(request, 'group_management/groups.html')
