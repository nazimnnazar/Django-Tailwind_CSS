from django.urls import path
from order.views import start_order

urlpatterns = [
    path('start_order/',start_order,name='start_order')
]