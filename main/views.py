from django.shortcuts import render
from main.forms import ItemForm
from main.models import Item

# Create your views here.

def index(request):
    items = Item.objects.all().order_by('-value')

    form = ItemForm()

    context = {
        'form' : form,
        'items' : items,
    }

    return render(request, 'main/index.html', context)

#HTMX

def items(request):
    print('items=====')
    form = ItemForm(request.POST)

    if form.is_valid():
        form.save()
    else:
        form = ItemForm()

    items = Item.objects.all().order_by('-value')

    context = {
        'form' : form,
        'items' : items
    }

    return render(request, 'htmx/items.html', context)
