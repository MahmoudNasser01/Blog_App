from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_post', views.add_post, name="add_post"),
    path('post_list', views.post_list, name="post_list"),
    path('<str:slug>', views.post_detials, name="post_detials"),
]