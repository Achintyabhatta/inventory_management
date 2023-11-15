from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer, HealthRecord, Order
from .helper import *
from .imports import *
from .response_handler import *

# Returns the Item with details for items that are in stock
class GetItemInInventory(APIView):
    def post(self, request):
        jwtResponse = NewAuthenticateJWTtoken(request)
        validToken = jwtResponse["isValid"]
        if not validToken:
            return WriteErrorMessageBadRequest("Invalid Token passed")
        try:
            inventory = Inventory.objects.filter(item_count__gt=0) # In Stock Item
        except Inventory.DoesNotExist:
            inventory = None
        except: # There some other Issue in accessing the database
            return WriteErrorMessageInternalServerError("server down")
        return WriteSuccessMessageWithData(list(inventory.values()))
    
# Get Out of stock Items  - Internal API { Not exposed to Customer }
class FetchOutOfStockItems(APIView):
    def get(self, request):
        try:
            inventory = Inventory.objects.filter(item_count=0) # In Stock Item
        except Inventory.DoesNotExist:
            inventory = None
        except: # There some other Issue in accessing the database
            return WriteErrorMessageInternalServerError("server down")
        return WriteSuccessMessageWithData(list(inventory.values()))
    
# Returns Supplier Details  - Internal API { Not exposed to Customer }
class GetSupplierList(APIView):
    def post(self, request):
        try:
            supplier = SupplierList.objects.filter() # In Stock Item
        except SupplierList.DoesNotExist:
            supplier = None
        except: # There some other Issue in accessing the database
            return WriteErrorMessageInternalServerError("server down")
        return WriteSuccessMessageWithData(list(supplier.values()))    

# Internal APIs
class GetItemsInInventory(APIView):
    def post(self, request):
        try:
            inventory = Inventory.objects.filter(item_count__gt=0) # In Stock Item
        except Inventory.DoesNotExist:
            inventory = None
        except: # There some other Issue in accessing the database
            return WriteErrorMessageInternalServerError("server down")
        return WriteSuccessMessageWithData(list(inventory.values()))
    
class IncrementItemCountInInventory(APIView):
    @transaction.atomic
    def post(self, request):
        itemID = request.data["itemID"]
        count = request.data["count"]
        try:
            inventory = Inventory.objects.get(id = itemID) # In Stock Item
            inventory.item_count = inventory.item_count + int(count)
            inventory.save()
        except Inventory.DoesNotExist:
            return WriteErrorMessageBadRequest("item does not exist")
        except Exception as e: 
            return WriteErrorMessageInternalServerError(str(e))
        return WriteSuccessMessageWithData(list(inventory.values()))
    
class DecrementItemCountInInventory(APIView):
    @transaction.atomic
    def post(self, request):
        itemID = request.data["itemID"]
        count = request.data["count"]
        try:
            inventory = Inventory.objects.get(id = itemID) # In Stock Item
            inventory.item_count = inventory.item_count - int(count)
            inventory.save()
        except Inventory.DoesNotExist:
            return WriteErrorMessageBadRequest("item does not exist")
        except Exception as e: 
            return WriteErrorMessageInternalServerError(str(e))
        return WriteSuccessMessageWithData(list(inventory.values()))