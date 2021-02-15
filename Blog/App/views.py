from django.shortcuts import render




def post_list(request):
    return render(request, 'pages/posts_list.html')

