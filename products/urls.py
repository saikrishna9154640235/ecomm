from products.views import *
from django.urls import path

urlpatterns = [
    path("cart_items",cart_items,name="cart_item"),
    path('<slug>/' ,get_product, name="product_get"),
    path("additems/<product_uid>/",add_cart,name="add_cart"),
    path('cart_items_remove/<remove>/',cart_items_remove,name='rems'),
   
    path("remove_cupon/<remove_coupon>/",remove_cart_coupon,name='remove'),
    path('success/',success, name='success'),
]

