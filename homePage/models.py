from django.db import models
from django.contrib.auth.models import User

# This is my Post Model.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
)
    image = models.ImageField(default='fallback.png', blank=False)
    caption = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="commenter")
    comments = models.TextField()                           
    created_on = models.DateTimeField(auto_now_add=True)
    


class Meeting(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="meetings")
    platform = models.CharField(max_length=200, unique=True)
    venue = models.CharField(max_length=200, unique=True)
    discription = models.TextField()
    start_time = models.DateTimeField()


