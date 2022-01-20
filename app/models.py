from django.utils import timezone
from unicodedata import category
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django_toggle_m2m.toggle import ToggleManyToMany


class User(AbstractUser):

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Location(models.Model):
    # number = models.IntegerField(Holding off on this for the moment.)
    #grocery_store = models.Charfield(max_length=250)
    #isle_number
    pass

class Category(models.Model):
    category =  models.CharField(max_length=250)

class Tag(models.Model):
    tag = models.CharField(max_length=250)

class Product(models.Model):
    name = models.CharField(max_length=250)
    image = models.URLField(max_length=200, null=True, blank=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    locations = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='locations')

class List(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    users = models.ManyToManyField('User', related_name='lists', blank=True) 
    tags = models.ManyToManyField('Tag', related_name='lists', blank=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)

    
class ListItem(models.Model):
    products = models.ManyToManyField('Product', related_name='items', blank=True)  
    item_quantity = models.PositiveIntegerField(default=1)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='list', blank=True, null=True)
