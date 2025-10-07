from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from catalog.models import Product
from drops.models import Collection, DropItem
from customers.models import Customer
from orders.models import Order, OrderItem
import random
from django.utils import timezone

class Command(BaseCommand):
    help = 'Peuple la base avec des données de démo'

    def handle(self, *args, **options):
        # Nettoyer les anciennes données
        User.objects.all().delete()
        
        # Créer un superutilisateur
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@merch.shop',
            password='adminpass'
        )
        
        # Créer 10 produits
        products = []
        for i in range(1, 11):
            product = Product.objects.create(
                name=f'T-Shirt Édition Limitée #{i}',
                description=f"Design exclusif n°{i} - Coton 240g/m²",
                price=39.99 + i,
                image_url=f'https://via.placeholder.com/400x300?text=Prod+{i}'
            )
            products.append(product)
            self.stdout.write(f'Produit créé : {product.name}')

        # Créer 3 collections
        now = timezone.now()
        collections = [
            Collection.objects.create(
                name=f'Collection Printemps 202{i}',
                starts_at=now - timezone.timedelta(days=2),
                ends_at=now + timezone.timedelta(days=7),
                is_active=True
            ),
            Collection.objects.create(
                name='Événement Spécial ESport',
                starts_at=now + timezone.timedelta(days=3),
                ends_at=now + timezone.timedelta(days=10)
            ),
            Collection.objects.create(
                name='Drop Rétro',
                starts_at=now - timezone.timedelta(days=30),
                ends_at=now - timezone.timedelta(days=15)
            )
        ]

        # Ajouter des produits aux collections
        for collection in collections:
            for product in random.sample(products, 5):
                DropItem.objects.create(
                    collection=collection,
                    product=product,
                    limited_stock=random.randint(50, 200),
                    price_override=product.price * 0.9 if random.random() > 0.5 else None
                )

        # Créer un client test
        user = User.objects.create_user(
            username='client_test',
            email='client@test.com',
            password='testpass'
        )
        customer = Customer.objects.get(user=user)
        
        # Créer des commandes
        for i in range(1, 4):
            order = Order.objects.create(
                email=user.email,
                customer=customer,
                status='paid' if i % 2 == 0 else 'shipped',
                shipping_address=f"{i} Rue de la Demo\n7500{i} Ville Test"
            )
            
            # Ajouter des articles
            items = random.sample(list(DropItem.objects.filter(collection=collections[0])), 3)
            for item in items:
                OrderItem.objects.create(
                    order=order,
                    drop_item=item,
                    quantity=random.randint(1, 3),
                    unit_price=item.price_override or item.product.price
                )

        self.stdout.write(self.style.SUCCESS('Données de démo générées avec succès!'))
