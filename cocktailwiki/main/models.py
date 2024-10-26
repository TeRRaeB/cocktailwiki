from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_POST = (
        (0, "Created"),
        (1, "Published"),
        (2, "Denied")
    )
    title = models.CharField(max_length=2500)
    content = models.TextField()
    image = models.ImageField('Image', null=False, upload_to='media')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(STATUS_POST, default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'


class Message(models.Model):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
