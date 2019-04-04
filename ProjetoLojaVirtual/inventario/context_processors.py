from .models import Inventory

def inventory(request):
    return{
        'inventory': Inventory.objects.all()
    }