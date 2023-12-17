from . import views
from django.urls import path
from django.contrib.auth.views import LoginView

app_name = 'core'


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('home/', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='core/welcome.html'), name='login'),
]
