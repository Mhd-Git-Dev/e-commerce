from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer


@receiver(post_save, sender=User)
def create_or_update_customer(sender, instance: User, created: bool, **kwargs):
    email = instance.email or f"user{instance.pk}@example.com"
    if created:
        Customer.objects.create(user=instance, email=email, first_name=instance.first_name, last_name=instance.last_name)
    else:
        try:
            customer = instance.customer
            customer.email = email
            customer.first_name = instance.first_name
            customer.last_name = instance.last_name
            customer.save(update_fields=["email", "first_name", "last_name"])
        except Customer.DoesNotExist:
            Customer.objects.create(user=instance, email=email)

