from django.urls import path
from . import views



urlpatterns = [
    path("login/",views.login_page,name="login"),
    path("register",views.register,name='register'),
    path("activate/<email_token>/",views.activate_email ,name="activate_email")
]
