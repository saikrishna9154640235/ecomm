from django.db import models

# Create your models here.
from base.models import *


class Category(basemodel):
    category_name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True ,null=True,blank=True)

    category_image=models.ImageField(upload_to="categories")
    
class Product(basemodel):
    product_name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True ,null=True,blank=True)

    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    product_price=models.IntegerField(default=100)
    product_description=models.TextField()
    
class productimage(basemodel):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")
    image=models.ImageField(upload_to="products")