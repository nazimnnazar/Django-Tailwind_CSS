from django.shortcuts import render,redirect
from .cart import Cart
from django.contrib.auth.decorators import login_required
from product.models import Product

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return render(request,'cart/menu_cart.html')

@login_required
def myaccount(request):
    return render(request,'core/myaccount.html')
def succes(request):
    return render(request,'cart/succes.html')

def editaccount(request):
    if request.method == 'POST':
        user = request.user
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        user.email=request.POST.get('email')
        user.username=request.POST.get('username')
        user.save()
        return redirect('myaccount')
    return render(request,'core/editaccount.html')

def update_cart(request, product_id, action):
    cart = Cart(request)

    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)
    
    product = Product.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)
    
    if quantity:
        quantity = quantity['quantity']

        item = {
            'product': {
                'id': product.id,
                'name': product.name,
                'image': product.image,
                'get_thumbnail': product.get_thumbnail(),
                'price': product.price,
            },
            'total_price': (quantity * product.price) ,
            'quantity': quantity,
        }
    else:
        item = None

    response = render(request, 'cart/partials/cart_item.html', {'item': item})
    response['HX-Trigger'] = 'update-menu-cart'

    return response

def cart_details(request):
    return render(request,'cart/cart.html')

def hx_cart_total(request):
    return render(request,'cart/partials/cart_total.html')