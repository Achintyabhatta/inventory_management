from django.urls import path
from . import views
from .views import *

app_name = 'inventory'

urlpatterns = [

    path('get-inventory', GetItemInInventory.as_view(), name='customer'),
    path('get-os-item', FetchOutOfStockItems.as_view(), name='customer'),
    path('get-supplier', GetSupplierList.as_view(), name='customer'),
    path('get-inventory-item', GetItemsInInventory.as_view(), name='customer'),
    path('increment-count', IncrementItemCountInInventory.as_view(), name='customer'),
    path('decrement-count', DecrementItemCountInInventory.as_view(), name='healthRecord')
]
