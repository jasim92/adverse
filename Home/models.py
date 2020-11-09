from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Homedb(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to="media/images", default="")

    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_id = models.AutoField
    product_title = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='media', default="")
    auther = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.product_title