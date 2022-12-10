from django.urls import path,include
from django.contrib.auth import views
from cart.views import add_to_cart
from core.views import frontpage,shop,singup,hx_menu_cart,about
urlpatterns = [

    path('',frontpage,name='frontpage'),
    path('add_to_cart/<int:product_id>/',add_to_cart,name='add_to_cart'),
    path('shop/',shop,name='shop'),
    path('singup/',singup,name='singup'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('hx_menu_cart/',hx_menu_cart,name='hx_menu_cart'),
    path('about/',about,name='about'),
    
]