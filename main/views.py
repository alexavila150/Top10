from django.shortcuts import render
from main.models import Item

# Create your views here.

def index(request):
    items = Item.objects.all().order_by('-value')

    context = {
        'items' : items
    }

    return render(request, 'main/index.html', context)