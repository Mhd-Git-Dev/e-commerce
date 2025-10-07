from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('accounts/', include('allauth.urls')),
    path('catalog/', include('catalog.urls')),
    path('drops/', include('drops.urls')),
    path('orders/', include('orders.urls')),
    path('payments/', include('payments.urls')),
    path('customers/', include('customers.urls')),
]
