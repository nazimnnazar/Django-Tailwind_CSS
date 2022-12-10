from django.contrib.auth import views
from django.urls import path
from cart.views import myaccount,editaccount,update_cart,cart_details,hx_cart_total,succes
urlpatterns = [
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('myaccount/',myaccount,name='myaccount'),
    path('succes/',succes,name='succes'),
    path('update_cart/<int:product_id>/<str:action>/', update_cart, name='update_cart'),
    path('cart/',cart_details,name='cart'),
    path('editaccount/',editaccount,name='editaccount'),
    path('hx_cart_total/',hx_cart_total,name='hx_cart_total'),
]