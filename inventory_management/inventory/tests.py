from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Inventory, SupplierList

class FetchOutOfStockItemsTestCase(TestCase):
    def test_fetch_out_of_stock_items(self):
        # TODO: Add your test case for PlaceNewOrder view
        pass

class GetItemInInventoryTestCase(TestCase):
    def test_get_item_in_inventory(self):
        # TODO: Add your test case for PlaceNewOrder view
        pass

class InventoryModelTestCase(TestCase):
    def test_inventory_model_str(self):
        # TODO: Add your test case for PlaceNewOrder view
        pass

class SupplierListTestCase(TestCase):
    def test_supplier_list(self):
        # TODO: Add your test case for PlaceNewOrder view
        pass
