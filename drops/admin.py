from django.contrib import admin
from .models import Collection, DropItem


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("name", "starts_at", "ends_at", "is_active")


@admin.register(DropItem)
class DropItemAdmin(admin.ModelAdmin):
    list_display = ("collection", "product", "limited_stock", "sold", "remaining", "visible")

# Register your models here.
