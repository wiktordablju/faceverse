from django.urls import path
from . import views

app_name = 'post_management'

urlpatterns = [
    path('create_post/', views.create_post, name='create_post'),
    path('like_post/', views.like_post, name='like_post'),
    path('post/<int:post_id>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

]
