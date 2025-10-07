from django.shortcuts import render
from catalog.models import Product
from drops.models import Collection
from django.utils import timezone


def home_view(request):
    featured_products = Product.objects.filter(active=True).order_by('-created_at')[:6]
    now = timezone.now()
    active_collections = Collection.objects.filter(
        is_active=True,
        starts_at__lte=now,
        ends_at__gte=now
    ).order_by('-starts_at')
    return render(request, 'home.html', {
        'featured_products': featured_products,
        'active_collections': active_collections
    })
