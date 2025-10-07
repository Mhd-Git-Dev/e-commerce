from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from orders.models import Order


@login_required
def profile(request):
    customer = getattr(request.user, 'customer', None)
    return render(request, 'customers/profile.html', {"customer": customer})


@login_required
def my_orders(request):
    orders = Order.objects.filter(email=request.user.email).order_by('-created_at')
    return render(request, 'customers/my_orders.html', {"orders": orders})




def index(request):
    return render(request, "customers/index.html")

# Create your views here.
