from django.db import models


class Payment(models.Model):
    order = models.OneToOneField('orders.Order', on_delete=models.CASCADE, related_name='payment')
    provider = models.CharField(max_length=50, default='demo')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='EUR')
    status = models.CharField(max_length=20, default='initiated')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Payment for order #{self.order_id} - {self.status}"

# Create your models here.
