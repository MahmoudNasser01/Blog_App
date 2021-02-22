from django.forms import ModelForm
from django import forms
from django.db import models
from .models import Post, Comment



class AddPostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)
        self.fields['content'].strip = False
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'title-field', 'placeholder': 'عنوان البوست', 'autocomplete': 'off'}),
            'content': forms.Textarea(attrs={'class': 'content-field', 'placeholder': 'ماذا تفكر في نشرة ؟؟'}),
            'photo': forms.FileInput(attrs={'class': 'content-field', 'placeholder': 'ماذا تفكر في نشرة ؟؟'}),
            'slug': forms.TextInput(attrs={'class': 'slug-field', 'placeholder': 'اضافه تاج للبوست', 'autocomplete': 'off'}),
        }



class AddComment(ModelForm):
    class  Meta:
        model = Comment
        fields = '__all__'


