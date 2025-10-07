from django.db import models
from django.utils.text import slugify
import uuid


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    sku = models.CharField(max_length=64, unique=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate unique slug with UUID
            base = slugify(self.name)
            unique_id = str(uuid.uuid4())[:8]
            self.slug = f"{base}-{unique_id}"
        if not self.sku:
            # Generate unique SKU using UUID
            base = slugify(self.name)[:20]
            unique_id = str(uuid.uuid4())[:8]
            self.sku = f"{base}-{unique_id}"
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

# Create your models here.
