from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to = 'mapicha/')
    image_name = models.CharField(max_length=100)
    image_caption = models.CharField(max_length=100)
    mtumiaji = models.ForeignKey(User, on_delete= models.CASCADE)
    timed_created = models.DateTimeField(auto_now_add = True)
    likes = models.IntegerField(null = True, default=0) #avoid adding comments field so as to be able to link it to the user logged in

    def __str__(self) -> str:
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Comment(models.Model):
    body = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    mtumiaji = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.post

class Profile(models.Model):
    photo =models.ImageField(upload_to = 'mapicha/')
    bio = models.TextField(default='Bio',max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.username} Profile'

class NewPost(models.Model):
    image = models.ImageField(upload_to = 'mapicha/')
