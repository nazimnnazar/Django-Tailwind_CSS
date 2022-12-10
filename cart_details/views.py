from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import Product
from django.conf import settings
# Create your views here.


@login_required
def cheout(request):
    pub_key = settings.STRIPE_API_KEY_PUBLISHABLE 
    return render(request,'cart/cheout.html',{'pub_key':pub_key})