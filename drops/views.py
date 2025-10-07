from django.shortcuts import render
from django.utils import timezone
from .models import Collection


def index(request):
    now = timezone.now()
    collections = Collection.objects.order_by('-starts_at')
    live = [c for c in collections if c.is_live()]
    upcoming = [c for c in collections if c.starts_at > now]
    past = [c for c in collections if c.ends_at < now]
    return render(request, "drops/index.html", {"live": live, "upcoming": upcoming, "past": past})

# Create your views here.
