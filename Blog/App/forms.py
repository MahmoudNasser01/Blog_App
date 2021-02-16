from django.forms import ModelForm
from .models import Post, Comment



class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class AddComment(ModelForm):
    class  Meta:
        model = Comment
        fields = '__all__'
