from django.db import models
from django.utils.html import format_html
from django.utils import timezone
# from django.contrib.auth.models import AbstractUser


# Create your models here.
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category/")
    add_date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
       return self.title

#food models
class Food(models.Model):
    food_id = models.AutoField(primary_key=True,default=timezone.now())
    title=models.CharField(max_length=100)
    price=models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="food/")
   
    def __str__(self):
        return self.title 
    
class OrderTable(models.Model):
    order_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.CharField(max_length=100)
    order = models.CharField(max_length=955)
    note = models.TextField()

    def __str__(self):
        return f"Order for {self.user}"
    
