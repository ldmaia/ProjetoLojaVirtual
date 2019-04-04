from django.shortcuts import render
from .models import Inventory,Item

def item_list(request):
    context = {
        'item_list': Item.objects.all()
    }
    return render(request, 'inventario/item_list.html',context)


def inventory(request,slug):
    inventory = Inventory.objects.get(slug=slug)
    context = {
        'current_inventory': inventory,
        'item_list': Item.objects.filter(inventory = inventory),
    }
    return render(request, 'inventario/inventory.html', context)

def item(request,slug):
    item = Item.objects.get(slug=slug)
    context = {
        'item': item
    }
    return render(request, 'inventario/item.html',context)

# Create your views here.
