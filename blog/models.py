from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from django.urls import reverse
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    post_image = models.ImageField(default="blog_default.jpg", upload_to="blog_pics")
    blog_view = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name="collected_votes")
    blog_comment = models.PositiveIntegerField(default=0)



    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # this function already exists in our super() we are ovveriding it to make sure images are uploaded on the scale we want them to be
        super().save(*args, **kwargs)

        img = Image.open(self.post_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.post_image.path)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments") 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_user", null=True) 
    # name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.post.title}"