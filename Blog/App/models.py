from django.db import models

from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse



class Post(models.Model):

    title = models.CharField(max_length=200, null=True)
    content = models.TextField(max_length=1600, null=True)
    photo = models.ImageField(upload_to='', blank=False, null=True)
    publish_date = models.DateTimeField(default=datetime.now, null=True)
    publish = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True,unique=True)


    def __str__(self):
        return f"{self.title} - {self.publish_date.year}/{self.publish_date.month}/{self.publish_date.day}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    content = models.TextField(max_length=500)
    publish_date = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return f"{self.author} - {self.post.title}"



    # Post

    #     - title
    #     - content
    #     - image
    #     - date and time
    #     - status ( Published - Draft)
    #     - likes
    #     - comments
    #     - author
    #
    # Comment
    #     - Author
    #     - Comment
    #     - Date & time






