from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_save
from reselling.utils import unique_slug_generator
from reselling.utilsA import unique_slug_generator_for_user
import random
import uuid


class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    location = models.CharField(max_length=200)
    profile = models.ImageField(default="media/default/user.png")
    slug = models.SlugField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.username)


def slug_generator_for_user(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_for_user(instance)


pre_save.connect(slug_generator_for_user, sender=UserProfile)


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Post)


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    commentfrom = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class Images(models.Model):
    image = models.FileField(upload_to='postimages', default="media/default/noimage.png")
    postImage = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.postImage)
