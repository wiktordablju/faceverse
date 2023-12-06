from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import GroupForm
from .models import Group


@login_required
def groups(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            group.members.add(request.user)
            return redirect('group_management:groups')
    else:
        form = GroupForm()
    return render(request, 'group_management/groups.html', {'form': form})
