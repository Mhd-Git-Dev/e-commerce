from django.db import models
from django.utils import timezone


class Collection(models.Model):
    name = models.CharField(max_length=200)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    image_url = models.URLField(null=True, blank=True)

    def is_live(self) -> bool:
        now = timezone.now()
        return self.is_active and self.starts_at <= now <= self.ends_at

    def __str__(self) -> str:
        return self.name


class DropItem(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, related_name='drop_items')
    limited_stock = models.PositiveIntegerField()
    sold = models.PositiveIntegerField(default=0)
    price_override = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    visible = models.BooleanField(default=True)

    class Meta:
        unique_together = ('collection', 'product')

    @property
    def remaining(self) -> int:
        return max(0, self.limited_stock - self.sold)

    def __str__(self) -> str:
        return f"{self.product} in {self.collection}"

# Create your models here.
