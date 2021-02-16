from django.shortcuts import render, redirect
from .models import Post, Comment

from .forms import AddPostForm, AddComment



def home(request):
    return render(request, 'pages/home.html')


def add_post(request):
    form = AddPostForm()

    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    context = {
        'form': form
    }
    return render(request, 'pages/add_post.html', context)

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'pages/posts_list.html', context)



def post_detials(request, slug):
    post = Post.objects.get(slug=slug)

    form = AddComment()
    if request.method == 'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            form.save()


    comments = Comment.objects.all().filter(post_id=post.id)

    context = {
        'post': post,
        'comments': comments,
        'form': form

    }

    return render(request, 'pages/post_detials.html', context)
