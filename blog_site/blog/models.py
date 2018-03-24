from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
from PIL import Image


class Category(models.Model):
    category = models.CharField(max_length=250, blank=True, unique=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category':self.category})

    def __str__(self):
        return self.category



class Post(models.Model):



    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    video_link = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/')
    category = models.ManyToManyField(Category,
                                blank=True,
    )


    def get_absolute_url(self):
        return reverse('detail', kwargs ={'pk':self.id})


    def __str__(self):
        return self.title + ' - ' + self.description



class Testimony(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    testimony = models.TextField(max_length=200, blank=True)


class Email_List(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self):
        return self.email



# Create your models here.
