from django.shortcuts import render,redirect
from .models import *
from django.db.models import Count
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from razorpay import Client
# Create your views here.
def get_product(request,slug):
    product=Product.objects.get(slug=slug)
    total_items=Cartitems.objects.filter(product=product).aggregate(total_items=Count('product__product_price'))
    
    if product.product_price>=10 or product.product_price<=20:
        print()
    else:
        print("noo")    
    context={"product":product,'total_items':total_items}
    return render(request,'products/products.html' ,context)
 
def add_cart(request,product_uid):
    user=request.user
    product=Product.objects.get(uid=product_uid)
   
    cart,create=Cart.objects.get_or_create(user=user,is_paid=False)
    
    if isinstance(cart, tuple):
        cart = cart[0] 
        
    cart_items=Cartitems.objects.create(
        product=product,
        cart=cart,
    )    
    
    return redirect('/')
from django.db.models import Sum
from django.conf import settings
def cart_items(request):
    cart = Cart.objects.get(is_paid=False, user=request.user) 
    total_price = Cartitems.objects.filter(cart=cart).aggregate(total_price=Sum('product__product_price'))['total_price'] or 0    




    if request.method=='POST':
        
        coupon=request.POST.get('coupon')
        coupon_obj=Coupon.objects.filter(coupon_code__icontains=coupon)
        if not coupon_obj.exists():
            messages.warning(request, "invalid coupon.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        if cart.coupon:
            messages.warning(request, "coupon already exists.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if cart.get_cart_total() is not None and cart.get_cart_total() <  coupon_obj.minimum_amount:
            messages.warning(request, "less amount coupon.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            
        cart.coupon=coupon_obj[0]
        cart.save()   
          
    client = Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
  
    payment=client.order.create({'amount':total_price*100,'currency':'INR','payment_capture':1})
    # Get all cart items associated with the cart
    cart.razor_pay_order_id=payment['id']
    cart.save()
    print(client)
    print(payment)
    
    total_price = Cartitems.objects.filter(cart=cart).aggregate(total_price=Sum('product__product_price'))['total_price'] or 0
    print(total_price,"h1")
    context={"cart":cart,'total_price':total_price,'payment':payment}
    return render(request,'cart_item/cart.html',context)

    
def cart_items_remove(request,remove):
    Cartitems.objects.get(uid=remove).delete()
    return redirect('/products/cart_items')

def remove_cart_coupon(request,remove_coupon):
    cart=Cart.objects.get(uid=remove_coupon)
    cart.coupon=None
    cart.save()
    messages.warning(request, "coupon already exists.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





from django.shortcuts import HttpResponse
from .models import Cart

def success(request):
    order_id = request.GET.get('order_id')
    
    cart = Cart.objects.get(razor_pay_order_id=order_id)
    
    
    cart.is_paid = True
    cart.save()
    
    # You can redirect to a success page or return a success message here
    return HttpResponse("Payment successful!")