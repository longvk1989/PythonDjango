from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('hellohtml/', views.hello_html, name='hello_html'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_id>/delete', views.delete_post, name='delete_post'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]