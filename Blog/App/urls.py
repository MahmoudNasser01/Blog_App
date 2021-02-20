from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_post', views.add_post, name="add_post"),
    path('post_list', views.post_list, name="post_list"),
    path('manage_posts', views.manage_posts, name="manage_posts"),
    path('post/<str:slug>', views.post_detials, name="post_detials"),
    path('manage_posts/delete_post/<str:slug>', views.delete_post, name="delete_post"),
    path('manage_posts/edit_post/<str:slug>', views.edit_post, name="edit_post")
]