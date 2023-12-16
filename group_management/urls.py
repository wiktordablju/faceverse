from django.urls import path
from . import views

app_name = 'group_management'

urlpatterns = [
    path('', views.groups, name='groups'),
    path('<int:group_id>/', views.group_detail, name='group_detail'),
    path('<int:group_id>/edit/', views.edit_group, name='edit_group'),
]
