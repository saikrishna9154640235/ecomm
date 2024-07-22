from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from products.models import Cart
from django.http import HttpResponse
# Create your views here.
def Index(request):
    products=Product.objects.all()
    context={"products":products}
    return render(request,'home/index.html',context)



def success(request):
    order_id = request.GET.get('order_id')
    
    cart = Cart.objects.get(razor_pay_order_id=order_id)
    
    
    cart.is_paid = True
    cart.save()
    
    # You can redirect to a success page or return a success message here
    return HttpResponse("Payment successful!")