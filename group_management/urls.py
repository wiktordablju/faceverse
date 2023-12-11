from django.urls import path
from . import views

app_name = 'group_management'

urlpatterns = [
    path('', views.groups, name='groups'),
    path('groups/<int:group_id>/', views.group_detail, name='group_detail'),
]
