from django.urls import path
from . import views 

urlpatterns = [
    path('shop/<slug:slug>?',views.product,name='product'),
]