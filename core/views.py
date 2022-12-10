from django.db.models import Q
from django.shortcuts import render,redirect
from product.models import Product,Category
from django.contrib.auth.decorators import login_required
from.forms import SignUpForm
from django.contrib.auth import login
# Create your views here.
def frontpage(request):
    product=Product.objects.all()[0:8]
    context={'product':product}
    return render(request,'core/frontpage.html',context)

def singup(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    else:
        form =SignUpForm()
    context={
        'form':form
        }
    return render(request,'core/singup.html',context)
    
def loginsign(request):
    return render(request,'core/login.html')

def shop(request):
    category=Category.objects.all()
    product=Product.objects.all()
    
    active_category=request.GET.get('category','')
  

    if active_category:
        product = product.filter(category__slug=active_category)
    
    query = request.GET.get('query','')
    if query:
        product = product.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context={
        'category':category,
        'product':product,
        'active_category':active_category
        }
    return render(request,'core/shop.html',context)

def hx_menu_cart(request):
    return render(request,'cart/menu_cart.html')

def about(request):
    return render(request,'core/about_details.html')