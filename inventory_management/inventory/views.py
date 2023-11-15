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
        
        

        return WriteSuccessMessage()
    
# Get Out of stock Items  - Internal API { Not exposed to Customer }
class FetchOutOfStockItems(APIView):
    def get(self, request):
        return WriteSuccessMessage()
    
# Returns Supplier Details  - Internal API { Not exposed to Customer }
class GetSupplierList(APIView):
    def post(self, request):
        return WriteSuccessMessage()
    