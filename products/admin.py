from django.contrib import admin
from products.models import *
# Register your models here.

admin.site.register(Category)

class ProductImageAdmin(admin.StackedInline):
    model=productimage
class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name','product_price','product_description']
    inlines=[ProductImageAdmin]  
    
    
     
@admin.register(Colorvariant)  
class ColorvariantAdmin(admin.ModelAdmin):
    list_display=['color_price']
    model=Colorvariant
    
    
    
@admin.register(Sizevariant)  
class  SizevariantAdmin(admin.ModelAdmin):
    model=Sizevariant    
    
    
     
    
admin.site.register(Product,ProductAdmin) 
admin.site.register(productimage)    
admin.site.register(Cart)
admin.site.register(Cartitems)
admin.site.register(Coupon)