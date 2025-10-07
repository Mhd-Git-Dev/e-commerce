from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='catalog_index'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
]


