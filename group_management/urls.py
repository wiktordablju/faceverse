from django.urls import path
from . import views

app_name = 'group_management'

urlpatterns = [
    path('', views.groups, name='groups'),
]
