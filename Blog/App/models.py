from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Post(models.Model):

    STATUS = (
        ('PUBLISHED', 'PUBLISHED'),
        ('PANNED', 'PANNED'),
    )

    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1600)
    img = models.ImageField(upload_to='images')
    publish_date = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=50, choices=STATUS, default='PUBLISHED')
    author = models.ForeignKey(User, on_delete=models.CASCADE)


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





