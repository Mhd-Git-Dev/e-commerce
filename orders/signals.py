from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import OrderItem


@receiver(pre_save, sender=OrderItem)
def set_unit_price_and_validate_stock(sender, instance: OrderItem, **kwargs):
    drop_item = instance.drop_item
    unit_price = drop_item.price_override or drop_item.product.price
    instance.unit_price = unit_price
    if instance.pk is None:
        # creating new item: ensure enough remaining stock
        if instance.quantity > drop_item.remaining:
            raise ValueError("Not enough stock remaining for this drop item")


@receiver(post_save, sender=OrderItem)
def increment_sold(sender, instance: OrderItem, created: bool, **kwargs):
    if created:
        drop_item = instance.drop_item
        drop_item.sold = drop_item.sold + instance.quantity
        drop_item.save(update_fields=["sold"])

