from typing import Iterable
from django.db import models

# Create your models here.
from base.models import *
from django.utils.text import slugify
from django.contrib.auth.models import User

class Category(basemodel):
    category_name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True ,null=True,blank=True)
    category_image=models.ImageField(upload_to="categories")
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.category_name)
        super(Category,self).save(*args,**kwargs)
        
    def __str__(self) -> str:
        return self.category_name
    
class    Colorvariant(basemodel):
    color_name=models.CharField(max_length=100)
    color_price=models.IntegerField(default=1)     

    def __str__(self):
        return self.color_name
    
    
class Sizevariant(basemodel):
    size_name=models.CharField(max_length=100)  
    size_price=models.IntegerField(default=1)     
    def __str__(self)->str:
        return self.size_name
    
    
class Product(basemodel):
    product_name=models.CharField(max_length=100)
    size_price=models.IntegerField(default=1)     

    slug=models.SlugField(unique=True ,null=True,blank=True)

    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    product_price=models.IntegerField(default=100)
    product_description=models.TextField()
    color_variant=models.ManyToManyField( Colorvariant,blank=True)
    size_variant=models.ManyToManyField(Sizevariant ,blank=True , related_name='size_variants')
    qunatity=models.IntegerField(default=1)
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.product_name)
        super(Product,self).save(*args,**kwargs)

    def __str__(self) -> str:
        return self.product_name
    
class productimage(basemodel):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")
    image=models.ImageField(upload_to="products")
    
class Coupon(basemodel):
    coupon_code=models.CharField(max_length=10)
    is_expired=models.BooleanField(default=False)
    dicount_price=models.IntegerField(default=100)
    minimum_amount=models.IntegerField(default=100)
               
from django.db.models import Sum    
class Cart(basemodel):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE ,related_name="carts") 
    coupon=models.ForeignKey(Coupon, on_delete=models.SET_NULL,null=True,blank=True)
    is_paid=models.BooleanField(default=False)
    razor_pay_order_id=models.CharField(max_length=100,null=True,blank=True)
    razor_pay_payment_id=models.CharField(max_length=100,null=True,blank=True)
    razor_pay_payment_signature=models.CharField(max_length=100,null=True,blank=True)

    def get_cart_total(self):
        cart= Cartitems.objects.filter(cart=self).aggregate(Sum('product__product_price'))['product__product_price__sum']
        if self.coupon:
            if self.coupon.minimum_amount<cart:
               return cart-self.coupon.dicount_price
        

class Cartitems(basemodel):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cart_items")
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="carts_item")
    


