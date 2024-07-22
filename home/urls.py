from django.urls import path
from  . import views
from products.models import Cart

urlpatterns = [
    path("",views.Index),
    path("success/",views.success,name="success")
]
