from django.urls import path
from . import views


app_name = 'user_management'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('friends/', views.friends, name='friends'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('<str:username>/', views.profile, name='profile'),

]
