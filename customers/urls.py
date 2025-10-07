from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='customers_profile'),
    path('orders/', views.my_orders, name='customers_orders'),
]


