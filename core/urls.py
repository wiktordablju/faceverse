from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', LoginView.as_view(template_name='core/welcome.html'), name='login'),
    path('groups/', views.groups, name='groups'),
    path('friends/', views.friends, name='friends'),
    path('profile/', views.profile, name='profile'),

]
