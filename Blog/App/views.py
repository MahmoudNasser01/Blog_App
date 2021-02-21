from django.shortcuts import render, redirect, get_object_or_404
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
        else:
            print('Error in the post')
    context = {
        'form': form
    }
    return render(request, 'pages/add_post.html', context)

def post_list(request):
    posts = Post.objects.filter(publish=True).order_by('-publish_date')
    context = {
        'posts': posts
    }
    return render(request, 'pages/posts_list.html', context)



def manage_posts(request):
    posts = Post.objects.all()

    context = {
        'posts' : posts
    }
    return render(request, 'pages/manage_posts.html', context)




def post_detials(request, slug):
    post = get_object_or_404(Post, slug=slug)
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


def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = AddPostForm(instance=post)
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post.delete()
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'pages/edit_post.html', context)


def delete_post(request, slug):

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('manage_posts')

