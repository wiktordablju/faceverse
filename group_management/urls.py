from django.urls import path
from . import views

app_name = 'group_management'

urlpatterns = [
    path('', views.groups, name='groups'),
    path('<slug:group_slug>/', views.group_detail, name='group_detail'),
    path('<slug:group_slug>/edit/', views.edit_group, name='edit_group'),
]
